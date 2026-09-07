def render_report(version: str, results: dict, n_splits: int, graph_parent_threshold: float) -> str:
    lines = [f"# Predictive Usefulness -- Step 5 / thesis D2.3 ({version})\n"]
    lines.append(
        f"Topic-grouped cross-validation (GroupKFold, k={n_splits}, grouped by "
        "`topic`) comparing four linear models per outcome. Grouped rather "
        "than plain K-fold because rows are repeated topic-year measurements "
        "-- a random split could put the same topic's rows in both train and "
        "test, leaking topic-level persistence into the score (same concern "
        "as `bootstrap_stability.py`'s topic-block resampling).\n"
        "\n"
        "`graph_parents` is derived directly from Step 4's bootstrap "
        "results: a predictor counts as a parent if its mean (continuous + "
        "discretized) bootstrap adjacency rate into that outcome is >= "
        f"{graph_parent_threshold}. This is a documented, recomputable "
        "threshold, not a hand-picked edge list, and is a first look at "
        "what a Step 5 stable-edge graph would contain.\n"
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

    for outcome, models in results.items():
        lines.append(f"## {outcome}\n")
        lines.append("```")
        header = f"{'model':<20} {'features':<55} {'R2 (mean+/-std)':<20} {'MAE (mean+/-std)':<20}"
        lines.append(header)
        for key in ["baseline", "all_t1", "all_t1_no_modularity", "graph_parents"]:
            m = models[key]
            feat_str = ", ".join(m["features"]) if m["features"] else "(none)"
            if len(feat_str) > 53:
                feat_str = feat_str[:50] + "..."
            if m["n_splits_used"] == 0:
                r2_str, mae_str = "n/a", "n/a"
            else:
                r2_str = f"{m['r2_mean']:.3f}+/-{m['r2_std']:.3f}"
                mae_str = f"{m['mae_mean']:.3f}+/-{m['mae_std']:.3f}"
            lines.append(f"{key:<20} {feat_str:<55} {r2_str:<20} {mae_str:<20}")
        lines.append("```")
        for key in ["baseline", "all_t1", "all_t1_no_modularity", "graph_parents"]:
            m = models[key]
            if m.get("note"):
                lines.append(f"- `{key}` ({m['label']}): {m['note']}")
        lines.append("")

    return "\n".join(lines)
