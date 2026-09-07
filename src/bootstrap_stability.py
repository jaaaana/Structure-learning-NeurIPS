import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from bootstrap_stability_report import render_report
from data_prep import DATASETS
from pc_learning import (
    CONTINUOUS_PREDICTORS,
    CONTINUOUS_OUTCOMES,
    DISCRETIZED_PREDICTORS,
    DISCRETIZED_OUTCOMES,
    load_continuous,
    load_discretized,
    run_one_setting,
    edge_recurrence,
)

ROOT = Path(__file__).resolve().parent.parent

BOOT_ALPHA = 0.05


def _report_out(version: str) -> Path:
    suffix = "" if version == "v4" else f"_{version}"
    return ROOT / "reports" / f"bootstrap_stability{suffix}.md"


def _runs_out(version: str) -> Path:
    suffix = "" if version == "v4" else f"_{version}"
    d = ROOT / "reports" / "pc_runs"
    d.mkdir(parents=True, exist_ok=True)
    return d / f"bootstrap_runs{suffix}.json"


def resample_topics(groups: dict, topics: np.ndarray, rng: np.random.Generator) -> pd.DataFrame:
    drawn = rng.choice(topics, size=len(topics), replace=True)
    return pd.concat([groups[t] for t in drawn], ignore_index=True)


def _is_degenerate(df: pd.DataFrame, node_names: list) -> bool:
    return any(df[n].nunique() < 2 for n in node_names)


def run_bootstrap(df: pd.DataFrame, node_names: list, indep_test: str,
                   n_boot: int, seed: int) -> tuple:
    groups = {t: g for t, g in df.groupby("topic")}
    topics = df["topic"].unique()
    rng = np.random.default_rng(seed)

    results = []
    n_degenerate = 0
    n_failed = 0
    row_counts = []

    for i in range(n_boot):
        resampled = resample_topics(groups, topics, rng)
        row_counts.append(len(resampled))

        if _is_degenerate(resampled, node_names):
            n_degenerate += 1
            continue
        try:
            res = run_one_setting(resampled, node_names, indep_test, BOOT_ALPHA, constrained=True)
        except Exception:
            n_failed += 1
            continue
        res["replicate"] = i
        results.append(res)

    diagnostics = {
        "n_boot_requested": n_boot,
        "n_succeeded": len(results),
        "n_degenerate_skipped": n_degenerate,
        "n_failed": n_failed,
        "row_counts_min": int(np.min(row_counts)) if row_counts else None,
        "row_counts_mean": float(np.mean(row_counts)) if row_counts else None,
        "row_counts_max": int(np.max(row_counts)) if row_counts else None,
    }
    return results, diagnostics


def main(version: str = "v4", n_boot: int = 500, seed: int = 0):
    cont_df = load_continuous(version)
    disc_df = load_discretized(version)

    cont_nodes = CONTINUOUS_PREDICTORS + CONTINUOUS_OUTCOMES
    disc_nodes = DISCRETIZED_PREDICTORS + DISCRETIZED_OUTCOMES

    print(f"[{version}] Bootstrapping continuous/Fisher-Z: {n_boot} replicates...")
    cont_results, cont_diag = run_bootstrap(cont_df, cont_nodes, "fisherz", n_boot, seed)
    cont_freq = edge_recurrence(cont_results)

    print(f"[{version}] Bootstrapping discretized/chi-square: {n_boot} replicates...")
    disc_results, disc_diag = run_bootstrap(disc_df, disc_nodes, "chisq", n_boot, seed)
    disc_freq = edge_recurrence(disc_results)

    report = render_report(version, seed, n_boot, BOOT_ALPHA, cont_diag, cont_freq, disc_diag, disc_freq)
    report_out = _report_out(version)
    report_out.write_text(report, encoding="utf-8")

    runs_out = _runs_out(version)
    runs_out.write_text(json.dumps(
        {
            "seed": seed, "n_boot": n_boot,
            "continuous": cont_results, "continuous_diagnostics": cont_diag,
            "discretized": disc_results, "discretized_diagnostics": disc_diag,
        },
        indent=2, default=str,
    ), encoding="utf-8")

    print(f"[{version}] continuous: {cont_diag['n_succeeded']}/{n_boot} succeeded")
    print(f"[{version}] discretized: {disc_diag['n_succeeded']}/{n_boot} succeeded")
    print(f"Wrote {report_out}")
    print(f"Wrote {runs_out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=list(DATASETS.keys()), default="v4")
    parser.add_argument("--n-boot", type=int, default=500)
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()
    main(args.version, args.n_boot, args.seed)
