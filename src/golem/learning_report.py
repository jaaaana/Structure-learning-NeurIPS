import sys
from pathlib import Path as _Path
_SRC_ROOT = str(_Path(__file__).resolve().parents[1])
if _SRC_ROOT not in sys.path:
    sys.path.insert(0, _SRC_ROOT)
import argparse
import json

import pandas as pd

from constraints import TIER_0, TIER_1, TIER_1_LOG_VARIANT, _base_name
from data_prep import DATASETS
from golem.learning import edge_recurrence, panel_fingerprint, paths
from pc.learning import load_continuous, load_discretized



def table(rows):
    df = rows if isinstance(rows, pd.DataFrame) else pd.DataFrame(rows)
    if df.empty:
        return "No eligible results.\n"
    rendered = df.to_string(index=False, float_format=lambda x: f"{x:.4f}")
    return "```\n" + "\n".join(line.rstrip() for line in rendered.splitlines()) + "\n```\n"


def recurrence_text():
    return ("Pairs are ordered so the more frequent direction points from `a` to `b`; ties use alphabetical order. "
            "Rates use all eligible fits, "
            "including empty graphs. `a_to_b_rate`, `b_to_a_rate`, and `undirected_rate` "
            "sum to `adjacency_rate`; conditional rates divide by adjacent fits only. "
            "The directional conditional rates use all adjacent fits as the denominator, including undirected fits. "
            "In constrained runs, a zero reverse-direction rate can follow directly from the tier mask forbidding "
            "backward arrows; it is not independent evidence for that direction. Orientation frequency and "
            "consistency of a particular direction are distinct.\n")


def render_report(version, results):
    fits = {(r["group"], r["representation"], r["constrained"], r["config"]["lambda1"]): r
            for r in results}
    counts = {status: sum(r["status"] == status for r in fits.values())
              for status in ("converged", "nonconverged", "failed")}
    lines = [f"# GOLEM Settings Comparison ({version})\n",
             f"**{len(results)} graph settings from {len(fits)} fitted models:** "
             f"{counts['converged']} converged, {counts['nonconverged']} reached the iteration limit, "
             f"{counts['failed']} failed numerically.\n",
             "## Settings grid\n",
             "Sensitivity outcomes and no-year runs freeze sparsity=0.02 and threshold=0.10. "
             "Size-control uses the continuous grid. `sensitivity_relaxed_tiers` is one continuous fit "
             "with temporal and exogenous-year restrictions retained, but predictor-predictor and "
             "outcome-outcome edges allowed.\n"]
    if results:
        cfg = results[0]["config"]
        lines.append(f"Optimizer: lambda_dag={cfg['lambda_dag']}, learning_rate={cfg['learning_rate']}, "
                     f"tolerance={cfg['tolerance']}, max_iter={cfg['max_iter']}.\n")
    settings = []
    for i, r in enumerate(results):
        settings.append({"id": i, "group": r["group"], "representation": r["representation"],
                         "constrained": r["constrained"], "lambda1": r["config"]["lambda1"],
                         "threshold": r["threshold"], "status": r["status"],
                         "iterations": r["iterations"], "directed": r.get("n_directed"),
                         "undirected": r.get("n_undirected"),
                         "violations_before": r.get("n_temporal_violations_before"),
                         "violations_after": r.get("n_temporal_violations")})
    lines.append(table(settings))
    lines += ["## Edge detail per setting\n"]
    for i, r in enumerate(results):
        lines.append(f"### Setting {i}: {r['group']} / {r['representation']} / "
                     f"lambda1={r['config']['lambda1']} / threshold={r['threshold']} / "
                     f"constrained={r['constrained']}\n")
        lines.append(f"Status: **{r['status']}**. Rows: {r['n_rows']}. Iterations: {r['iterations']}.\n")
        if r["status"] == "failed":
            lines.append(f"Failure: {r['failure_reason']}\n")
            continue
        if r["status"] != "converged":
            lines.append("Exploratory graph only; excluded from recurrence and comparisons.\n")
        lookup = {n: k for k, n in enumerate(r["node_names"])}
        edges = []
        for kind in ("directed", "undirected"):
            for a, b in r[f"{kind}_edges"]:
                edges.append({"a": a, "edge": "->" if kind == "directed" else "--", "b": b,
                              "strength_a_to_b": r["strengths"][lookup[a]][lookup[b]],
                              "strength_b_to_a": r["strengths"][lookup[b]][lookup[a]],
                              "flag": "possible size confound" if "modularity_t1" in (_base_name(a), _base_name(b)) else ""})
        lines.append(table(edges) if edges else "No edges exceed this threshold.\n")
    lines += ["## Adjacency vs. orientation stability across constrained main-model settings\n",
              "Across the converged constrained main-model fits, `adjacency_rate` counts any edge between a pair; "
              "the direction rates show how those adjacent fits orient it. For pairs spanning different temporal "
              "tiers, the temporal constraint fixes direction, so orientation is constraint-imposed rather than "
              "independently learned. `same_direction_rate` measures consistency among directed fits.\n",
              recurrence_text(),
              "Thresholds from the same fitted model are correlated settings, not independent replications.\n"]
    for representation in ("continuous", "discretized", "combined"):
        selected = [r for r in results if r["group"] == "main" and r["constrained"] and r["status"] == "converged"
                    and (representation == "combined" or r["representation"] == representation)]
        lines += [f"### {representation}: {len(selected)} eligible settings\n", table(edge_recurrence(selected))]
    relaxed = [r for r in results if r["group"] == "sensitivity_relaxed_tiers"
               and r["status"] == "converged"]
    same_tier_edges = []
    tier_sets = [set(TIER_0), set(TIER_1) | {TIER_1_LOG_VARIANT}]
    for r in relaxed:
        lookup = {n: k for k, n in enumerate(r["node_names"])}
        for kind in ("directed", "undirected"):
            for a, b in r[f"{kind}_edges"]:
                ba, bb = _base_name(a), _base_name(b)
                if not any(ba in tier and bb in tier for tier in tier_sets):
                    continue
                same_tier_edges.append({
                    "representation": r["representation"], "lambda1": r["config"]["lambda1"],
                    "threshold": r["threshold"], "a": a,
                    "edge": "->" if kind == "directed" else "--", "b": b,
                    "strength_a_to_b": r["strengths"][lookup[a]][lookup[b]],
                    "strength_b_to_a": r["strengths"][lookup[b]][lookup[a]],
                })
    lines += ["## Relaxed-tier sensitivity\n",
              "Exploratory same-tier edges; not bootstrap-stability classified.\n",
              table(same_tier_edges) if same_tier_edges else "No eligible same-tier edges in converged fits.\n"]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Render the GOLEM settings report from saved fits.")
    parser.add_argument("--version", choices=list(DATASETS), default="v5")
    args = parser.parse_args()
    report, source = paths(args.version)
    if not source.exists():
        parser.error(f"no saved GOLEM settings results at {source}")
    results = json.loads(source.read_text(encoding="utf-8"))
    panels = {"continuous": load_continuous(args.version),
              "discretized": load_discretized(args.version)}
    fingerprints = {name: panel_fingerprint(df) for name, df in panels.items()}
    if any(r.get("input_fingerprint") != fingerprints.get(r["representation"])
           for r in results):
        parser.error("saved GOLEM fits use different inputs; rerun src/golem/learning.py")
    if not any(r["group"] == "sensitivity_relaxed_tiers" for r in results):
        parser.error("saved GOLEM fits lack the relaxed-tier sensitivity; rerun src/golem/learning.py")
    report.write_text(render_report(args.version, results), encoding="utf-8")
    print(f"Wrote {report}")


if __name__ == "__main__":
    main()
