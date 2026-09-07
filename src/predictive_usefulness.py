import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupKFold

from constraints import EXOGENOUS, MAIN_OUTCOMES
from data_prep import DATASETS
from pc_learning import CONNECTIVITY_LOG_VARIANT, CONTINUOUS_PREDICTORS, edge_recurrence, load_continuous
from predictive_usefulness_report import render_report

ROOT = Path(__file__).resolve().parent.parent

N_SPLITS = 5
GRAPH_PARENT_THRESHOLD = 0.5

COLUMN_FOR_BASE = {"connectivity_t1": CONNECTIVITY_LOG_VARIANT}

PERSISTENCE_BASELINE = {"topic_share_t": "topic_share_t1"}


def _suffix(version: str) -> str:
    return "" if version == "v4" else f"_{version}"


def _report_out(version: str) -> Path:
    return ROOT / "reports" / f"predictive_usefulness{_suffix(version)}.md"


def _bootstrap_runs_path(version: str) -> Path:
    return ROOT / "reports" / "pc_runs" / f"bootstrap_runs{_suffix(version)}.json"


def graph_selected_parents(version: str) -> dict:
    path = _bootstrap_runs_path(version)
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found -- run `python src/bootstrap_stability.py "
            f"--version {version} --n-boot 500 --seed 0` first."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    cont_freq = edge_recurrence(data["continuous"]).set_index(["from", "to"])["adjacency_rate"]
    disc_freq = edge_recurrence(data["discretized"]).set_index(["from", "to"])["adjacency_rate"]
    mean_freq = pd.concat([cont_freq, disc_freq], axis=1).mean(axis=1)

    parents = {}
    for outcome in MAIN_OUTCOMES:
        selected = [frm for (frm, to), rate in mean_freq.items() if to == outcome and rate >= GRAPH_PARENT_THRESHOLD]
        parents[outcome] = [COLUMN_FOR_BASE.get(p, p) for p in selected]
    return parents


def _cv_scores(df: pd.DataFrame, features: list, target: str, model) -> dict:
    X = df[features].to_numpy(dtype=float) if features else np.zeros((len(df), 0))
    y = df[target].to_numpy(dtype=float)
    groups = df["topic"].to_numpy()
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

    gkf = GroupKFold(n_splits=N_SPLITS)
    r2s, maes = [], []
    for train_idx, test_idx in gkf.split(X, y, groups):
        model.fit(X[train_idx], y[train_idx])
        pred = model.predict(X[test_idx])
        r2s.append(r2_score(y[test_idx], pred))
        maes.append(mean_absolute_error(y[test_idx], pred))

    return {
        "n_splits_used": N_SPLITS, "note": "",
        "r2_mean": float(np.mean(r2s)), "r2_std": float(np.std(r2s)),
        "mae_mean": float(np.mean(maes)), "mae_std": float(np.std(maes)),
    }


def run_comparison(version: str) -> dict:
    df = load_continuous(version)
    parents = graph_selected_parents(version)

    results = {}
    for outcome in MAIN_OUTCOMES:
        all_t1 = [p for p in CONTINUOUS_PREDICTORS]
        all_t1_no_modularity = [p for p in all_t1 if p != "modularity_t1"]
        graph_parents = parents.get(outcome, [])

        if outcome in PERSISTENCE_BASELINE:
            baseline_features = [PERSISTENCE_BASELINE[outcome]]
            baseline_model = LinearRegression()
            baseline_label = f"persistence ({PERSISTENCE_BASELINE[outcome]} only)"
        else:
            baseline_features = []
            baseline_model = DummyRegressor(strategy="mean")
            baseline_label = "intercept-only (mean)"

        results[outcome] = {
            "baseline": {"label": baseline_label, "features": baseline_features,
                         **_cv_scores(df, baseline_features, outcome, baseline_model)},
            "all_t1": {"label": "all main t-1 predictors + year", "features": all_t1,
                       **_cv_scores(df, all_t1, outcome, LinearRegression())},
            "all_t1_no_modularity": {
                "label": "all_t1 minus modularity_t1 (size-confound check, see sensitivity_size_control)",
                "features": all_t1_no_modularity,
                **_cv_scores(df, all_t1_no_modularity, outcome, LinearRegression())},
            "graph_parents": {"label": f"graph-selected parents (mean bootstrap adjacency >= {GRAPH_PARENT_THRESHOLD})",
                               "features": graph_parents,
                               **(_cv_scores(df, graph_parents, outcome, LinearRegression())
                                  if graph_parents else
                                  {"n_splits_used": 0, "note": "no predictor cleared the threshold",
                                   "r2_mean": float("nan"), "r2_std": float("nan"),
                                   "mae_mean": float("nan"), "mae_std": float("nan")})},
        }
    return results


def main(version: str = "v4"):
    results = run_comparison(version)
    report = render_report(version, results, N_SPLITS, GRAPH_PARENT_THRESHOLD)
    out_path = _report_out(version)
    out_path.write_text(report, encoding="utf-8")
    print(f"[{version}] Wrote {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=list(DATASETS.keys()), default="v4")
    args = parser.parse_args()
    main(args.version)
