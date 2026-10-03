def render_report(version: str, classification: list, main_graph: dict,
                   annotated_main: list, pred_usefulness: dict,
                   stable_threshold: float, candidate_threshold: float, gap_threshold: float,
                   size_confound_sources: set, suffix: str) -> str:
    lines = [f"# Final Team Deliverable -- Step 5 ({version})\n"]
    lines.append(
        "Classifies every predictor/exogenous edge seen in the Step 4 "
        "topic-level block bootstrap (`bootstrap_stability.py`, 500 "
        "replicates) into a tier, using both the continuous+Fisher-Z and "
        "discretized+chi-square representations rather than a single "
        "adjacency number. `excluded` overrides the numeric tiers "
        "regardless of rate, but only for variables entirely absent from "
        "the model-ready data (see 'Excluded from interpretation'). "
        "`modularity_t1` edges are a different case: they get their real "
        "tier from the numbers like everything else, but are additionally "
        "flagged `[SIZE CONFOUND]` wherever they appear, since "
        "`pc_learning.py`'s `sensitivity_size_control` group shows every "
        "`modularity_t1 -> outcome` edge disappears once topic size is "
        "controllable -- a reason to be skeptical of the edge's "
        "interpretation, not a reason to hide its actual numbers. "
        "Thresholds: stable >= {:.1f} mean rate (representation "
        "gap <= {:.1f}), candidate >= {:.1f} mean rate (same gap "
        "requirement), ambiguous = gap > {:.1f} regardless of mean, weak = "
        "everything else. Classified independently per dataset version -- "
        "v4 and v5 can and do disagree on some edges.\n".format(
            stable_threshold, gap_threshold, candidate_threshold, gap_threshold)
    )
    lines.append(
        "These tiers are computed from **adjacency rate alone** -- whether "
        "an edge appears at all, in either bootstrap representation -- never "
        "from orientation rate. Under this pipeline's temporal-tier "
        "background knowledge, every edge that can appear at all is between "
        "two different tiers, and `causal-learn` mechanically forces its "
        "direction immediately after skeleton discovery, before any "
        "independent PC orientation logic runs; see "
        "`bootstrap_stability.md`'s orientation-stability caveat and "
        "'Orientation provenance' section for the full derivation.\n"
    )
    lines.append(
        "**`stable`/`candidate`/`ambiguous`/`weak` are descriptive labels for "
        "a bootstrap-adjacency-frequency bucket, nothing more** -- they are "
        "not p-values, confidence intervals, or any other statistical "
        "significance test, and clearing the `stable` bar is not a "
        "correctness or causal-truth claim. They also describe **adjacency "
        "only**: whether the edge recurs across replicates, never which "
        "direction it points (see the paragraph above and the `[T]`/"
        "`unconstrained_same_direction` annotations for that, a fully "
        "separate question).\n"
    )

    lines.append("## Main graph (frozen setting: continuous / Fisher-Z / alpha=0.05 / constrained)\n")
    lines.append(
        f"{main_graph['n_directed']} directed edges, {main_graph['n_undirected']} "
        "undirected, on n={} rows. Every edge below is annotated with its "
        "tier from the bootstrap classification (not just this single "
        "run).\n".format(main_graph["n_rows"])
    )
    lines.append(
        "Every edge's *direction* here is `[T]` -- forced by the temporal "
        "background knowledge, not discovered by PC on its own. Under this "
        "model's tier structure, every edge that can exist at all is between "
        "two different tiers, and `causal-learn` mechanically orients any "
        "such edge immediately after skeleton discovery, before its own "
        "v-structure or Meek orientation logic ever runs -- there is no edge "
        "in this graph that could have been genuinely `[PC]`-oriented under "
        "these constraints (see `bootstrap_stability.md`'s 'Orientation "
        "provenance' section for the full derivation). "
        "`unconstrained_same_direction` below is the one independent check "
        "available: the share of an unconstrained bootstrap's adjacent "
        "replicates (same resampled data, no background knowledge at all) "
        "where PC's own orientation logic landed on this same direction "
        "anyway -- high means the data corroborates the assumption, low "
        "means the direction rests on the temporal assumption alone.\n"
    )
    lines.append("```")
    for e in annotated_main:
        rate_str = f"{e['mean_rate']:.3f}" if e["mean_rate"] is not None else "n/a"
        sdr = e.get("same_direction_rate")
        sdr_str = f"{sdr:.3f}" if sdr is not None else "n/a"
        confound_flag = "  [SIZE CONFOUND]" if e.get("size_confound_flag") else ""
        lines.append(
            f"{e['src']} -> {e['dst']}   [T, unconstrained_same_direction={sdr_str}]   "
            f"[{e['tier']}, mean_rate={rate_str}]{confound_flag}"
        )
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
        header = (f"{'from':<22} {'to':<20} {'continuous':<11} {'discretized':<12} {'mean':<7} {'gap':<6} "
                   "flag")
        lines.append(header)
        for r in rows:
            flag = "SIZE_CONFOUND" if r.get("size_confound_flag") else ""
            lines.append(
                f"{r['from']:<22} {r['to']:<20} {r['continuous_rate']:<11} "
                f"{r['discretized_rate']:<12} {r['mean_rate']:<7} {r['gap']:<6} {flag}"
            )
        lines.append("```")
        confound_rows = [r for r in rows if r.get("size_confound_flag")]
        for r in confound_rows:
            lines.append(
                f"- `{r['from']} -> {r['to']}`: flagged size confound -- "
                "pc_learning.py's sensitivity_size_control group shows this edge "
                "disappears (replaced by `n_papers_t1_log -> modularity_t1`) once "
                "topic size is available to condition on. Its tier above is from the "
                "real adjacency rate; this flag is a reason to be skeptical of its "
                "interpretation, not a reason to disbelieve the rate itself."
            )
        if tier == "excluded":
            lines.append(
                "- `bridge_concentration_t1` is near-degenerate (mass at 0/1) and has "
                "a known issue in its underlying betweenness computation -- excluded "
                "from the main model and every sensitivity setting at Step 1, not "
                "produced in either model-ready table, left as future work; listed "
                "here for completeness, not because it appeared in the bootstrap.\n"
            )
        elif not confound_rows:
            lines.append("")

    lines.append("## Cross-reference: predictive usefulness (Step 5 / D2.3)\n")
    lines.append(
        "`graph_parents_nested_cv` below selects its additional predictors "
        "separately inside each cross-validation fold, using only that "
        "fold's training topics, specifically to avoid the held-out fold's "
        "topics leaking into predictor selection (see "
        "`predictive_usefulness{}.md` for the full nested-CV detail). It is "
        "a different statistic from the stable/candidate tiers above (which "
        "use the full-dataset, both-representations bootstrap) -- not the "
        "same number restated under a new name.\n".format(suffix)
    )
    for outcome, models in pred_usefulness.items():
        b, a, an, g = models["baseline"], models["all_t1"], models["all_t1_no_modularity"], models["graph_parents_nested_cv"]
        lines.append(
            f"- `{outcome}`: baseline R²={b['r2_mean']:.3f}, all_t1={a['r2_mean']:.3f}, "
            f"all_t1_no_modularity={an['r2_mean']:.3f}, graph_parents_nested_cv={g['r2_mean']:.3f} "
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
        "novel structural mechanism. `modularity_t1`'s edges get their tier from their "
        "real adjacency rate like any other edge (typically `candidate` or `weak` here, "
        "never `stable`), but are flagged `[SIZE CONFOUND]`/`SIZE_CONFOUND` wherever "
        "they appear: `pc_learning.py`'s `sensitivity_size_control` group shows every "
        "`modularity_t1 -> outcome` edge disappears, replaced by `n_papers_t1_log -> "
        "modularity_t1`, once topic size is controllable -- read any `modularity_t1` "
        "edge below as a demonstrated size confound regardless of its numeric tier. "
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
