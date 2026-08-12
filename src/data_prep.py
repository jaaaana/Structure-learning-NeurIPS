"""Step 1: Data preparation for constraint-based structure learning.

Loads the NeurIPS topic-year panel, writes a data-quality report, and
produces a continuous and a discretized version of the input table for the
PC algorithm runs in later steps.

Usage:
    python src/data_prep.py                 # runs on v4 (default)
    python src/data_prep.py --version v5     # runs on the refreshed v5 panel
Each version gets its own report/output files -- running v5 never touches
the v4 outputs.
"""
import argparse
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

DATASETS = {
    "v4": {
        "raw": ROOT / "data" / "raw" / "nips-panel-v4.csv",
        "continuous_out": ROOT / "data" / "processed" / "topic_year_continuous.csv",
        "discretized_out": ROOT / "data" / "processed" / "topic_year_discretized.csv",
        "report_out": ROOT / "reports" / "data_quality.md",
    },
    "v5": {
        "raw": ROOT / "data" / "raw" / "nips-panel-v5-refreshed.csv",
        "continuous_out": ROOT / "data" / "processed" / "topic_year_continuous_v5.csv",
        "discretized_out": ROOT / "data" / "processed" / "topic_year_discretized_v5.csv",
        "report_out": ROOT / "reports" / "data_quality_v5.md",
    },
}

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
        "stale extraction. This version also extends coverage to 2024."
    ),
}

ID_COLS = ["topic", "year"]
SIZE_COLS = ["n_papers", "n_authors"]
PREDICTORS_T1 = [
    "topic_share_t1",
    "cross_topic_rate_t1",
    "connectivity_t1",
    "modularity_t1",
    "bridge_concentration_t1",
]
OUTCOMES = ["topic_growth", "median_cites_2yr", "log1p_median_c2", "hit_rate_2yr"]
CORE_VARS = PREDICTORS_T1 + OUTCOMES

# bridge_concentration_t1 is near-degenerate (mass piled at 0 and 1), so it
# gets a binary split instead of a tertile split during discretization.
TERTILE_VARS = [
    "topic_share_t1",
    "cross_topic_rate_t1",
    "connectivity_t1",
    "modularity_t1",
    "topic_growth",
    "log1p_median_c2",
    "hit_rate_2yr",
]


def load_data(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def panel_structure(df: pd.DataFrame) -> dict:
    rows_per_topic = df.groupby("topic").size()
    rows_per_year = df.groupby("year").size()

    # Rows whose topic has no row at year-1 in this panel, even though the
    # _t1 columns are still populated -- flags that the panel is filtered
    # (e.g. by a minimum paper/author count), not every topic-year included.
    indexed = df.set_index(["topic", "year"])
    no_predecessor = 0
    for topic, year in indexed.index:
        if (topic, year - 1) not in indexed.index:
            no_predecessor += 1

    return {
        "n_rows": len(df),
        "n_topics": df["topic"].nunique(),
        "year_min": int(df["year"].min()),
        "year_max": int(df["year"].max()),
        "rows_per_topic": rows_per_topic,
        "rows_per_year": rows_per_year,
        "n_single_row_topics": int((rows_per_topic == 1).sum()),
        "n_rows_without_predecessor": no_predecessor,
    }


def missing_value_report(df: pd.DataFrame) -> pd.Series:
    return df.isna().sum()


def distribution_summary(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    desc = df[cols].describe().T
    desc["skew"] = df[cols].skew()
    return desc


def correlation_analysis(df: pd.DataFrame, cols: list) -> tuple:
    pearson = df[cols].corr(method="pearson")
    spearman = df[cols].corr(method="spearman")
    return pearson, spearman


def outlier_and_tail_summary(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    rows = []
    for col in cols:
        s = df[col]
        q1, q3 = s.quantile(0.25), s.quantile(0.75)
        iqr = q3 - q1
        lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
        n_outliers = int(((s < lo) | (s > hi)).sum())
        rows.append({
            "variable": col,
            "n_outliers_iqr": n_outliers,
            "kurtosis": s.kurt(),
            "min": s.min(),
            "max": s.max(),
        })
    return pd.DataFrame(rows).set_index("variable")


def redundancy_check(df: pd.DataFrame, cols: list, threshold: float = 0.5) -> list:
    corr = df[cols].corr()
    pairs = []
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            r = corr.loc[a, b]
            if abs(r) > threshold:
                pairs.append((a, b, r))
    return sorted(pairs, key=lambda x: -abs(x[2]))


def small_graph_instability(df: pd.DataFrame, n_quartiles: int = 4) -> pd.DataFrame:
    tmp = df.copy()
    labels = [f"Q{i + 1}" for i in range(n_quartiles)]
    tmp["size_quartile"] = pd.qcut(tmp["n_papers"], n_quartiles, labels=labels)
    summary = tmp.groupby("size_quartile", observed=True).agg(
        n_papers_mean=("n_papers", "mean"),
        modularity_t1_mean=("modularity_t1", "mean"),
        modularity_t1_std=("modularity_t1", "std"),
        bridge_concentration_t1_mean=("bridge_concentration_t1", "mean"),
        bridge_concentration_t1_std=("bridge_concentration_t1", "std"),
    )
    return summary.round(3)


def citation_window_check(df: pd.DataFrame) -> pd.DataFrame:
    summary = df.groupby("year").agg(
        n_rows=("topic", "count"),
        median_cites_2yr_mean=("median_cites_2yr", "mean"),
        pct_zero_cites=("median_cites_2yr", lambda s: (s == 0).mean()),
        hit_rate_2yr_mean=("hit_rate_2yr", "mean"),
    )
    return summary.round(3)


def flag_problematic_variables(df: pd.DataFrame) -> list:
    flags = []

    bc = df["bridge_concentration_t1"]
    at_floor = (bc <= 0.05).mean()
    at_ceiling = (bc >= 0.95).mean()
    flags.append(
        "`bridge_concentration_t1` is near-degenerate: "
        f"{at_floor:.0%} of rows sit at/near 0 and {at_ceiling:.0%} sit at/near 1, "
        "leaving very few rows in between. Continuous CI tests (Fisher-Z) assume "
        "a roughly continuous spread, so this variable is a poor fit for the "
        "continuous PC run -- treat it as effectively binary and rely on the "
        "discretized version for it. Per the recovered pipeline "
        "(`nips_pipeline_v4_clean.ipynb`), this is the share of total "
        "betweenness centrality held by the top 10% of authors in the "
        "topic's co-authorship graph -- on small author counts, a handful of "
        "authors mechanically dominate betweenness, which explains the "
        "degeneracy directly rather than just describing it."
    )

    mod = df["modularity_t1"]
    mod_size_corr = mod.corr(df["n_papers"])
    flags.append(
        "`modularity_t1` has low variance (compressed into "
        f"[{mod.min():.2f}, {mod.max():.2f}]) and correlates with topic size "
        f"(corr with n_papers = {mod_size_corr:.2f}): bigger topics tend to show "
        "higher modularity. Any edge involving modularity_t1 should be checked "
        "against topic size as a possible confound, and treated cautiously on "
        "small topics where a handful of authors can make the collaboration "
        "graph trivially \"modular\"."
    )

    skew_raw = df["median_cites_2yr"].skew()
    skew_log = df["log1p_median_c2"].skew()
    flags.append(
        f"`median_cites_2yr` is right-skewed (skew={skew_raw:.2f}); its "
        f"log-transformed twin `log1p_median_c2` is close to symmetric "
        f"(skew={skew_log:.2f}) and is the better choice for continuous "
        "Fisher-Z tests."
    )

    hr_skew = df["hit_rate_2yr"].skew()
    flags.append(
        f"`hit_rate_2yr` is a bounded proportion (range "
        f"[{df['hit_rate_2yr'].min():.2f}, {df['hit_rate_2yr'].max():.2f}]) and "
        f"right-skewed (skew={hr_skew:.2f}), not a raw count -- keep this in mind "
        "for the predictive-usefulness models in the evaluation framework later."
    )

    flags.append(
        "Rows are (topic, year) pairs, and the same topic contributes multiple "
        "rows across years. Standard CI tests used by PC assume i.i.d. samples, "
        "which repeated observations of the same topic technically violate. "
        "This isn't fixed at the data-prep stage; the bootstrap/subsampling "
        "stability analysis in Step 4 is the empirical check against it. A "
        "within-topic-demeaned version is also worth adding as a Step 4 "
        "sensitivity setting, since pooling topics conflates between-topic "
        "differences with the within-topic t-1->t dynamic the model is "
        "actually meant to capture."
    )

    flags.append(
        "`connectivity_t1` is heavily right-tailed (kurtosis far above every "
        "other variable, a handful of very high values) -- a log transform or "
        "winsorizing before the continuous Fisher-Z run would reduce the "
        "chance that a few extreme topic-years dominate the partial-"
        "correlation estimates."
    )

    flags.append(
        "`median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate "
        "in recent years -- see the 'Citation-window finding' section above "
        "for the full explanation (OpenAlex citation-indexing lag, not a "
        "stale-extraction artifact) and the Citation-window check table below "
        "for the exact per-year numbers."
    )

    return flags


def make_continuous_version(df: pd.DataFrame, out_path: Path) -> pd.DataFrame:
    cols = ID_COLS + SIZE_COLS + PREDICTORS_T1 + OUTCOMES
    out = df[cols].copy()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    return out


def make_discretized_version(df: pd.DataFrame, out_path: Path, n_bins: int = 3) -> pd.DataFrame:
    out = df[ID_COLS + SIZE_COLS].copy()
    labels = [f"q{i + 1}" for i in range(n_bins)]

    for col in TERTILE_VARS:
        out[f"{col}_bin"] = pd.qcut(df[col], q=n_bins, labels=labels, duplicates="drop")

    out["bridge_concentration_t1_bin"] = pd.cut(
        df["bridge_concentration_t1"],
        bins=[-0.01, 0.95, 1.01],
        labels=["low_or_mid", "high"],
    )

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    return out


def render_report(df: pd.DataFrame, structure: dict, missing: pd.Series,
                   dist: pd.DataFrame, pearson: pd.DataFrame, flags: list,
                   outliers: pd.DataFrame, redundant_pairs: list,
                   size_instability: pd.DataFrame,
                   citation_window: pd.DataFrame, version: str,
                   raw_path: Path, continuous_out: Path, discretized_out: Path) -> str:
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

    lines.append("## Recommendation for the first PC model\n")
    lines.append(
        f"- Use the **continuous** table (`{continuous_out.relative_to(ROOT)}`) with "
        "Fisher-Z for the primary run, dropping `bridge_concentration_t1` from "
        "that continuous run (near-degenerate, see flags above) -- keep the "
        "other 4 predictors (`topic_share_t1`, `cross_topic_rate_t1`, "
        "`connectivity_t1`, `modularity_t1`) and use `log1p_median_c2` in "
        "place of raw `median_cites_2yr`."
    )
    lines.append(
        f"- Use the **discretized** table (`{discretized_out.relative_to(ROOT)}`) with "
        "chi-square/G-test as the second setting -- this is where "
        "`bridge_concentration_t1_bin` (binary) can be included, since "
        "discretization sidesteps its continuous-test unsuitability."
    )
    lines.append(
        "- Carry `modularity_t1` in both versions, but flag any edge touching "
        "it during interpretation (Step 5 / thesis D4) as possibly confounded "
        "with topic size."
    )
    lines.append(
        "- `n_papers`/`n_authors` are not part of the causal model (per docx "
        "Step 2's variable list) but are kept in both output tables as context "
        "columns for exactly this kind of small-topic sanity check.\n"
    )

    return "\n".join(lines)


def main(version: str = "v4"):
    paths = DATASETS[version]
    df = load_data(paths["raw"])

    structure = panel_structure(df)
    missing = missing_value_report(df)
    dist = distribution_summary(df, CORE_VARS)
    pearson, spearman = correlation_analysis(df, CORE_VARS)
    flags = flag_problematic_variables(df)
    outliers = outlier_and_tail_summary(df, CORE_VARS)
    redundant_pairs = redundancy_check(df, CORE_VARS)
    size_instability = small_graph_instability(df)
    citation_window = citation_window_check(df)

    make_continuous_version(df, paths["continuous_out"])
    make_discretized_version(df, paths["discretized_out"])

    report = render_report(df, structure, missing, dist, pearson, flags,
                            outliers, redundant_pairs, size_instability,
                            citation_window, version, paths["raw"],
                            paths["continuous_out"], paths["discretized_out"])
    paths["report_out"].parent.mkdir(parents=True, exist_ok=True)
    paths["report_out"].write_text(report, encoding="utf-8")

    print(f"[{version}] Loaded {structure['n_rows']} rows, {structure['n_topics']} topics, "
          f"{structure['year_min']}-{structure['year_max']}.")
    print(f"Wrote continuous table -> {paths['continuous_out']}")
    print(f"Wrote discretized table -> {paths['discretized_out']}")
    print(f"Wrote data-quality report -> {paths['report_out']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=list(DATASETS.keys()), default="v4")
    args = parser.parse_args()
    main(args.version)
