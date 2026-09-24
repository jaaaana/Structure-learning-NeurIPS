import pandas as pd

from constraints import _base_name
from golem_learning import comparison_rows, edge_recurrence



def table(rows):
    df = rows if isinstance(rows, pd.DataFrame) else pd.DataFrame(rows)
    return "No eligible results.\n" if df.empty else "```\n" + df.to_string(index=False, float_format=lambda x: f"{x:.4f}") + "\n```\n"


def recurrence_text():
    return ("Pairs use alphabetical base-variable order. Rates use all eligible fits, "
            "including empty graphs. `a_to_b_rate`, `b_to_a_rate`, and `undirected_rate` "
            "sum to `adjacency_rate`; conditional rates divide by adjacent fits only. "
            "Orientation frequency and consistency of a particular direction are distinct.\n")


def render_report(version, results, pc_results=None, pc_note="PC artifact unavailable"):
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
             "Size-control uses the continuous grid. No hyperparameter is selected by agreement with PC.\n"]
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
        lines.append(f"Optimizer: `{r['config']}`. Objective components: `{r['objective']}`.\n")
        lines.append("Nodes (including isolates): " + ", ".join(f"`{n}`" for n in r["node_names"]) + ".\n")
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
        lines.append(f"Cyclic components: `{r['cyclic_components']}`. "
                     f"Converted orientations: `{r['converted_orientations']}`.\n")
    lines += ["## Constrained main-model recurrence\n", recurrence_text(),
              "Thresholds from the same fitted model are correlated settings, not independent replications.\n"]
    for representation in ("continuous", "discretized", "combined"):
        selected = [r for r in results if r["group"] == "main" and r["constrained"] and r["status"] == "converged"
                    and (representation == "combined" or r["representation"] == representation)]
        lines += [f"### {representation}: {len(selected)} eligible settings\n", table(edge_recurrence(selected))]
    lines += ["## Comparison with PC\n", pc_note + "\n",
              "Match representation, model group, constraint mode, row count, and normalized node set. "
              "Legacy PC files omit input hashes and node lists; nodes are reconstructed from their "
              "group, so exact historical input identity cannot be independently verified. "
              "Other PC endpoint types count toward adjacency only. Two empty skeletons have Jaccard=1.\n",
              table(comparison_rows(results, pc_results))]
    return "\n".join(lines)
