import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold

from pc_bootstrap_stability import run_bootstrap
from constraints import EXOGENOUS, MAIN_OUTCOMES
from data_prep import DATASETS
from pc_learning import CONNECTIVITY_LOG_VARIANT, CONTINUOUS_PREDICTORS, CONTINUOUS_OUTCOMES, edge_recurrence, load_continuous
from pc_predictive_usefulness_report import render_report

ROOT = Path(__file__).resolve().parent.parent

N_SPLITS = 5
GRAPH_PARENT_THRESHOLD = 0.5
N_BOOT_PER_FOLD = 150
NESTED_SEED = 0
ROBUSTNESS_THRESHOLDS = [0.3, 0.5, 0.7]

COLUMN_FOR_BASE = {"connectivity_t1": CONNECTIVITY_LOG_VARIANT}

BASELINE_FEATURES = {"topic_share_t": ["topic_share_t1", "year"], "log1p_median_c2": ["year"]}


def _suffix(version: str) -> str:
    return "" if version == "v4" else f"_{version}"


def _report_out(version: str) -> Path:
    return ROOT / "reports" / f"predictive_usefulness{_suffix(version)}.md"


def _nested_cv_path(version: str) -> Path:
    return ROOT / "reports" / "pc_runs" / f"predictive_nested_cv{_suffix(version)}.json"


def _cv_scores(df: pd.DataFrame, features: list, target: str, model, folds: list) -> dict:
    X = df[features].to_numpy(dtype=float) if features else np.zeros((len(df), 0))
    y = df[target].to_numpy(dtype=float)
    n_groups = df["topic"].nunique()

    if n_groups < N_SPLITS:
        model.fit(X, y)
        pred = model.predict(X)
        return {
            "n_splits_used": 1,
            "note": f"only {n_groups} topics, below N_SPLITS={N_SPLITS} -- reporting in-sample fit, not CV",
            "r2_mean": r2_score(y, pred), "r2_std": 0.0,
            "mae_mean": mean_absolute_error(y, pred), "mae_std": 0.0,
        }

    r2s, maes = [], []
    for train_idx, test_idx in folds:
        model.fit(X[train_idx], y[train_idx])
        pred = model.predict(X[test_idx])
        r2s.append(r2_score(y[test_idx], pred))
        maes.append(mean_absolute_error(y[test_idx], pred))

    return {
        "n_splits_used": len(folds), "note": "",
        "r2_mean": float(np.mean(r2s)), "r2_std": float(np.std(r2s)),
        "mae_mean": float(np.mean(maes)), "mae_std": float(np.std(maes)),
    }


def nested_graph_parents(df: pd.DataFrame, folds: list, n_boot_per_fold: int, base_seed: int) -> dict:
    """Leakage-free graph-selected-predictor comparison: for each fold, the
    predictor-selection bootstrap runs on that fold's TRAINING topics only
    (never the held-out ones), so the choice of which predictors to trust is
    exactly as blind to the test topics as the regression coefficients
    already are. Model features are always BASELINE_FEATURES[outcome] plus
    whatever additional predictors that fold's bootstrap selected -- never
    the selected predictors alone -- so the comparison against `baseline`
    stays a strict superset (nested) comparison."""
    node_names = CONTINUOUS_PREDICTORS + CONTINUOUS_OUTCOMES
    per_outcome = {outcome: {"r2s": [], "maes": [], "added_per_fold": []} for outcome in MAIN_OUTCOMES}
    fold_diagnostics = []

    for fold_idx, (train_idx, test_idx) in enumerate(folds):
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]
        n_train_topics = train_df["topic"].nunique()
        fold_results, fold_diag = run_bootstrap(train_df, node_names, "fisherz", n_boot_per_fold, base_seed + fold_idx)
        fold_diag["n_train_topics"] = n_train_topics
        fold_diagnostics.append(fold_diag)
        print(f"  fold {fold_idx}: {n_train_topics} training topics, "
              f"{fold_diag['n_succeeded']}/{n_boot_per_fold} bootstrap replicates succeeded "
              f"({fold_diag['n_degenerate_skipped']} degenerate, {fold_diag['n_failed']} failed)")
        fold_freq = edge_recurrence(fold_results).set_index(["from", "to"])["adjacency_rate"]

        for outcome in MAIN_OUTCOMES:
            selected_base = [frm for (frm, to) in fold_freq.index
                              if to == outcome and fold_freq[(frm, to)] >= GRAPH_PARENT_THRESHOLD]
            baseline_cols = BASELINE_FEATURES[outcome]
            added_cols = [COLUMN_FOR_BASE.get(p, p) for p in selected_base
                          if COLUMN_FOR_BASE.get(p, p) not in baseline_cols]
            feature_cols = baseline_cols + added_cols

            model = LinearRegression()
            model.fit(train_df[feature_cols].to_numpy(dtype=float), train_df[outcome].to_numpy(dtype=float))
            pred = model.predict(test_df[feature_cols].to_numpy(dtype=float))

            per_outcome[outcome]["r2s"].append(r2_score(test_df[outcome].to_numpy(dtype=float), pred))
            per_outcome[outcome]["maes"].append(mean_absolute_error(test_df[outcome].to_numpy(dtype=float), pred))
            per_outcome[outcome]["added_per_fold"].append(added_cols)

    results = {}
    for outcome in MAIN_OUTCOMES:
        r2s = per_outcome[outcome]["r2s"]
        maes = per_outcome[outcome]["maes"]
        added_per_fold = per_outcome[outcome]["added_per_fold"]
        n_folds = len(r2s)

        counts = {}
        for added in added_per_fold:
            for p in added:
                counts[p] = counts.get(p, 0) + 1
        if counts:
            selection_note = "additional predictors selected per fold beyond the baseline: " + ", ".join(
                f"{p} ({c}/{n_folds} folds)" for p, c in sorted(counts.items(), key=lambda kv: -kv[1]))
        else:
            selection_note = "no additional predictor cleared the threshold in any fold"

        results[outcome] = {
            "label": f"baseline features + graph-selected predictors, nested per-fold bootstrap "
                     f"({n_boot_per_fold} reps/fold, continuous/Fisher-Z, threshold={GRAPH_PARENT_THRESHOLD}, "
                     f"base_seed={base_seed} -> per-fold seeds {base_seed}..{base_seed + len(folds) - 1})",
            "base_seed": base_seed,
            "features": BASELINE_FEATURES[outcome],
            "per_fold_added": added_per_fold,
            "fold_diagnostics": fold_diagnostics,
            "n_splits_used": n_folds,
            "note": selection_note,
            "r2_mean": float(np.mean(r2s)), "r2_std": float(np.std(r2s)),
            "mae_mean": float(np.mean(maes)), "mae_std": float(np.std(maes)),
        }
    return results


def threshold_robustness(df: pd.DataFrame, folds: list, n_boot_per_fold: int, base_seed: int,
                          thresholds: list = ROBUSTNESS_THRESHOLDS) -> dict:
    """Checks whether the predictive-usefulness conclusion depends on the
    predictor-selection threshold, per the mentor's instruction: same 5
    folds/settings as `nested_graph_parents`, each fold's training-only
    bootstrap frequency table computed ONCE (150 reps), then every threshold
    in `thresholds` is applied to that same table -- never re-bootstrapped
    per threshold. Baseline features are always kept; only the additional
    selected predictors vary by threshold. The goal is not to pick the best
    threshold, but to see whether R2/MAE (and the selected predictors) stay
    materially the same across a stricter vs. looser selection rule."""
    node_names = CONTINUOUS_PREDICTORS + CONTINUOUS_OUTCOMES
    per_outcome = {outcome: {t: {"r2s": [], "maes": [], "added_per_fold": []} for t in thresholds}
                   for outcome in MAIN_OUTCOMES}
    fold_diagnostics = []

    for fold_idx, (train_idx, test_idx) in enumerate(folds):
        train_df = df.iloc[train_idx]
        test_df = df.iloc[test_idx]
        n_train_topics = train_df["topic"].nunique()
        fold_results, fold_diag = run_bootstrap(train_df, node_names, "fisherz", n_boot_per_fold, base_seed + fold_idx)
        fold_diag["n_train_topics"] = n_train_topics
        fold_diagnostics.append(fold_diag)
        print(f"  [threshold robustness] fold {fold_idx}: {n_train_topics} training topics, "
              f"{fold_diag['n_succeeded']}/{n_boot_per_fold} bootstrap replicates succeeded "
              f"({fold_diag['n_degenerate_skipped']} degenerate, {fold_diag['n_failed']} failed)")
        fold_freq = edge_recurrence(fold_results).set_index(["from", "to"])["adjacency_rate"]

        for outcome in MAIN_OUTCOMES:
            baseline_cols = BASELINE_FEATURES[outcome]
            for threshold in thresholds:
                selected_base = [frm for (frm, to) in fold_freq.index
                                  if to == outcome and fold_freq[(frm, to)] >= threshold]
                added_cols = [COLUMN_FOR_BASE.get(p, p) for p in selected_base
                              if COLUMN_FOR_BASE.get(p, p) not in baseline_cols]
                feature_cols = baseline_cols + added_cols

                model = LinearRegression()
                model.fit(train_df[feature_cols].to_numpy(dtype=float), train_df[outcome].to_numpy(dtype=float))
                pred = model.predict(test_df[feature_cols].to_numpy(dtype=float))

                per_outcome[outcome][threshold]["r2s"].append(r2_score(test_df[outcome].to_numpy(dtype=float), pred))
                per_outcome[outcome][threshold]["maes"].append(
                    mean_absolute_error(test_df[outcome].to_numpy(dtype=float), pred))
                per_outcome[outcome][threshold]["added_per_fold"].append(added_cols)

    results = {}
    for outcome in MAIN_OUTCOMES:
        results[outcome] = {"base_seed": base_seed, "fold_diagnostics": fold_diagnostics, "by_threshold": {}}
        for threshold in thresholds:
            r2s = per_outcome[outcome][threshold]["r2s"]
            maes = per_outcome[outcome][threshold]["maes"]
            added_per_fold = per_outcome[outcome][threshold]["added_per_fold"]
            n_folds = len(r2s)

            counts = {}
            for added in added_per_fold:
                for p in added:
                    counts[p] = counts.get(p, 0) + 1
            if counts:
                selection_note = "selected per fold beyond baseline: " + ", ".join(
                    f"{p} ({c}/{n_folds} folds)" for p, c in sorted(counts.items(), key=lambda kv: -kv[1]))
            else:
                selection_note = "no additional predictor cleared this threshold in any fold"

            results[outcome]["by_threshold"][threshold] = {
                "features": BASELINE_FEATURES[outcome],
                "per_fold_added": added_per_fold,
                "n_splits_used": n_folds,
                "note": selection_note,
                "r2_mean": float(np.mean(r2s)), "r2_std": float(np.std(r2s)),
                "mae_mean": float(np.mean(maes)), "mae_std": float(np.std(maes)),
            }
    return results


def run_comparison(version: str) -> dict:
    df = load_continuous(version)
    folds = list(GroupKFold(n_splits=N_SPLITS).split(np.zeros(len(df)), groups=df["topic"].to_numpy()))

    results = {}
    for outcome in MAIN_OUTCOMES:
        all_t1 = [p for p in CONTINUOUS_PREDICTORS]
        all_t1_no_modularity = [p for p in all_t1 if p != "modularity_t1"]
        baseline_features = BASELINE_FEATURES[outcome]
        baseline_label = "persistence + year" if outcome == "topic_share_t" else "year only"

        results[outcome] = {
            "baseline": {"label": baseline_label, "features": baseline_features,
                         **_cv_scores(df, baseline_features, outcome, LinearRegression(), folds)},
            "all_t1": {"label": "all main t-1 predictors + year", "features": all_t1,
                       **_cv_scores(df, all_t1, outcome, LinearRegression(), folds)},
            "all_t1_no_modularity": {
                "label": "all_t1 minus modularity_t1 (size-confound check, see sensitivity_size_control)",
                "features": all_t1_no_modularity,
                **_cv_scores(df, all_t1_no_modularity, outcome, LinearRegression(), folds)},
        }

    nested = nested_graph_parents(df, folds, N_BOOT_PER_FOLD, NESTED_SEED)
    for outcome in MAIN_OUTCOMES:
        results[outcome]["graph_parents_nested_cv"] = nested[outcome]

    robustness = threshold_robustness(df, folds, N_BOOT_PER_FOLD, NESTED_SEED, ROBUSTNESS_THRESHOLDS)
    for outcome in MAIN_OUTCOMES:
        results[outcome]["threshold_robustness"] = robustness[outcome]

    return results


def main(version: str = "v5"):
    results = run_comparison(version)
    report = render_report(version, results, N_SPLITS, GRAPH_PARENT_THRESHOLD, N_BOOT_PER_FOLD,
                            ROBUSTNESS_THRESHOLDS)
    out_path = _report_out(version)
    out_path.write_text(report, encoding="utf-8")

    nested_out = _nested_cv_path(version)
    nested_out.write_text(json.dumps(results, indent=2, default=str), encoding="utf-8")

    print(f"[{version}] Wrote {out_path}")
    print(f"[{version}] Wrote {nested_out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=list(DATASETS.keys()), default="v5")
    args = parser.parse_args()
    main(args.version)
