import argparse
from dataclasses import asdict, replace
import hashlib
import json
from pathlib import Path

import pandas as pd

from constraints import EXOGENOUS, SENSITIVITY_OUTCOMES_ONLY, SIZE_VARS, _base_name
from data_prep import DATASETS
from golem_model import FitConfig, extract_graph, fit_many, vocabulary
from pc_learning import (
    CONTINUOUS_PREDICTORS, CONTINUOUS_OUTCOMES, DISCRETIZED_PREDICTORS,
    DISCRETIZED_OUTCOMES, SIZE_CONTROL_PREDICTORS, load_continuous,
    load_discretized, count_temporal_violations,
)

ROOT = Path(__file__).resolve().parent.parent
SPARSITIES = [0.01, 0.02, 0.05]
THRESHOLDS = [0.05, 0.10, 0.20]


def suffix(version):
    return "" if version == "v4" else f"_{version}"


def paths(version, bootstrap=False):
    stem = "golem_bootstrap_stability" if bootstrap else "golem_settings_comparison"
    raw = "bootstrap_runs" if bootstrap else "golem_runs"
    return (ROOT / "reports" / f"{stem}{suffix(version)}.md",
            ROOT / "reports" / "golem_runs" / f"{raw}{suffix(version)}.json")


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False), encoding="utf-8")
    temporary.replace(path)


def panel_fingerprint(df):
    return hashlib.sha256(pd.util.hash_pandas_object(df, index=True).values.tobytes()
                          + "|".join(df.columns).encode()).hexdigest()


def model_nodes(representation, group="main"):
    continuous = representation == "continuous"
    predictors = list(CONTINUOUS_PREDICTORS if continuous else DISCRETIZED_PREDICTORS)
    outcomes = list(CONTINUOUS_OUTCOMES if continuous else DISCRETIZED_OUTCOMES)
    if group.startswith("sensitivity_outcome:"):
        outcome = group.split(":", 1)[1]
        outcomes = [outcome if continuous else f"{outcome}_bin"]
    elif group == "sensitivity_no_year":
        predictors = [n for n in predictors if _base_name(n) not in EXOGENOUS]
    elif group == "sensitivity_size_control":
        if not continuous:
            raise ValueError("PC size-control sensitivity is continuous only")
        predictors = list(SIZE_CONTROL_PREDICTORS)
    elif group != "main":
        raise ValueError(f"Unknown model group: {group}")
    return predictors + outcomes


def graph_result(fit, threshold, group="main"):
    result = dict(fit, threshold=threshold, group=group)
    if fit["strengths"] is None:
        return result
    result.update(extract_graph(fit["strengths"], fit["node_names"], threshold))
    result["n_temporal_violations_before"] = count_temporal_violations(result["thresholded_directed_edges"])
    result["n_temporal_violations"] = count_temporal_violations(result["directed_edges"])
    return result


def edge_recurrence(results):
    """One canonical unordered pair; preserve both directional counts."""
    counts = {}
    for r in results:
        directed = {tuple(_base_name(n) for n in e) for e in r.get("directed_edges", [])}
        undirected = {tuple(sorted(_base_name(n) for n in e)) for e in r.get("undirected_edges", [])}
        pairs = {tuple(sorted(e)) for e in directed} | undirected
        for a, b in pairs:
            entry = counts.setdefault((a, b), [0, 0, 0, 0])
            entry[0] += 1
            entry[1] += int((a, b) in directed)
            entry[2] += int((b, a) in directed)
            entry[3] += int((a, b) in undirected)
    columns = ["a", "b", "n_adjacent", "n_total", "adjacency_rate", "a_to_b_rate",
               "b_to_a_rate", "undirected_rate", "orientation_rate_given_adjacent",
               "a_to_b_given_adjacent", "b_to_a_given_adjacent", "undirected_given_adjacent"]
    rows = []
    for (a, b), (adj, ab, ba, und) in sorted(counts.items()):
        rows.append([a, b, adj, len(results), adj / len(results), ab / len(results),
                     ba / len(results), und / len(results), (ab + ba) / adj,
                     ab / adj, ba / adj, und / adj])
    table = pd.DataFrame(rows, columns=columns)
    return table.sort_values("adjacency_rate", ascending=False, kind="stable")


def compare_graphs(golem, pc):
    def edges(result):
        directed = {tuple(_base_name(n) for n in e) for e in result.get("directed_edges", [])}
        undirected = {tuple(sorted(_base_name(n) for n in e)) for e in result.get("undirected_edges", [])}
        other = {tuple(sorted((_base_name(e[0]), _base_name(e[1])))) for e in result.get("other_edges", [])}
        return directed, undirected, {tuple(sorted(e)) for e in directed} | undirected | other
    gd, gu, gs = edges(golem)
    pd_, pu, ps = edges(pc)
    return {"shared_adjacencies": len(gs & ps), "golem_only": len(gs - ps),
            "pc_only": len(ps - gs), "jaccard": len(gs & ps) / len(gs | ps) if gs | ps else 1.0,
            "direction_agreement": len(gd & pd_),
            "direction_reversals": len(gd & {(b, a) for a, b in pd_}),
            "shared_pc_undirected": len(gs & pu), "shared_golem_undirected": len(ps & gu)}


def load_pc(version, bootstrap=False):
    name = "bootstrap_runs" if bootstrap else "pc_runs"
    path = ROOT / "reports" / "pc_runs" / f"{name}{suffix(version)}.json"
    if not path.exists():
        return None, f"PC artifact unavailable: {path.relative_to(ROOT)}"
    try:
        return json.loads(path.read_text(encoding="utf-8")), str(path.relative_to(ROOT))
    except (ValueError, OSError) as exc:
        return None, f"PC artifact unavailable: {exc}"


def comparison_rows(results, pc_results):
    rows = []
    for index, g in enumerate(results):
        if g["status"] != "converged":
            continue
        for p in pc_results or []:
            if (p.get("group", "main"), p["representation"], p["constrained"]) != (
                    g["group"], g["representation"], g["constrained"]):
                continue
            # Older PC artifacts omit node_names; their group defines the full set,
            # including isolated nodes (which cannot be inferred from edge lists).
            pn = p.get("node_names", model_nodes(p["representation"], p.get("group", "main")))
            if {_base_name(n) for n in pn} != {_base_name(n) for n in g["node_names"]}:
                continue
            if p["n_rows"] != g["n_rows"]:
                continue
            rows.append({"golem_setting": index, "pc_test": p["indep_test"],
                         "pc_alpha": p["alpha"], **compare_graphs(g, p)})
    return rows


def run_grid(version, config=FitConfig(), sparsities=None, thresholds=None):
    sparsities = SPARSITIES if sparsities is None else sparsities
    thresholds = THRESHOLDS if thresholds is None else thresholds
    panels = {"continuous": load_continuous(version), "discretized": load_discretized(version)}
    results = []
    _, out = paths(version)
    groups = ["main"] + [f"sensitivity_outcome:{o}" for o in SENSITIVITY_OUTCOMES_ONLY] + ["sensitivity_no_year", "sensitivity_size_control"]
    for group in groups:
        for representation, df in panels.items():
            if group == "sensitivity_size_control" and representation != "continuous":
                continue
            names = model_nodes(representation, group)
            cats = vocabulary(df, names) if representation == "discretized" else None
            grid = group in ("main", "sensitivity_size_control")
            for constrained in (True, False):
                for penalty in sparsities if grid else [0.02]:
                    cfg = replace(config, lambda1=penalty)
                    fit = fit_many([df], names, representation, constrained, cfg, cats,
                                   SIZE_VARS if group == "sensitivity_size_control" else None)[0]
                    fit["input_fingerprint"] = panel_fingerprint(df)
                    for threshold in thresholds if grid else [0.10]:
                        results.append(graph_result(fit, threshold, group))
                    write_json(out, results)
                    print(f"{group} {representation} constrained={constrained} lambda={penalty}: "
                          f"{fit['status']} ({fit['iterations']} iterations)", flush=True)
    return results


def add_optimizer_arguments(parser):
    parser.add_argument("--version", choices=list(DATASETS), default="v4")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--lambda-dag", type=float, default=5.0)
    parser.add_argument("--learning-rate", type=float, default=0.001)
    parser.add_argument("--max-iter", type=int, default=10000)
    parser.add_argument("--tolerance", type=float, default=1e-7)
    parser.add_argument("--check-every", type=int, default=100)
    parser.add_argument("--patience", type=int, default=5)


def config_from_args(args, lambda1=0.02):
    return FitConfig(lambda1=lambda1, **{k: getattr(args, k) for k in asdict(FitConfig()) if k != "lambda1"})


def main():
    from golem_learning_report import render_report
    parser = argparse.ArgumentParser(description=__doc__)
    add_optimizer_arguments(parser)
    parser.add_argument("--sparsities", nargs="+", type=float, default=SPARSITIES)
    parser.add_argument("--thresholds", nargs="+", type=float, default=THRESHOLDS)
    args = parser.parse_args()
    if any(t < 0 or not __import__('math').isfinite(t) for t in args.thresholds):
        parser.error("thresholds must be finite and nonnegative")
    results = run_grid(args.version, config_from_args(args), args.sparsities, args.thresholds)
    pc, pc_note = load_pc(args.version)
    report, _ = paths(args.version)
    report.write_text(render_report(args.version, results, pc, pc_note), encoding="utf-8")
    print(f"Wrote {report}")


if __name__ == "__main__":
    main()
