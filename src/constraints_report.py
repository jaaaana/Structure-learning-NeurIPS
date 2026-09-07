def render_report(data: dict, exogenous: list, tier_0: list, tier_1: list,
                   tier_1_log_variant: str, main_predictors: list, main_outcomes: list,
                   sensitivity_predictors_only: list, sensitivity_outcomes_only: list,
                   size_vars: list) -> str:
    lines = []
    lines.append("# Edge Constraints -- Step 2\n")
    lines.append(
        "Formal forbidden/allowed/sensitivity edge lists for the PC runs in "
        "Step 3, per the temporal rule: edges from t (outcomes) "
        "back to t-1 (predictors) are forbidden; the main allowed direction "
        "is t-1 -> t.\n"
    )

    lines.append("## Temporal tiers\n")
    lines.append(f"- Tier 0 (exogenous, context): {', '.join(exogenous)}")
    lines.append(f"- Tier 1 (predictors, t-1): {', '.join(tier_0)}")
    lines.append(f"- Tier 2 (outcomes, t): {', '.join(tier_1)}")
    lines.append(
        f"- Note: `{tier_1_log_variant}` is `median_cites_2yr` log1p-transformed "
        "for continuous CI tests -- same tier, same underlying variable, "
        "never include both in one PC run."
    )
    lines.append(
        "- `year` (tier 0) is exogenous: it may point at anything, but "
        "nothing may point into it -- added per the 2026-08-19 "
        "correction, since several variables share a calendar-time trend "
        "and an unconstrained year node could otherwise absorb spurious "
        "edges.\n"
    )

    lines.append("## Main model vs. sensitivity-only variables\n")
    lines.append(
        f"Per the 2026-08-19 correction, the **main PC model** "
        f"uses predictors {', '.join(main_predictors)} (+ `year`) and "
        f"outcomes {', '.join(main_outcomes)}. "
        f"`{', '.join(sensitivity_predictors_only)}` is a sensitivity-only "
        f"predictor and `{', '.join(sensitivity_outcomes_only)}` are "
        "sensitivity-only outcomes -- all still temporally tiered the same "
        "way above, just excluded from the main Step 3 grid.\n"
    )

    lines.append("## Forbidden edges (hard rule, always applied)\n")
    lines.append(
        f"All {len(data['forbidden_edges'])} outcome-to-predictor edges "
        "(t -> t-1). Example: `median_cites_2yr -> connectivity_t1` is "
        "forbidden.\n"
    )
    lines.append("```")
    for src, dst in data["forbidden_edges"]:
        lines.append(f"{src} -> {dst}  [FORBIDDEN]")
    lines.append("```\n")

    lines.append("## Allowed edges (main model search space)\n")
    lines.append(
        f"All {len(data['allowed_edges_main_model'])} predictor-to-outcome "
        "edges (t-1 -> t). This is the space PC is permitted to place edges "
        "in for the main model -- it is not a guarantee any specific edge "
        "will be learned, that's for Step 3 to determine from data.\n"
    )
    lines.append("```")
    for src, dst in data["allowed_edges_main_model"]:
        lines.append(f"{src} -> {dst}  [allowed]")
    lines.append("```\n")

    lines.append("## Sensitivity-only edges (excluded from main model)\n")
    lines.append(
        "### Outcome-outcome (t -> t), explicitly specified\n"
    )
    lines.append(
        "Example given: `TopicGrowth_t -> HitRate2yr_t`. These are excluded "
        "from the main model and only explored as a separate sensitivity "
        "setting in Step 4.\n"
    )
    lines.append("```")
    for src, dst in data["sensitivity_edges"]["outcome_outcome_t"]:
        lines.append(f"{src} -> {dst}  [sensitivity only]")
    lines.append("```\n")

    lines.append(
        "### Predictor-predictor (t-1 -> t-1), interpretive extension\n"
    )
    lines.append(
        "Not explicitly specified, but treated "
        "the same way as outcome-outcome edges here: both tiers are "
        "contemporaneous internally, so within-tier edges have no temporal "
        "basis for the main model, only a correlational one. Flagged "
        "explicitly as an interpretive choice, available as an additional "
        "Step 4 sensitivity setting if useful (e.g. checking whether "
        "`topic_share_t1` and `modularity_t1`, r=0.43 in the Step 1 "
        "correlation analysis, should be modeled as connected).\n"
    )
    lines.append("```")
    for src, dst in data["sensitivity_edges"]["predictor_predictor_t1"]:
        lines.append(f"{src} -> {dst}  [sensitivity only]")
    lines.append("```\n")

    lines.append("## Notes for downstream steps\n")
    lines.append(
        "- These constraints are purely temporal. They say nothing about "
        "variable quality -- `bridge_concentration_t1`'s near-degeneracy and "
        "`modularity_t1`'s confound with topic size (Step 1 findings) still "
        "apply and are handled separately (which predictor subset a given "
        "PC setting uses), not by this module.\n"
    )
    lines.append(
        f"- `build_background_knowledge(..., size_vars={size_vars})` builds an "
        "optional 4th tier for `n_papers_t1`, inserted below the regular "
        "predictors so it can enter `modularity_t1`'s conditioning set "
        "(forbid_within_tier would otherwise block a same-tier variable from "
        "ever doing that, regardless of correlation -- see the SIZE_VARS "
        "comment in this module). Used only by `pc_learning.py`'s "
        "`sensitivity_size_control` group, not the main model; see "
        "`pc_settings_comparison.md` for results.\n"
    )
    lines.append(
        "- JSON export (`edge_constraints.json`) mirrors the schema already "
        "used in the team's `dag_constraints.json` (`forbidden_edges` + "
        "`temporal_tiers`), so the LLM-guided/hybrid parts of the project "
        "can consume it directly.\n"
    )
    lines.append(
        "- `build_background_knowledge()` is directly reusable in Step 3: "
        "pass it the exact `node_names` list for a given PC run and it "
        "assigns tiers only to the variables present, so it works "
        "unmodified across the continuous/discretized settings and "
        "different citation-outcome choices.\n"
    )

    return "\n".join(lines)
