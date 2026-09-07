import argparse
from pathlib import Path

import pandas as pd

from data_prep_report import render_flags, render_report

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

ID_COLS = ["topic", "year"]
SIZE_COLS = ["n_papers", "n_authors"]
T1_SIZE_COLS = ["n_papers_t1", "n_authors_t1"]
EXOGENOUS = ["year"]

# Same threshold refresh_citations.py's MIN_CELL_SIZE uses for the t
# (current-year) minimum-cell-size filter -- applied here to the t-1
# predictor graph per the 2026-08-19 correction: network
# predictors (topic_share_t1, connectivity_t1, etc.) are measured on the
# topic's t-1 collaboration graph, so *that* graph -- not n_papers at t --
# is what must clear a minimum-size bar before those predictors are trusted.
MIN_T1_SIZE = 20

PREDICTORS_T1 = [
    "topic_share_t1",
    "cross_topic_rate_t1",
    "connectivity_t1",
    "modularity_t1",
    "bridge_concentration_t1",
]
# topic_share (renamed topic_share_t on output) is the new main-model outcome
# per the 2026-08-19 correction -- topic_growth is computed as
# log(topic_share_t) - log(topic_share_t1), so its dependence on
# topic_share_t1 is partly mechanical; topic_share_t as a direct outcome
# avoids that. topic_growth and hit_rate_2yr remain as sensitivity-only
# outcomes (see constraints.py's MAIN_OUTCOMES / SENSITIVITY_OUTCOMES).
OUTCOMES = ["topic_growth", "median_cites_2yr", "log1p_median_c2", "hit_rate_2yr", "topic_share"]
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
    "topic_share",
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


def _zero_rate(s: pd.Series) -> float:
    valid = s.dropna()
    return (valid == 0).mean() if len(valid) else float("nan")


def citation_window_check(df: pd.DataFrame) -> pd.DataFrame:
    aggs = {
        "n_rows": ("topic", "count"),
        "median_cites_2yr_mean": ("median_cites_2yr", "mean"),
        "pct_zero_cites_2yr": ("median_cites_2yr", _zero_rate),
        "hit_rate_2yr_mean": ("hit_rate_2yr", "mean"),
    }
    if "median_cites_3yr" in df.columns:
        aggs["median_cites_3yr_mean"] = ("median_cites_3yr", "mean")
        aggs["pct_zero_cites_3yr"] = ("median_cites_3yr", _zero_rate)
        aggs["n_valid_3yr"] = ("median_cites_3yr", lambda s: int(s.notna().sum()))
    summary = df.groupby("year").agg(**aggs)
    return summary.round(3)


def compute_flag_stats(df: pd.DataFrame) -> dict:
    bc = df["bridge_concentration_t1"]
    mod = df["modularity_t1"]
    return {
        "bc_at_floor": (bc <= 0.05).mean(),
        "bc_at_ceiling": (bc >= 0.95).mean(),
        "mod_min": mod.min(),
        "mod_max": mod.max(),
        "mod_size_corr": mod.corr(df["n_papers"]),
        "skew_raw": df["median_cites_2yr"].skew(),
        "skew_log": df["log1p_median_c2"].skew(),
        "hr_min": df["hit_rate_2yr"].min(),
        "hr_max": df["hit_rate_2yr"].max(),
        "hr_skew": df["hit_rate_2yr"].skew(),
    }


def add_t1_size_cols(df: pd.DataFrame) -> pd.DataFrame:
    if "n_papers_t1" in df.columns:
        return df
    lag = df[["topic", "year"] + SIZE_COLS].rename(
        columns={"n_papers": "n_papers_t1", "n_authors": "n_authors_t1"}
    )
    lag["year"] = lag["year"] + 1
    return df.merge(lag, on=["topic", "year"], how="left")


def min_graph_size_filter(df: pd.DataFrame, min_size: int = MIN_T1_SIZE) -> tuple:
    mask = df["n_papers_t1"].notna() & (df["n_papers_t1"] >= min_size)
    return df[mask].copy(), int((~mask).sum())


def make_continuous_version(df: pd.DataFrame, out_path: Path) -> pd.DataFrame:
    df = add_t1_size_cols(df)
    filtered, n_dropped = min_graph_size_filter(df)
    cols = ID_COLS + SIZE_COLS + T1_SIZE_COLS + PREDICTORS_T1 + OUTCOMES
    out = filtered[cols].rename(columns={"topic_share": "topic_share_t"}).copy()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    return out, n_dropped


def make_discretized_version(df: pd.DataFrame, out_path: Path, n_bins: int = 3) -> pd.DataFrame:
    df = add_t1_size_cols(df)
    filtered, _ = min_graph_size_filter(df)
    out = filtered[ID_COLS + SIZE_COLS + T1_SIZE_COLS].copy()
    labels = [f"q{i + 1}" for i in range(n_bins)]

    for col in TERTILE_VARS:
        out_name = "topic_share_t_bin" if col == "topic_share" else f"{col}_bin"
        out[out_name] = pd.qcut(filtered[col], q=n_bins, labels=labels, duplicates="drop")

    out["bridge_concentration_t1_bin"] = pd.cut(
        filtered["bridge_concentration_t1"],
        bins=[-0.01, 0.95, 1.01],
        labels=["low_or_mid", "high"],
    )
    out["year_bin"] = pd.qcut(filtered["year"], q=n_bins, labels=labels, duplicates="drop")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path, index=False)
    return out


def main(version: str = "v4"):
    paths = DATASETS[version]
    df = load_data(paths["raw"])

    structure = panel_structure(df)
    missing = missing_value_report(df)
    dist = distribution_summary(df, CORE_VARS)
    pearson, spearman = correlation_analysis(df, CORE_VARS)
    flags = render_flags(compute_flag_stats(df))
    outliers = outlier_and_tail_summary(df, CORE_VARS)
    redundant_pairs = redundancy_check(df, CORE_VARS)
    size_instability = small_graph_instability(df)
    citation_window = citation_window_check(df)

    _, n_dropped_t1 = make_continuous_version(df, paths["continuous_out"])
    make_discretized_version(df, paths["discretized_out"])

    report = render_report(df, structure, missing, dist, pearson, flags,
                            outliers, redundant_pairs, size_instability,
                            citation_window, version, paths["raw"],
                            paths["continuous_out"], paths["discretized_out"],
                            n_dropped_t1, MIN_T1_SIZE)
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
