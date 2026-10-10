import sys
from pathlib import Path as _Path
_SRC_ROOT = str(_Path(__file__).resolve().parents[1])
if _SRC_ROOT not in sys.path:
    sys.path.insert(0, _SRC_ROOT)
"""Markdown report rendering for GOLEM predictive-usefulness results."""

import argparse
import json
from pathlib import Path

from data_prep import DATASETS

ROOT = Path(__file__).resolve().parents[2]


def render_report(payload):
    settings = payload["settings"]
    seed_start = settings["seed"]
    seed_end = seed_start + settings["n_splits"] - 1
    lines = [f"# GOLEM Predictive Usefulness ({payload['version']})\n",
             f"Five-fold topic-grouped cross-validation. Predictor selection uses training topics only "
             f"({settings['n_boot_per_fold']} bootstrap fits per fold; lambda1={settings['lambda1']}; "
             f"lambda_dag={settings.get('lambda_dag', 5.0)}; "
             f"tolerance={settings.get('tolerance', 1e-6)}; max_iter={settings.get('max_iter', 10000)}; "
             f"edge threshold={settings['graph_threshold']}; "
             f"selection frequency threshold={settings['selection_threshold']}). "
             "Only converged fits count toward selection.\n",
             "All models use the same five GroupKFold splits, grouped by topic. This keeps each topic's "
             "yearly rows together and prevents a topic from appearing in both training and held-out data.\n",
             "`baseline` is the non-graph comparison: `topic_share_t ~ topic_share_t1 + year` and "
             "`log1p_median_c2 ~ year`. `golem_parents_nested_cv` keeps those baseline features and adds "
             "GOLEM-selected parents, selected separately in each training fold using topic-block bootstrap "
             f"resamples ({settings['n_boot_per_fold']} fits per fold; base seed {seed_start}; "
             f"fold seeds {seed_start}..{seed_end}). The held-out fold is not used for selection. "
             "An improvement over baseline therefore measures the added predictors' value beyond the "
             "baseline features.\n",
             "`all_t1` and `all_t1_no_modularity` are fixed-feature benchmarks; the latter omits the "
             "size-associated `modularity_t1` to show whether performance depends on that feature. "
             "These scores measure predictive usefulness, not causal effects.\n"]
    for outcome, models in payload["outcomes"].items():
        lines += [f"## {outcome}\n", "```\n",
                  "model                    features                                           R2 (mean+/-std)      MAE (mean+/-std)\n",
                  "------------------------ -------------------------------------------------- ------------------- -------------------\n"]
        for key in ("baseline", "all_t1", "all_t1_no_modularity", "golem_parents_nested_cv"):
            row = models[key]
            features = ", ".join(row["features"])
            if len(features) > 48:
                features = features[:45] + "..."
            lines.append(f"{key:24} {features:50} "
                         f"{row['r2_mean']:.3f}+/-{row['r2_std']:.3f}        "
                         f"{row['mae_mean']:.3f}+/-{row['mae_std']:.3f}\n")
        lines += ["```\n",
                  f"- `golem_parents_nested_cv` (baseline features + graph-selected predictors, nested per-fold "
                  f"bootstrap ({settings['n_boot_per_fold']} reps/fold, threshold="
                  f"{settings['selection_threshold']})): "
                  f"{models['golem_parents_nested_cv']['selection_note']}\n",
                  f"\n### {outcome}: predictor-selection threshold robustness\n",
                  "Each fold's training-only bootstrap frequency table is computed once and reused for every "
                  "threshold shown here. Baseline features are retained; this checks sensitivity to the "
                  "selection cutoff rather than choosing the best-scoring cutoff.\n\n",
                  "```\n",
                  "threshold   R2 (mean+/-std)      MAE (mean+/-std)\n",
                  "---------   -------------------  -------------------\n"]
        threshold_items = sorted(models["threshold_robustness"].items(),
                                  key=lambda item: float(item[0]))
        for threshold, row in threshold_items:
            lines.append(f"{float(threshold):<11.2f} {row['r2_mean']:.3f}+/-{row['r2_std']:.3f}        "
                         f"{row['mae_mean']:.3f}+/-{row['mae_std']:.3f}\n")
        for anchor in ("baseline", "all_t1"):
            row = models[anchor]
            lines.append(f"({anchor})     {row['r2_mean']:.3f}+/-{row['r2_std']:.3f}        "
                         f"{row['mae_mean']:.3f}+/-{row['mae_std']:.3f}\n")
        lines.append("```\n")
        for threshold, row in threshold_items:
            additions = {}
            for fold_additions in row["per_fold_added"]:
                for predictor in fold_additions:
                    additions[predictor] = additions.get(predictor, 0) + 1
            selected = ", ".join(f"{name} ({count}/5 folds)"
                                  for name, count in additions.items())
            note = (f"selected per fold beyond baseline: {selected}" if selected else
                    "no additional predictor cleared this threshold in any fold")
            lines.append(f"- threshold={float(threshold):.2f}: {note}\n")

        r2_values = [row["r2_mean"] for _, row in threshold_items]
        spread = max(r2_values) - min(r2_values) if r2_values else 0.0
        baseline_gap = abs(models["baseline"]["r2_mean"] - models["all_t1"]["r2_mean"])
        thresholds = [float(t) for t, _ in threshold_items]
        lo, hi = min(thresholds), max(thresholds)
        if baseline_gap > 0 and spread < 0.25 * baseline_gap:
            verdict = (f"R2 varies by only {spread:.3f} across thresholds {lo:.2f}-{hi:.2f}, "
                       f"small relative to the {baseline_gap:.3f} baseline-to-all_t1 gap; the "
                       "predictive-usefulness conclusion looks stable to this cutoff choice.")
        else:
            verdict = (f"R2 varies by {spread:.3f} across thresholds {lo:.2f}-{hi:.2f}, not small "
                       f"relative to the {baseline_gap:.3f} baseline-to-all_t1 gap; the conclusion is "
                       "sensitive to the cutoff, so interpret the frozen-threshold result with care.")
        lines.append(f"- **Threshold-dependence check** (informal yardstick, not a statistical test): {verdict}\n")
        lines += ["\n#### GOLEM fit convergence by fold\n",
                  "fold | training topics | converged / requested | nonconverged | failed | degenerate\n",
                  "---: | ---: | ---: | ---: | ---: | ---:\n"]
        for fold in payload["folds"]:
            d = fold["diagnostics"]
            lines.append(f"{fold['fold']} | {d['n_train_topics']} | "
                         f"{d['n_succeeded']}/{d['n_boot_requested']} | {d['n_nonconverged']} | "
                         f"{d['n_failed']} | {d['n_degenerate_skipped']}\n")
        lines.append("\n")
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", choices=list(DATASETS), default="v5")
    args = parser.parse_args()
    suffix = "" if args.version == "v4" else f"_{args.version}"
    source = ROOT / "reports" / "golem" / "runs" / f"predictive_nested_cv{suffix}.json"
    target = ROOT / "reports" / "golem" / f"predictive_usefulness{suffix}.md"
    payload = json.loads(source.read_text(encoding="utf-8"))
    target.write_text(render_report(payload), encoding="utf-8")
    print(f"Wrote {target}")


if __name__ == "__main__":
    main()
