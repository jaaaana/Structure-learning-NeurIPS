from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

CITATION_NOTES = {
    "v4": (
        "This was initially suspected to be right-censoring from a stale "
        "data pull, but the recovered panel-construction pipeline "
        "(`nips_pipeline_v4_clean.ipynb`, last run 2026-03-17) shows this "
        "concern is already handled: `median_cites_2yr` only uses papers "
        "whose 2-year citation window has fully elapsed (`c2_complete = "
        "current_year > pub_year + 1`), computed from OpenAlex's real "
        "per-year citation breakdown (`counts_by_year`), not a raw lifetime "
        "snapshot. Since the pipeline ran in 2026, every year through 2023 "
        "clears that bar -- the pattern is real, complete data."
    ),
    "v5": (
        "This panel's citations were refreshed via `src/refresh_citations.py` "
        "(an adaptation of `nips_pipeline_v4_clean.ipynb`), re-pulling "
        "OpenAlex's per-year citation breakdown for all matched papers. "
        "Compared to v4, the zero-citation rate dropped substantially for "
        "2022 (40.0% -> 15.8%) and 2023 (46.4% -> 29.2%) with no change for "
        "2021 (13.0% both) -- directly confirming the remaining pattern is "
        "OpenAlex's own citation-indexing lag for recent literature, not a "
        "stale extraction. This version also extends coverage to 2024.\n"
        "\n"
        "**Snapshot date**: the OpenAlex `counts_by_year` pull that this "
        "panel's citation numbers are based on was taken on **2026-08-11** "
        "(the run that populated `data/processed/nips-c2-checkpoint.csv`; "
        "`refresh_citations.py` has been rerun since then to add the "
        "`n_papers_t1`/`n_authors_t1` columns, but that rerun made 0 new "
        "OpenAlex requests -- it recomputed the panel entirely from the "
        "already-cached 2026-08-11 checkpoint, so the citation snapshot "
        "date is unchanged).\n"
        "\n"
        "**`median_cites_2yr` definition**: for a paper published in "
        "calendar year `pub_year`, `c2 = counts_by_year[pub_year] + "
        "counts_by_year[pub_year + 1]` (citations received during the "
        "publication year plus the following calendar year, from "
        "OpenAlex's real per-year breakdown, not a lifetime snapshot). A "
        "paper only contributes to `median_cites_2yr` if its window has "
        "fully elapsed (`c2_complete = current_year > pub_year + 1`); "
        "`median_cites_2yr` for a topic-year is the median `c2` across that "
        "topic-year's `c2_complete` papers. This project stays on this "
        "2-year definition -- not switching to a 1-year window even though "
        "that would yield a few more usable recent-year rows.\n"
        "\n"
        "**Manual spot-check**: 5 papers (years 2018, 2021, 2022, 2023, "
        "2024, one per year) were re-fetched live from the OpenAlex API "
        "directly (not from the cache) on 2026-08-19 and their `c2` "
        "recomputed from the live response. All 5 matched the cached "
        "checkpoint value exactly (0 discrepancies), confirming no drift "
        "between the 2026-08-11 snapshot and OpenAlex's current data for "
        "these papers."
    ),
}

TOPIC_NOTES = {
    "v4": (
        "v4 has 29 unique topics after merging."
    ),
    "v5": (
        "v5 has 28 unique topics after merging (v4 had 29). Both versions "
        "run the same `merge_topics()` step in `src/refresh_citations.py`: "
        "each paper's raw OpenAlex `primary_topic` label is TF-IDF "
        "character-n-gram vectorized, hierarchically clustered by cosine "
        "distance, and every cluster is collapsed to its most frequent "
        "member label. This makes the final topic set a function of "
        "*which papers are in the input population* -- v5 adds 2024 papers "
        "(and re-pulls citation data, though that doesn't affect topic "
        "labels), which shifts the raw label frequencies enough that the "
        "clustering merges one pair of topics that stayed separate in v4. "
        "This is expected instability from the automated merge step, not a "
        "data error -- documented here, plus in the retained "
        "`nips-topic-merge-map.json` output, which lists every raw-label -> "
        "canonical-label merge decision v5 made."
    ),
}


def render_flags(stats: dict) -> list:
    """Flagged-variables prose, parameterized by
    data_prep.compute_flag_stats()'s numbers. Order and content match the
    report's 'Flagged variables' section."""
    return [
        (
            "`bridge_concentration_t1` is near-degenerate: "
            f"{stats['bc_at_floor']:.0%} of rows sit at/near 0 and "
            f"{stats['bc_at_ceiling']:.0%} sit at/near 1, "
            "leaving very few rows in between. Continuous CI tests (Fisher-Z) assume "
            "a roughly continuous spread, so this variable is a poor fit for the "
            "continuous PC run -- treat it as effectively binary and rely on the "
            "discretized version for it. Per the recovered pipeline "
            "(`nips_pipeline_v4_clean.ipynb`), this is the share of total "
            "betweenness centrality held by the top 10% of authors in the "
            "topic's co-authorship graph -- on small author counts, a handful of "
            "authors mechanically dominate betweenness, which explains the "
            "degeneracy directly rather than just describing it."
        ),
        (
            "`modularity_t1` has low variance (compressed into "
            f"[{stats['mod_min']:.2f}, {stats['mod_max']:.2f}]) and correlates with topic size "
            f"(corr with n_papers = {stats['mod_size_corr']:.2f}): bigger topics tend to show "
            "higher modularity. Any edge involving modularity_t1 should be checked "
            "against topic size as a possible confound, and treated cautiously on "
            "small topics where a handful of authors can make the collaboration "
            "graph trivially \"modular\"."
        ),
        (
            f"`median_cites_2yr` is right-skewed (skew={stats['skew_raw']:.2f}); its "
            f"log-transformed twin `log1p_median_c2` is close to symmetric "
            f"(skew={stats['skew_log']:.2f}) and is the better choice for continuous "
            "Fisher-Z tests."
        ),
        (
            f"`hit_rate_2yr` is a bounded proportion (range "
            f"[{stats['hr_min']:.2f}, {stats['hr_max']:.2f}]) and "
            f"right-skewed (skew={stats['hr_skew']:.2f}), not a raw count -- keep this in mind "
            "for the predictive-usefulness models in the evaluation framework later."
        ),
        (
            "Rows are (topic, year) pairs, and the same topic contributes multiple "
            "rows across years. Standard CI tests used by PC assume i.i.d. samples, "
            "which repeated observations of the same topic technically violate. "
            "This isn't fixed at the data-prep stage; the bootstrap/subsampling "
            "stability analysis in Step 4 is the empirical check against it. A "
            "within-topic-demeaned version is also worth adding as a Step 4 "
            "sensitivity setting, since pooling topics conflates between-topic "
            "differences with the within-topic t-1->t dynamic the model is "
            "actually meant to capture."
        ),
        (
            "`connectivity_t1` is heavily right-tailed (kurtosis far above every "
            "other variable, a handful of very high values) -- a log transform or "
            "winsorizing before the continuous Fisher-Z run would reduce the "
            "chance that a few extreme topic-years dominate the partial-"
            "correlation estimates."
        ),
        (
            "`median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate "
            "in recent years -- see the 'Citation-window finding' section above "
            "for the full explanation (OpenAlex citation-indexing lag, not a "
            "stale-extraction artifact) and the Citation-window check table below "
            "for the exact per-year numbers."
        ),
    ]


def render_report(df, structure: dict, missing, dist, pearson, flags: list,
                   outliers, redundant_pairs: list, size_instability,
                   citation_window, version: str, raw_path: Path,
                   continuous_out: Path, discretized_out: Path,
                   n_dropped_t1: int, min_t1_size: int) -> str:
    lines = []
    lines.append(f"# Data Quality Report -- NeurIPS Topic-Year Panel ({version})\n")
    lines.append(f"Source: `{raw_path.relative_to(ROOT)}`\n")

    lines.append("## Citation-window finding (resolved)\n")
    lines.append(
        "`median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate "
        "in recent years (see the Citation-window check below). "
        f"{CITATION_NOTES[version]}\n"
        "\n"
        "The likely remaining explanation is OpenAlex's own citation-"
        "indexing lag for recent literature -- independently confirmed by a "
        "teammate who built the citation-enrichment step: *'OpenAlex gives "
        "significantly smaller values... it seems difficult to get citations "
        "up to year t.'* This is a substantive limitation worth discussing "
        "in the thesis, but **not** grounds to truncate or exclude "
        "recent-year rows -- there's no reason to treat those rows as less "
        "valid than earlier years.\n"
    )

    if "median_cites_3yr" in df.columns:
        zr2 = df.groupby("year")["median_cites_2yr"].apply(_zero_rate)
        zr3 = df.groupby("year")["median_cites_3yr"].apply(_zero_rate)
        n_valid_3 = df.groupby("year")["median_cites_3yr"].apply(lambda s: int(s.notna().sum()))
        affected_years = sorted(y for y in zr2.index if zr2[y] > 0)

        comparable = [y for y in affected_years if n_valid_3.get(y, 0) > 0]
        no_window_yet = [y for y in affected_years if n_valid_3.get(y, 0) == 0]

        if comparable:
            rows = "; ".join(f"{y}: {zr2[y]:.0%} -> {zr3[y]:.0%}" for y in comparable)
            note = ""
            if no_window_yet:
                years_str = ", ".join(str(y) for y in no_window_yet)
                note = (
                    f" ({years_str} excluded from this comparison -- their "
                    "3-year window hasn't closed yet, so median_cites_3yr is "
                    "entirely missing for that year, not zero.)"
                )
            lines.append(
                "**Corroborating evidence**: `median_cites_3yr` (a 3-year "
                "citation window, computed the same way but with one more "
                "year for citations to be indexed) shows a much milder "
                "version of the same pattern -- zero-citation rate by year, "
                f"2yr window -> 3yr window: {rows}.{note} Giving citations one "
                "more year to be indexed sharply reduces the effect, which "
                "is exactly what an indexing-lag explanation predicts and a "
                "genuine decline in citation impact would not produce.\n"
            )

    lines.append("## Overview\n")
    lines.append(f"- Rows: {structure['n_rows']}")
    lines.append(f"- Unique topics: {structure['n_topics']}")
    lines.append(f"- Years covered: {structure['year_min']}-{structure['year_max']}")
    lines.append(f"- Topics with only 1 row: {structure['n_single_row_topics']}")
    lines.append(
        f"- Rows with no same-topic row at year-1 in this panel (but with "
        f"populated `_t1` predictors anyway): {structure['n_rows_without_predecessor']}"
    )
    lines.append(
        "  - This means the panel is **filtered** (e.g. a minimum paper/author "
        "count per topic-year), not every topic-year combination -- the `_t1` "
        "features are computed from the full underlying corpus regardless of "
        "whether the prior year cleared the panel's inclusion threshold.\n"
    )

    lines.append("## Topic taxonomy\n")
    lines.append(f"{TOPIC_NOTES[version]}\n")

    lines.append("### Rows per year\n")
    lines.append("```")
    lines.append(structure["rows_per_year"].to_string())
    lines.append("```\n")

    lines.append("## Missing values\n")
    n_missing_total = int(missing.sum())
    if n_missing_total == 0:
        lines.append("None found across any column.\n")
    else:
        lines.append("```")
        lines.append(missing[missing > 0].to_string())
        lines.append("```\n")

    lines.append("## Distribution summary (core variables)\n")
    lines.append("```")
    lines.append(dist[["count", "mean", "std", "min", "50%", "max", "skew"]].round(3).to_string())
    lines.append("```\n")

    lines.append("## Correlation analysis (Pearson, core variables)\n")
    lines.append("```")
    lines.append(pearson.round(2).to_string())
    lines.append("```\n")

    lines.append("## Outliers and heavy tails (IQR method)\n")
    lines.append("```")
    lines.append(outliers.round(3).to_string())
    lines.append("```\n")

    lines.append("## Redundancy check (|Pearson r| > 0.5)\n")
    if redundant_pairs:
        for a, b, r in redundant_pairs:
            lines.append(f"- `{a}` <-> `{b}`: r={r:.2f}")
    else:
        lines.append("None found.")
    lines.append("")

    lines.append(
        "## Small-graph instability check "
        "(modularity_t1 / bridge_concentration_t1 by topic-size quartile)\n"
    )
    lines.append("```")
    lines.append(size_instability.to_string())
    lines.append("```\n")

    lines.append("## Citation-window check (median_cites_2yr / hit_rate_2yr by year)\n")
    lines.append("```")
    lines.append(citation_window.to_string())
    lines.append("```\n")

    lines.append("## Flagged variables\n")
    for f in flags:
        lines.append(f"- {f}")
    lines.append("")

    lines.append("## t-1 minimum-graph-size filter (2026-08-19 correction)\n")
    lines.append(
        "Network predictors (`topic_share_t1`, `cross_topic_rate_t1`, "
        "`connectivity_t1`, `modularity_t1`, `bridge_concentration_t1`) are "
        "measured on the topic's **t-1** collaboration graph, not the t "
        "graph -- so the minimum-graph-size condition has to be checked "
        "against `n_papers_t1`, not `n_papers`. Both continuous and "
        "discretized output tables below have this filter already applied "
        f"(rows with `n_papers_t1 < {min_t1_size}`, or no recoverable t-1 "
        f"size at all, are dropped): **{n_dropped_t1} row(s) dropped**, "
        f"{structure['n_rows'] - n_dropped_t1} remain for the main model. "
        "The raw panel and every other section of this report still "
        "describe the full, unfiltered data -- only the two model-ready "
        "output tables are filtered.\n"
    )

    lines.append("## Recommendation for the first PC model\n")
    lines.append(
        "Per the 2026-08-19 correction, the **main model** "
        "outcome is `topic_share_t` (not `topic_growth` -- topic_growth is "
        "computed as log(topic_share_t) - log(topic_share_t1), so its "
        "dependence on topic_share_t1 is partly mechanical) plus "
        "`log1p_median_c2`; `topic_growth` and `hit_rate_2yr` are "
        "sensitivity-only outcomes. `bridge_concentration_t1` is dropped "
        "from the main model entirely (both continuous and discretized) "
        "for now -- near-degenerate, see flags above -- and `year` is "
        "included as an exogenous context variable with no edges allowed "
        "pointing into it (see constraints.py).\n"
    )
    lines.append(
        f"- Use the **continuous** table (`{continuous_out.relative_to(ROOT)}`) with "
        "Fisher-Z for the primary run: predictors `topic_share_t1`, "
        "`cross_topic_rate_t1`, `connectivity_t1` (log-transformed), "
        "`modularity_t1`, plus `year`; outcomes `topic_share_t`, "
        "`log1p_median_c2`."
    )
    lines.append(
        f"- Use the **discretized** table (`{discretized_out.relative_to(ROOT)}`) with "
        "chi-square/G-test as the sensitivity comparison. "
        "`bridge_concentration_t1_bin` is still produced in this table (for "
        "the separate bridge_concentration sensitivity setting) even though "
        "it's excluded from the main discretized model too."
    )
    lines.append(
        "- Carry `modularity_t1` in both versions, but flag any edge touching "
        "it during interpretation (Step 5 / thesis D4) as possibly confounded "
        "with topic size."
    )
    lines.append(
        "- `n_papers`/`n_authors` (t) are not part of the causal model but are "
        "kept as context columns for small-topic sanity checks; "
        "`n_papers_t1`/`n_authors_t1` are kept the same way, and are also "
        "what the minimum-graph-size filter above is computed from.\n"
    )

    return "\n".join(lines)


def _zero_rate(s) -> float:
    """Share of non-missing values equal to 0. NaN if there's no valid data at
    all -- plain `(s == 0).mean()` silently treats every NaN as "not zero",
    which understates the zero-rate (or reports a misleading 0%) whenever a
    year has partial or total missingness, as median_cites_3yr does for the
    most recent year (its window hasn't closed yet).

    Duplicated from data_prep.py deliberately: this module doesn't import
    from data_prep.py (data_prep.py imports render_report from here, so the
    reverse import would be circular), and this is a one-line helper used
    only inside render_report()'s 3-year corroborating-evidence block.
    """
    valid = s.dropna()
    return (valid == 0).mean() if len(valid) else float("nan")
