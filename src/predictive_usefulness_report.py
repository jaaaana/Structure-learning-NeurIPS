def render_report(version: str, results: dict, n_splits: int, graph_parent_threshold: float,
                   n_boot_per_fold: int) -> str:
    lines = [f"# Predictive Usefulness -- Step 5 / thesis D2.3 ({version})\n"]
    lines.append(
        f"Topic-grouped cross-validation (GroupKFold, k={n_splits}, grouped by "
        "`topic`) comparing four linear models per outcome, using the exact "
        "same fold split for all four so every model is scored on identical "
        "held-out topics. Grouped rather than plain K-fold because rows are "
        "repeated topic-year measurements -- a random split could put the "
        "same topic's rows in both train and test, leaking topic-level "
        "persistence into the score (same concern as "
        "`bootstrap_stability.py`'s topic-block resampling).\n"
        "\n"
        "`baseline` is the minimal, non-graph comparison per outcome: "
        "`year` only for `log1p_median_c2`, `topic_share_t1` + `year` for "
        "`topic_share_t`. `graph_parents_nested_cv` is always `baseline`'s "
        "own features plus zero or more additional predictors -- **selected "
        "separately inside each fold, using only that fold's training "
        f"topics** ({n_boot_per_fold} bootstrap replicates per fold, "
        "continuous/Fisher-Z, adjacency threshold "
        f">= {graph_parent_threshold}), never using the held-out fold's "
        "topics for selection the way a single full-dataset bootstrap would. "
        "Because its features are always a superset of `baseline`'s, an "
        "improvement over `baseline` cleanly means the added predictors "
        "carry predictive information beyond it, not that an unrelated "
        "feature set happened to score higher. **This is a predictive-value "
        "claim only**: if `graph_parents_nested_cv` outperforms `baseline`, "
        "that shows the selected social/network predictors add knowledge "
        "beyond the simple temporal effects already in `baseline` -- it does "
        "not show those predictors are proven causal, which would require "
        "the PC/bootstrap stability evidence above, not this comparison. "
        "This threshold is kept "
        "numerically identical to the frozen main model's bootstrap "
        "threshold for interpretability, even though its statistical "
        "meaning differs here (fewer topics per fold, far fewer replicates "
        "than the main 500-replicate full-dataset bootstrap) -- not "
        "presented as directly comparable to that number. "
        "`graph_parents_nested_cv` is a different statistic from any "
        "`stable`/`candidate` tier in `final_team_deliverable" +
        ("" if version == "v4" else f"_{version}") +
        ".md` (which uses the full-dataset, both-representations bootstrap), "
        "not the same one restated.\n"
        "\n"
        "`all_t1_no_modularity` is `all_t1` with `modularity_t1` dropped -- "
        "added after `pc_learning.py`'s `sensitivity_size_control` group "
        "showed every `modularity_t1 -> outcome` edge in the main model "
        "disappears once topic size (`n_papers_t1`) is controllable, "
        "replaced by `n_papers_t1 -> modularity_t1`. This checks how much "
        "of `all_t1`'s predictive gain over baseline was actually riding on "
        "that now-refuted predictor, without changing the original "
        "`all_t1` row above it.\n"
    )

    model_keys = ["baseline", "all_t1", "all_t1_no_modularity", "graph_parents_nested_cv"]
    for outcome, models in results.items():
        lines.append(f"## {outcome}\n")
        lines.append("```")
        header = f"{'model':<24} {'features':<50} {'R2 (mean+/-std)':<20} {'MAE (mean+/-std)':<20}"
        lines.append(header)
        for key in model_keys:
            m = models[key]
            feat_str = ", ".join(m["features"]) if m["features"] else "(none)"
            if len(feat_str) > 48:
                feat_str = feat_str[:45] + "..."
            if m["n_splits_used"] == 0:
                r2_str, mae_str = "n/a", "n/a"
            else:
                r2_str = f"{m['r2_mean']:.3f}+/-{m['r2_std']:.3f}"
                mae_str = f"{m['mae_mean']:.3f}+/-{m['mae_std']:.3f}"
            lines.append(f"{key:<24} {feat_str:<50} {r2_str:<20} {mae_str:<20}")
        lines.append("```")
        for key in model_keys:
            m = models[key]
            if m.get("note"):
                lines.append(f"- `{key}` ({m['label']}): {m['note']}")
        lines.append("")

    return "\n".join(lines)
