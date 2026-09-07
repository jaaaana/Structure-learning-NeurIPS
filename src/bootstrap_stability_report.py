def render_report(version: str, seed: int, n_boot: int, boot_alpha: float,
                   cont_diag: dict, cont_freq, disc_diag: dict, disc_freq) -> str:
    suffix = "" if version == "v4" else f"_{version}"
    lines = []
    lines.append(f"# Bootstrap Stability Analysis -- Step 4 ({version})\n")
    lines.append(
        f"Topic-level block bootstrap (seed={seed}, requested B={n_boot}) at the "
        f"frozen main-model setting (alpha={boot_alpha}, constrained, temporal + "
        "exogenous-year background knowledge applied). Each replicate resamples "
        "topics (not rows) with replacement and keeps every row of each sampled "
        "topic, per the 2026-08-19 correction: rows are repeated "
        "topic-year measurements, so plain row-level bootstrap would treat a "
        "topic's own yearly observations as independent draws. This is a "
        f"separate sensitivity axis from `pc_settings_comparison{suffix}.md`'s "
        "alpha/representation grid -- that grid holds the sample fixed and "
        "varies settings; this analysis holds settings fixed and varies the "
        "sample.\n"
    )

    for label, diag, freq in [
        ("continuous / Fisher-Z", cont_diag, cont_freq),
        ("discretized / chi-square", disc_diag, disc_freq),
    ]:
        lines.append(f"## {label}\n")
        lines.append(
            f"- Requested: {diag['n_boot_requested']} replicates. "
            f"Succeeded: {diag['n_succeeded']}. "
            f"Skipped (degenerate resample, a node had fewer than 2 distinct "
            f"values): {diag['n_degenerate_skipped']}. "
            f"Failed (PC raised an exception): {diag['n_failed']}."
        )
        if diag["row_counts_min"] is not None:
            lines.append(
                f"- Resampled row count per replicate: min={diag['row_counts_min']}, "
                f"mean={diag['row_counts_mean']:.1f}, max={diag['row_counts_max']} "
                "(varies because block bootstrap resamples topics, not rows -- a "
                "topic drawn twice contributes its rows twice, a topic not drawn "
                "contributes none).\n"
            )
        if len(freq):
            lines.append(
                "`adjacency_rate` = share of successful replicates where PC placed "
                "any edge (directed or undirected) between the pair; "
                "`orientation_rate_given_adjacent` = of those, share where PC "
                "committed to a direction. Sorted by adjacency_rate descending -- "
                "this table, not the settings-grid recurrence table, is the "
                "stability evidence for Step 5 / thesis Chapter 5. No fixed "
                "stable/unstable cutoff is applied here; choose and justify a "
                "threshold in the writeup.\n"
            )
            lines.append("```")
            lines.append(freq.to_string(index=False))
            lines.append("```\n")
        else:
            lines.append("No successful replicates produced any edge.\n")

    return "\n".join(lines)
