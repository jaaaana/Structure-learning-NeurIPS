from constraints import _base_name
from golem_learning import compare_graphs, edge_recurrence, model_nodes
from golem_learning_report import recurrence_text, table


def render_report(version, payload, pc=None, pc_note="PC artifact unavailable"):
    meta = payload["metadata"]
    lines = [f"# GOLEM Bootstrap Stability ({version})\n",
             f"Topic-block bootstrap: seed={meta['seed']}, requested B={meta['n_boot']} per representation. "
             "Topics are sampled with replacement; all years and duplicate draws are retained. "
             "Sampling matches PC; settings are fixed, with temporal constraints enabled.\n",
             f"Fit configuration: `{meta['config']}`. Threshold: {meta['threshold']}.\n",
             recurrence_text()]
    for representation in ("continuous", "discretized"):
        records = payload[representation]
        successful = [r for r in records if r["status"] == "converged"]
        lines += [f"## {representation}\n", table([payload[f"{representation}_diagnostics"]]),
                  "Only converged replicates enter the denominator, including converged empty graphs. "
                  "Nonconvergence is not evidence for an absent edge. Frequencies describe the converged "
                  "subset; substantial attrition can bias stability estimates. No stable/unstable cutoff is imposed.\n",
                  table(edge_recurrence(successful))]
        problem_rows = [{"replicate": r["replicate"], "status": r["status"],
                         "reason": r.get("failure_reason") or "Iteration limit reached"}
                        for r in records if r["status"] != "converged"]
        if problem_rows:
            lines += ["### Skipped, failed, and nonconverged replicates\n", table(problem_rows)]
        lines += ["### Cycle conversion and temporal diagnostics\n",
                  table([{"replicate": r["replicate"], "cyclic_components": len(r.get("cyclic_components", [])),
                          "converted_orientations": len(r.get("converted_orientations", [])),
                          "violations_before": r.get("n_temporal_violations_before"),
                          "violations_after": r.get("n_temporal_violations")}
                         for r in successful if r.get("converted_orientations") or r.get("n_temporal_violations_before")])]
        lines += ["### Comparison with PC bootstrap\n", pc_note + "\n"]
        if pc is None or representation not in pc:
            lines.append("PC bootstrap comparison unavailable.\n")
            continue
        expected_nodes = {_base_name(n) for n in model_nodes(representation)}
        pc_runs = [r for r in pc[representation]
                   if r.get("constrained", True) and r.get("group", "main") == "main"
                   and {_base_name(n) for n in r.get("node_names", model_nodes(representation))} == expected_nodes]
        gf = edge_recurrence(successful)
        pf = edge_recurrence(pc_runs)
        if not gf.empty or not pf.empty:
            joined = gf.merge(pf, on=["a", "b"], how="outer", suffixes=("_golem", "_pc"))
            # An unobserved edge has rate zero only when that method has eligible fits.
            for suffix_, runs in (("golem", successful), ("pc", pc_runs)):
                if runs:
                    cols = [c for c in joined if c.endswith("_" + suffix_)]
                    joined[cols] = joined[cols].fillna(0)
                    joined[f"n_total_{suffix_}"] = len(runs)
            columns = ["a", "b", "adjacency_rate_golem", "adjacency_rate_pc",
                       "a_to_b_rate_golem", "a_to_b_rate_pc", "b_to_a_rate_golem", "b_to_a_rate_pc",
                       "undirected_rate_golem", "undirected_rate_pc"]
            lines.append(table(joined[columns]))
        if pc.get("seed") != meta["seed"] or pc.get("n_boot") != meta["n_boot"]:
            lines.append("Paired replicate comparisons unavailable: PC seed or requested replicate count differs.\n")
            continue
        pc_by_id = {r["replicate"]: r for r in pc_runs}
        paired = []
        for g in successful:
            p = pc_by_id.get(g["replicate"])
            if p is not None and p["n_rows"] == g["n_rows"]:
                paired.append({"replicate": g["replicate"], **compare_graphs(g, p)})
        lines += ["Paired comparisons include only replicates successful in both methods with matching "
                  "row counts. Historical PC files lack input hashes; identical historical inputs cannot "
                  "be verified independently.\n", table(paired)]
    return "\n".join(lines)
