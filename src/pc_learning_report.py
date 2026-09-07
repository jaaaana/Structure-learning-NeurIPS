from constraints import TIER_0, TIER_1, TIER_1_LOG_VARIANT, _base_name


def render_report(version: str, results: list, recurrence, continuous_predictors: list,
                   discretized_predictors: list, continuous_outcomes: list,
                   discretized_outcomes: list) -> str:
    lines = []
    lines.append(f"# PC Algorithm Settings Comparison -- Step 3 ({version})\n")
    lines.append(
        "PC run across a controlled grid, per the 2026-08-19 "
        "correction. **Main model**: predictors "
        f"{', '.join(continuous_predictors)} (continuous) / "
        f"{', '.join(discretized_predictors)} (discretized), outcomes "
        f"{', '.join(continuous_outcomes)} (continuous) / "
        f"{', '.join(discretized_outcomes)} (discretized) -- continuous data "
        "+ Fisher-Z, discretized data + chi-square, continuous data + KCI "
        "(kernel-based, nonlinear-robust), alpha in {0.01, 0.05, 0.10}, with "
        "and without the Step 2/3 temporal + exogenous-year constraints. "
        "`bridge_concentration_t1` is dropped from the main model entirely "
        "(near-degenerate, Step 1 finding). **Sensitivity groups** (alpha=0.05 "
        "only): `sensitivity_outcome:<name>` swaps in `topic_growth` or "
        "`hit_rate_2yr` as the outcome instead of the main "
        f"`{continuous_outcomes}`; `sensitivity_no_year` reruns the main "
        "predictor/outcome set with the `year` node removed, to check "
        "whether year is actually absorbing any of the signal; "
        "`sensitivity_size_control` adds `n_papers_t1` (log-transformed, own "
        "tier below the regular predictors so it isn't blocked from "
        "`modularity_t1`'s conditioning set by forbid_within_tier) to check "
        "whether `modularity_t1`'s known size confound "
        "(r=0.48-0.51 with n_papers_t1 across v4/v5, stronger than the "
        "topic_share_t1 proxy) is driving any of its edges -- compare its "
        "edge list below against the main constrained run's.\n"
    )

    lines.append("## Settings grid\n")
    lines.append("```")
    header = (f"{'group':<26} {'repr':<12} {'test':<9} {'alpha':<6} {'constr':<7} "
              f"{'directed':<9} {'undirected':<11} {'temporal_violations':<20}")
    lines.append(header)
    for r in results:
        lines.append(
            f"{r.get('group', 'main'):<26} {r['representation']:<12} {r['indep_test']:<9} {r['alpha']:<6} "
            f"{str(r['constrained']):<7} {r['n_directed']:<9} {r['n_undirected']:<11} "
            f"{r['n_temporal_violations']:<20}"
        )
    lines.append("```\n")

    lines.append("## Edge detail per setting\n")
    for r in results:
        tag = "constrained" if r["constrained"] else "unconstrained"
        lines.append(f"### [{r.get('group', 'main')}] {r['representation']} / {r['indep_test']} / alpha={r['alpha']} / {tag}\n")
        if r["directed_edges"]:
            lines.append("Directed:")
            for src, dst in r["directed_edges"]:
                flag = ""
                if not r["constrained"] and (_base_name(src) in TIER_1 or _base_name(src) == TIER_1_LOG_VARIANT) \
                        and _base_name(dst) in TIER_0:
                    flag = "  [TEMPORAL VIOLATION]"
                lines.append(f"- `{src}` -> `{dst}`{flag}")
        if r["undirected_edges"]:
            lines.append("Undirected / ambiguous:")
            for a, b in r["undirected_edges"]:
                lines.append(f"- `{a}` -- `{b}`")
        if not r["directed_edges"] and not r["undirected_edges"]:
            lines.append("No edges found at this setting.")
        lines.append("")

    lines.append("## Adjacency vs. orientation stability across constrained main-model settings\n")
    n_main_constrained = len([r for r in results if r["constrained"] and r.get("group") == "main"])
    lines.append(
        f"Across the {n_main_constrained} constrained **main-model** settings "
        "in this grid (continuous+Fisher-Z, discretized+chi-square, "
        "continuous+KCI, alpha in {0.01, 0.05, 0.10}): `adjacency_rate` is "
        "how often PC places *any* edge (directed or undirected) between the "
        "two variables; `orientation_rate_given_adjacent` is, of those "
        "adjacent settings, how often PC actually commits to a direction "
        "rather than leaving it undirected/ambiguous in the CPDAG. Kept as "
        "two separate numbers per the 2026-08-19 correction -- "
        "a stable adjacency with unstable orientation is a materially "
        "different finding from a fully stable directed edge. Sensitivity "
        "settings (different outcome/predictor sets) are excluded from this "
        "table. This is a cheap first look, not the Step 4 bootstrap "
        "stability analysis -- it only varies representation/test/alpha, not "
        "the sample itself.\n"
    )
    if len(recurrence):
        lines.append("```")
        lines.append(recurrence.to_string(index=False))
        lines.append("```\n")
    else:
        lines.append("No edges recurred across any constrained main-model setting.\n")

    return "\n".join(lines)
