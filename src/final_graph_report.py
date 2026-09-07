def render_report(version: str, classification: list, main_graph: dict,
                   annotated_main: list, pred_usefulness: dict,
                   stable_threshold: float, candidate_threshold: float, gap_threshold: float,
                   excluded_sources: set, suffix: str) -> str:
    lines = [f"# Final Team Deliverable -- Step 5 ({version})\n"]
    lines.append(
        "Classifies every predictor/exogenous edge seen in the Step 4 "
        "topic-level block bootstrap (`bootstrap_stability.py`, 500 "
        "replicates) into a tier, using both the continuous+Fisher-Z and "
        "discretized+chi-square representations rather than a single "
        "adjacency number. `excluded` overrides the numeric tiers "
        "regardless of rate -- see the 'Excluded from interpretation' "
        "section. Thresholds: stable >= {:.1f} mean rate (representation "
        "gap <= {:.1f}), candidate >= {:.1f} mean rate (same gap "
        "requirement), ambiguous = gap > {:.1f} regardless of mean, weak = "
        "everything else. Classified independently per dataset version -- "
        "v4 and v5 can and do disagree on some edges.\n".format(
            stable_threshold, gap_threshold, candidate_threshold, gap_threshold)
    )

    lines.append("## Main graph (frozen setting: continuous / Fisher-Z / alpha=0.05 / constrained)\n")
    lines.append(
        f"{main_graph['n_directed']} directed edges, {main_graph['n_undirected']} "
        "undirected, on n={} rows. Every edge below is annotated with its "
        "tier from the bootstrap classification (not just this single "
        "run).\n".format(main_graph["n_rows"])
    )
    lines.append("```")
    for e in annotated_main:
        rate_str = f"{e['mean_rate']:.3f}" if e["mean_rate"] is not None else "n/a"
        lines.append(f"{e['src']} -> {e['dst']}   [{e['tier']}, mean_rate={rate_str}]")
    lines.append("```\n")

    for tier, heading, note in [
        ("stable", "Stable-edge graph", "Cleared the stability bar in both representations."),
        ("candidate", "Candidate edges", "Moderate, consistent-direction signal -- tentative, not stable."),
        ("ambiguous", "Ambiguous edges", "Large swing between continuous and discretized representations -- "
                                          "likely a representation artifact (linear vs. binned CI test), not "
                                          "interpretable as a finding either way without further work."),
        ("excluded", "Excluded from interpretation", "Overridden regardless of numeric rate -- see reason per edge."),
    ]:
        lines.append(f"## {heading}\n")
        lines.append(f"{note}\n")
        rows = [r for r in classification if r["tier"] == tier]
        if not rows:
            lines.append("(none)\n")
            continue
        lines.append("```")
        header = f"{'from':<22} {'to':<20} {'continuous':<11} {'discretized':<12} {'mean':<7} {'gap':<6}"
        lines.append(header)
        for r in rows:
            lines.append(
                f"{r['from']:<22} {r['to']:<20} {r['continuous_rate']:<11} "
                f"{r['discretized_rate']:<12} {r['mean_rate']:<7} {r['gap']:<6}"
            )
        lines.append("```")
        if tier == "excluded":
            for r in rows:
                if r["from"] in excluded_sources:
                    lines.append(
                        f"- `{r['from']} -> {r['to']}`: size confound -- "
                        "pc_learning.py's sensitivity_size_control group shows this edge "
                        "disappears (replaced by `n_papers_t1_log -> modularity_t1`) once "
                        "topic size is available to condition on."
                    )
            lines.append(
                "- `bridge_concentration_t1` is near-degenerate (mass at 0/1) and was "
                "already excluded from the main model at Step 1 -- listed here for "
                "completeness, not because it appeared in the bootstrap.\n"
            )
        else:
            lines.append("")

    lines.append("## Cross-reference: predictive usefulness (Step 5 / D2.3)\n")
    for outcome, models in pred_usefulness.items():
        b, a, an, g = models["baseline"], models["all_t1"], models["all_t1_no_modularity"], models["graph_parents"]
        lines.append(
            f"- `{outcome}`: baseline R²={b['r2_mean']:.3f}, all_t1={a['r2_mean']:.3f}, "
            f"all_t1_no_modularity={an['r2_mean']:.3f}, graph_parents={g['r2_mean']:.3f} "
            "(see `predictive_usefulness{}.md` for full CV detail).".format(suffix)
        )
    lines.append(
        "\nNote: `sensitivity_outcome:topic_growth`/`:hit_rate_2yr` and "
        "`sensitivity_no_year` (in `pc_settings_comparison{}.md`) are single-run "
        "results, not bootstrap-replicated, so they are not tier-classified above "
        "-- treat them as context, not stability evidence.\n".format(suffix)
    )

    lines.append("## Interpretation\n")
    stable_pairs = [f"`{r['from']}->{r['to']}`" for r in classification if r["tier"] == "stable"]
    lines.append(
        f"The only edges stable across both bootstrap representations for {version} are: "
        f"{', '.join(stable_pairs) if stable_pairs else '(none)'}. These are dominated by "
        "mechanical persistence (`topic_share_t1->topic_share_t`) and calendar-time "
        "absorption (`year` into `connectivity_t1`/`log1p_median_c2`), not by a genuinely "
        "novel structural mechanism. `modularity_t1`'s edges, despite moderate raw "
        "adjacency rates, are excluded outright as a demonstrated size confound. "
        "`connectivity_t1->log1p_median_c2` is flagged ambiguous rather than reported "
        "either way, since its adjacency rate depends almost entirely on which CI test "
        "(linear vs. binned) is used. The most defensible candidate for a real, "
        "non-mechanical structural relationship is `cross_topic_rate_t1->log1p_median_c2`, "
        "which survives as stable or candidate depending on version without being "
        "refuted by any sensitivity check run so far -- still a candidate, not a proven "
        "causal claim, given PC's Markov/faithfulness/i.i.d. assumptions are not fully "
        "met by this panel.\n"
    )

    return "\n".join(lines)
