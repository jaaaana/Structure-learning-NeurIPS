import argparse
import json
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
from causallearn.graph.GraphNode import GraphNode
from causallearn.search.ConstraintBased.PC import pc

from constraints import (
    EXOGENOUS,
    MAIN_PREDICTORS,
    MAIN_OUTCOMES,
    SENSITIVITY_OUTCOMES_ONLY,
    SIZE_VARS,
    TIER_0,
    TIER_1,
    TIER_1_LOG_VARIANT,
    _base_name,
    build_background_knowledge,
)
from data_prep import DATASETS
from pc_learning_report import render_report

ROOT = Path(__file__).resolve().parent.parent

ALPHAS = [0.01, 0.05, 0.10]

CONNECTIVITY_LOG_VARIANT = "connectivity_t1_log"
_MAIN_PREDICTORS_LOGGED = [CONNECTIVITY_LOG_VARIANT if p == "connectivity_t1" else p for p in MAIN_PREDICTORS]
CONTINUOUS_PREDICTORS = _MAIN_PREDICTORS_LOGGED + EXOGENOUS
CONTINUOUS_OUTCOMES = MAIN_OUTCOMES

SIZE_LOG_VARIANT = "n_papers_t1_log"
SIZE_CONTROL_PREDICTORS = CONTINUOUS_PREDICTORS + [SIZE_LOG_VARIANT]

DISCRETIZED_PREDICTORS = [f"{v}_bin" for v in MAIN_PREDICTORS] + [f"{v}_bin" for v in EXOGENOUS]
DISCRETIZED_OUTCOMES = [f"{v}_bin" for v in MAIN_OUTCOMES]

SENSITIVITY_OUTCOME_ALPHA = 0.05


def _reports_dir(version: str) -> Path:
    d = ROOT / "reports" / "pc_runs"
    d.mkdir(parents=True, exist_ok=True)
    return d


def _report_out(version: str) -> Path:
    suffix = "" if version == "v4" else f"_{version}"
    return ROOT / "reports" / f"pc_settings_comparison{suffix}.md"


def load_continuous(version: str) -> pd.DataFrame:
    df = pd.read_csv(DATASETS[version]["continuous_out"])
    df[CONNECTIVITY_LOG_VARIANT] = np.log(df["connectivity_t1"])
    df[SIZE_LOG_VARIANT] = np.log(df["n_papers_t1"])
    return df


def load_discretized(version: str) -> pd.DataFrame:
    df = pd.read_csv(DATASETS[version]["discretized_out"])
    bin_cols = [c for c in df.columns if c.endswith("_bin")]
    for c in bin_cols:
        df[c] = df[c].astype("category").cat.codes
    return df


def classify_edges(G, node_names: list) -> dict:
    directed = []
    undirected = []
    other = []
    for edge in G.get_graph_edges():
        a, b = edge.get_node1().get_name(), edge.get_node2().get_name()
        ep1, ep2 = str(edge.get_endpoint1()), str(edge.get_endpoint2())
        if ep1 == "TAIL" and ep2 == "ARROW":
            directed.append((a, b))
        elif ep1 == "ARROW" and ep2 == "TAIL":
            directed.append((b, a))
        elif ep1 == "TAIL" and ep2 == "TAIL":
            undirected.append(tuple(sorted((a, b))))
        else:
            other.append((a, b, ep1, ep2))
    return {"directed": directed, "undirected": undirected, "other": other}


def count_temporal_violations(directed_edges: list) -> int:
    t1_or_earlier = TIER_0 + SIZE_VARS
    n = 0
    for src, dst in directed_edges:
        is_outcome_src = _base_name(src) in TIER_1 or _base_name(src) == TIER_1_LOG_VARIANT
        if is_outcome_src and _base_name(dst) in t1_or_earlier:
            n += 1
        elif _base_name(dst) in EXOGENOUS and (_base_name(src) in t1_or_earlier or is_outcome_src):
            n += 1
    return n


def run_one_setting(df: pd.DataFrame, node_names: list, indep_test: str, alpha: float,
                     constrained: bool, size_vars: list = None) -> dict:
    data = df[node_names].to_numpy(dtype=float)
    bk = build_background_knowledge(node_names, size_vars=size_vars) if constrained else None

    cg = pc(data, alpha=alpha, indep_test=indep_test, node_names=node_names,
            background_knowledge=bk, show_progress=False)

    edges = classify_edges(cg.G, node_names)
    n_violations = count_temporal_violations(edges["directed"]) if not constrained else 0

    return {
        "indep_test": indep_test,
        "alpha": alpha,
        "constrained": constrained,
        "n_rows": len(df),
        "n_directed": len(edges["directed"]),
        "n_undirected": len(edges["undirected"]),
        "n_other": len(edges["other"]),
        "n_temporal_violations": n_violations,
        "directed_edges": edges["directed"],
        "undirected_edges": edges["undirected"],
        "other_edges": edges["other"],
    }


def run_grid(version: str) -> list:
    cont_df = load_continuous(version)
    disc_df = load_discretized(version)

    results = []

    for alpha, constrained in product(ALPHAS, [True, False]):
        node_names = CONTINUOUS_PREDICTORS + CONTINUOUS_OUTCOMES
        res = run_one_setting(cont_df, node_names, "fisherz", alpha, constrained)
        res["representation"] = "continuous"
        res["group"] = "main"
        results.append(res)

    for alpha, constrained in product(ALPHAS, [True, False]):
        node_names = DISCRETIZED_PREDICTORS + DISCRETIZED_OUTCOMES
        res = run_one_setting(disc_df, node_names, "chisq", alpha, constrained)
        res["representation"] = "discretized"
        res["group"] = "main"
        results.append(res)

    for alpha, constrained in product(ALPHAS, [True, False]):
        node_names = CONTINUOUS_PREDICTORS + CONTINUOUS_OUTCOMES
        res = run_one_setting(cont_df, node_names, "kci", alpha, constrained)
        res["representation"] = "continuous"
        res["group"] = "main"
        results.append(res)

    for outcome in SENSITIVITY_OUTCOMES_ONLY:
        for constrained in [True, False]:
            node_names = CONTINUOUS_PREDICTORS + [outcome]
            res = run_one_setting(cont_df, node_names, "fisherz", SENSITIVITY_OUTCOME_ALPHA, constrained)
            res["representation"] = "continuous"
            res["group"] = f"sensitivity_outcome:{outcome}"
            results.append(res)

            node_names_disc = DISCRETIZED_PREDICTORS + [f"{outcome}_bin"]
            res = run_one_setting(disc_df, node_names_disc, "chisq", SENSITIVITY_OUTCOME_ALPHA, constrained)
            res["representation"] = "discretized"
            res["group"] = f"sensitivity_outcome:{outcome}"
            results.append(res)

    cont_no_year = [n for n in CONTINUOUS_PREDICTORS if n not in EXOGENOUS]
    disc_no_year = [n for n in DISCRETIZED_PREDICTORS if _base_name(n) not in EXOGENOUS]
    for constrained in [True, False]:
        node_names = cont_no_year + CONTINUOUS_OUTCOMES
        res = run_one_setting(cont_df, node_names, "fisherz", SENSITIVITY_OUTCOME_ALPHA, constrained)
        res["representation"] = "continuous"
        res["group"] = "sensitivity_no_year"
        results.append(res)

        node_names_disc = disc_no_year + DISCRETIZED_OUTCOMES
        res = run_one_setting(disc_df, node_names_disc, "chisq", SENSITIVITY_OUTCOME_ALPHA, constrained)
        res["representation"] = "discretized"
        res["group"] = "sensitivity_no_year"
        results.append(res)

    for alpha, constrained in product(ALPHAS, [True, False]):
        node_names = SIZE_CONTROL_PREDICTORS + CONTINUOUS_OUTCOMES
        res = run_one_setting(cont_df, node_names, "fisherz", alpha, constrained,
                               size_vars=SIZE_VARS)
        res["representation"] = "continuous"
        res["group"] = "sensitivity_size_control"
        results.append(res)

    return results


def _tier_rank(name: str) -> float:
    b = _base_name(name)
    if b in EXOGENOUS:
        return 0
    if b in SIZE_VARS:
        return 0.5
    if b in TIER_0:
        return 1
    return 2


def edge_recurrence(results: list) -> pd.DataFrame:
    n_settings = len(results)

    adjacency_counts = {}
    directed_counts = {}
    for r in results:
        seen_this_run = set()
        for src, dst in r["directed_edges"]:
            a, b = _base_name(src), _base_name(dst)
            pair = (a, b) if _tier_rank(a) <= _tier_rank(b) else (b, a)
            directed_counts[pair] = directed_counts.get(pair, 0) + 1
            if pair not in seen_this_run:
                adjacency_counts[pair] = adjacency_counts.get(pair, 0) + 1
                seen_this_run.add(pair)
        for x, y in r["undirected_edges"]:
            a, b = _base_name(x), _base_name(y)
            pair = (a, b) if _tier_rank(a) <= _tier_rank(b) else (b, a)
            if pair not in seen_this_run:
                adjacency_counts[pair] = adjacency_counts.get(pair, 0) + 1
                seen_this_run.add(pair)

    cols = ["from", "to", "n_settings_adjacent", "n_settings_total", "adjacency_rate",
            "n_settings_oriented", "orientation_rate_given_adjacent"]
    if not adjacency_counts:
        return pd.DataFrame(columns=cols)

    rows = []
    for pair, n_adj in adjacency_counts.items():
        n_dir = directed_counts.get(pair, 0)
        rows.append({
            "from": pair[0], "to": pair[1],
            "n_settings_adjacent": n_adj, "n_settings_total": n_settings,
            "adjacency_rate": round(n_adj / n_settings, 3),
            "n_settings_oriented": n_dir,
            "orientation_rate_given_adjacent": round(n_dir / n_adj, 3),
        })
    return pd.DataFrame(rows).sort_values("adjacency_rate", ascending=False)[cols]


def main(version: str = "v4"):
    results = run_grid(version)
    main_constrained = [r for r in results if r["constrained"] and r.get("group") == "main"]
    recurrence = edge_recurrence(main_constrained)

    report = render_report(version, results, recurrence, CONTINUOUS_PREDICTORS,
                            DISCRETIZED_PREDICTORS, CONTINUOUS_OUTCOMES, DISCRETIZED_OUTCOMES)
    out_path = _report_out(version)
    out_path.write_text(report, encoding="utf-8")

    runs_dir = _reports_dir(version)
    suffix = "" if version == "v4" else f"_{version}"
    json_path = runs_dir / f"pc_runs{suffix}.json"
    json_path.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")

    print(f"[{version}] Ran {len(results)} PC settings.")
    print(f"Wrote {out_path}")
    print(f"Wrote {json_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=list(DATASETS.keys()), default="v4")
    args = parser.parse_args()
    main(args.version)
