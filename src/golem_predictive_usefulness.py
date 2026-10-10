"""Leakage-free predictive evaluation using GOLEM-selected graph parents."""
import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold

from constraints import MAIN_OUTCOMES
from data_prep import DATASETS
from golem_learning import graph_result
from golem_model import FitConfig, fit_many
from pc_bootstrap_stability import _is_degenerate, resample_topics
from pc_learning import CONTINUOUS_OUTCOMES, CONTINUOUS_PREDICTORS, load_continuous
from golem_predictive_usefulness_report import render_report

ROOT = Path(__file__).resolve().parent.parent
N_SPLITS = 5
N_BOOT_PER_FOLD = 150
NESTED_SEED = 0
GRAPH_THRESHOLD = 0.10
SELECTION_THRESHOLD = 0.50
ROBUSTNESS_THRESHOLDS = [0.30, 0.50, 0.70]
BASELINE_FEATURES = {"topic_share_t": ["topic_share_t1", "year"],
                     "log1p_median_c2": ["year"]}


def _suffix(version):
    return "" if version == "v4" else f"_{version}"


def _scores(df, features, outcome, folds):
    x = df[features].to_numpy(dtype=float)
    y = df[outcome].to_numpy(dtype=float)
    r2s, maes = [], []
    for train_idx, test_idx in folds:
        model = LinearRegression().fit(x[train_idx], y[train_idx])
        pred = model.predict(x[test_idx])
        r2s.append(r2_score(y[test_idx], pred))
        maes.append(mean_absolute_error(y[test_idx], pred))
    return {"n_splits_used": len(folds), "r2_mean": float(np.mean(r2s)),
            "r2_std": float(np.std(r2s)), "mae_mean": float(np.mean(maes)),
            "mae_std": float(np.std(maes))}


def _fit_bootstrap_fold(df, names, n_boot, seed, config, threshold, batch_size):
    groups = {topic: group for topic, group in df.groupby("topic")}
    topics = df["topic"].unique()
    rng = np.random.default_rng(seed)
    records = []
    categories = None
    for start in range(0, n_boot, batch_size):
        pending, frames, positions = [], [], []
        for replicate in range(start, min(start + batch_size, n_boot)):
            sample = resample_topics(groups, topics, rng)
            base = {"replicate": replicate, "n_rows": len(sample)}
            if _is_degenerate(sample, names):
                pending.append(dict(base, status="degenerate", directed_edges=[], undirected_edges=[]))
            else:
                positions.append(len(pending))
                pending.append(base)
                frames.append(sample)
        if frames:
            try:
                fits = fit_many(frames, names, "continuous", True, config, categories)
            except (ValueError, RuntimeError, FloatingPointError, np.linalg.LinAlgError):
                fits = []
                for frame in frames:
                    try:
                        fits.append(fit_many([frame], names, "continuous", True, config, categories)[0])
                    except (ValueError, RuntimeError, FloatingPointError, np.linalg.LinAlgError) as exc:
                        fits.append({"status": "failed", "strengths": None,
                                     "failure_reason": str(exc), "node_names": names,
                                     "n_rows": len(frame)})
            for pos, fit in zip(positions, fits):
                pending[pos].update(graph_result(fit, threshold, "main"))
        records.extend(pending)
    successful = [r for r in records if r["status"] == "converged"]
    diag = {"n_boot_requested": n_boot, "n_completed": len(records),
            "n_succeeded": len(successful),
            "n_nonconverged": sum(r["status"] == "nonconverged" for r in records),
            "n_failed": sum(r["status"] == "failed" for r in records),
            "n_degenerate_skipped": sum(r["status"] == "degenerate" for r in records),
            "n_train_topics": int(df["topic"].nunique())}
    return successful, diag


def _directional_parent_rates(records, outcomes):
    counts = {}
    for record in records:
        seen = set()
        for src, dst in record.get("directed_edges", []):
            if dst not in outcomes:
                continue
            pair = (src, dst)
            if pair not in seen:
                counts[pair] = counts.get(pair, 0) + 1
                seen.add(pair)
    n = len(records)
    return {pair: count / n for pair, count in counts.items()} if n else {}


def _added_features(rates, outcome, threshold):
    base = BASELINE_FEATURES[outcome]
    return sorted(src for (src, dst), rate in rates.items()
                  if dst == outcome and rate >= threshold and src not in base)


def run_comparison(version, n_boot=N_BOOT_PER_FOLD, seed=NESTED_SEED,
                   batch_size=25, graph_threshold=GRAPH_THRESHOLD,
                   selection_threshold=SELECTION_THRESHOLD,
                   robustness_thresholds=ROBUSTNESS_THRESHOLDS,
                   config=FitConfig(lambda1=0.02)):
    df = load_continuous(version)
    folds = list(GroupKFold(n_splits=N_SPLITS).split(
        np.zeros(len(df)), groups=df["topic"].to_numpy()))
    names = CONTINUOUS_PREDICTORS + CONTINUOUS_OUTCOMES
    all_predictors = list(CONTINUOUS_PREDICTORS)
    all_without_modularity = [p for p in all_predictors if p != "modularity_t1"]

    results = {}
    for outcome in MAIN_OUTCOMES:
        baseline = BASELINE_FEATURES[outcome]
        results[outcome] = {
            "baseline": {"features": baseline, **_scores(df, baseline, outcome, folds)},
            "all_t1": {"features": all_predictors, **_scores(df, all_predictors, outcome, folds)},
            "all_t1_no_modularity": {"features": all_without_modularity,
                                     **_scores(df, all_without_modularity, outcome, folds)},
        }

    per_fold = []
    nested_scores = {o: {"r2": [], "mae": [], "added": []} for o in MAIN_OUTCOMES}
    threshold_scores = {o: {t: {"r2": [], "mae": [], "added": []}
                            for t in robustness_thresholds} for o in MAIN_OUTCOMES}
    for fold_idx, (train_idx, test_idx) in enumerate(folds):
        train_df, test_df = df.iloc[train_idx], df.iloc[test_idx]
        successful, diag = _fit_bootstrap_fold(
            train_df, names, n_boot, seed + fold_idx, config, graph_threshold, batch_size)
        rates = _directional_parent_rates(successful, set(MAIN_OUTCOMES))
        fold_payload = {"fold": fold_idx, "diagnostics": diag,
                        "directional_parent_rates": [
                            {"source": a, "outcome": b, "rate": rate}
                            for (a, b), rate in sorted(rates.items())]}
        for outcome in MAIN_OUTCOMES:
            baseline = BASELINE_FEATURES[outcome]
            added = _added_features(rates, outcome, selection_threshold)
            features = baseline + added
            model = LinearRegression().fit(train_df[features].to_numpy(dtype=float),
                                           train_df[outcome].to_numpy(dtype=float))
            pred = model.predict(test_df[features].to_numpy(dtype=float))
            nested_scores[outcome]["r2"].append(r2_score(test_df[outcome], pred))
            nested_scores[outcome]["mae"].append(mean_absolute_error(test_df[outcome], pred))
            nested_scores[outcome]["added"].append(added)
            fold_payload.setdefault("selected", {})[outcome] = added
            for threshold in robustness_thresholds:
                threshold_added = _added_features(rates, outcome, threshold)
                threshold_features = baseline + threshold_added
                threshold_model = LinearRegression().fit(
                    train_df[threshold_features].to_numpy(dtype=float),
                    train_df[outcome].to_numpy(dtype=float))
                threshold_pred = threshold_model.predict(
                    test_df[threshold_features].to_numpy(dtype=float))
                threshold_scores[outcome][threshold]["r2"].append(
                    r2_score(test_df[outcome], threshold_pred))
                threshold_scores[outcome][threshold]["mae"].append(
                    mean_absolute_error(test_df[outcome], threshold_pred))
                threshold_scores[outcome][threshold]["added"].append(threshold_added)
        per_fold.append(fold_payload)
        print(f"fold {fold_idx}: {diag['n_succeeded']}/{n_boot} converged GOLEM bootstrap fits",
              flush=True)

    for outcome in MAIN_OUTCOMES:
        nested = nested_scores[outcome]
        added_counts = {}
        for selected in nested["added"]:
            for feature in selected:
                added_counts[feature] = added_counts.get(feature, 0) + 1
        results[outcome]["golem_parents_nested_cv"] = {
            "features": BASELINE_FEATURES[outcome],
            "selection_note": (", ".join(f"{p} ({n}/{len(folds)} folds)"
                                           for p, n in sorted(added_counts.items()))
                               if added_counts else "no additional predictor cleared the threshold"),
            "per_fold_added": nested["added"], "n_splits_used": len(folds),
            "r2_mean": float(np.mean(nested["r2"])), "r2_std": float(np.std(nested["r2"])),
            "mae_mean": float(np.mean(nested["mae"])), "mae_std": float(np.std(nested["mae"])),
        }
        results[outcome]["threshold_robustness"] = {
            str(t): {"per_fold_added": threshold_scores[outcome][t]["added"],
                     "r2_mean": float(np.mean(threshold_scores[outcome][t]["r2"])),
                     "r2_std": float(np.std(threshold_scores[outcome][t]["r2"])),
                     "mae_mean": float(np.mean(threshold_scores[outcome][t]["mae"])),
                     "mae_std": float(np.std(threshold_scores[outcome][t]["mae"]))}
            for t in robustness_thresholds}
    return {"version": version, "settings": {"n_splits": N_SPLITS, "n_boot_per_fold": n_boot,
            "seed": seed, "batch_size": batch_size, "lambda1": config.lambda1,
            "lambda_dag": config.lambda_dag, "tolerance": config.tolerance,
            "max_iter": config.max_iter,
            "graph_threshold": graph_threshold, "selection_threshold": selection_threshold,
            "robustness_thresholds": robustness_thresholds,
            "baseline_features": BASELINE_FEATURES},
            "folds": per_fold, "outcomes": results}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", choices=list(DATASETS), default="v5")
    parser.add_argument("--n-boot-per-fold", type=int, default=N_BOOT_PER_FOLD)
    parser.add_argument("--seed", type=int, default=NESTED_SEED)
    parser.add_argument("--batch-size", type=int, default=25)
    parser.add_argument("--selection-threshold", type=float, default=SELECTION_THRESHOLD)
    args = parser.parse_args()
    if args.n_boot_per_fold < 1 or args.batch_size < 1:
        parser.error("bootstrap counts and batch size must be positive")
    if not np.isfinite(args.selection_threshold) or not 0 <= args.selection_threshold <= 1:
        parser.error("selection threshold must be between 0 and 1")
    payload = run_comparison(args.version, n_boot=args.n_boot_per_fold, seed=args.seed,
                             batch_size=args.batch_size,
                             selection_threshold=args.selection_threshold)
    out_json = ROOT / "reports" / "golem_runs" / f"golem_predictive_nested_cv{_suffix(args.version)}.json"
    out_md = ROOT / "reports" / f"golem_predictive_usefulness{_suffix(args.version)}.md"
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    out_md.write_text(render_report(payload), encoding="utf-8")
    print(f"Wrote {out_md}")
    print(f"Wrote {out_json}")


if __name__ == "__main__":
    main()
