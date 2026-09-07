# Edge Constraints -- Step 2

Formal forbidden/allowed/sensitivity edge lists for the PC runs in Step 3, per the temporal rule: edges from t (outcomes) back to t-1 (predictors) are forbidden; the main allowed direction is t-1 -> t.

## Temporal tiers

- Tier 0 (exogenous, context): year
- Tier 1 (predictors, t-1): topic_share_t1, cross_topic_rate_t1, connectivity_t1, modularity_t1, bridge_concentration_t1
- Tier 2 (outcomes, t): topic_growth, median_cites_2yr, hit_rate_2yr, topic_share_t
- Note: `log1p_median_c2` is `median_cites_2yr` log1p-transformed for continuous CI tests -- same tier, same underlying variable, never include both in one PC run.
- `year` (tier 0) is exogenous: it may point at anything, but nothing may point into it -- added per the 2026-08-19 correction, since several variables share a calendar-time trend and an unconstrained year node could otherwise absorb spurious edges.

## Main model vs. sensitivity-only variables

Per the 2026-08-19 correction, the **main PC model** uses predictors topic_share_t1, cross_topic_rate_t1, connectivity_t1, modularity_t1 (+ `year`) and outcomes topic_share_t, log1p_median_c2. `bridge_concentration_t1` is a sensitivity-only predictor and `topic_growth, hit_rate_2yr` are sensitivity-only outcomes -- all still temporally tiered the same way above, just excluded from the main Step 3 grid.

## Forbidden edges (hard rule, always applied)

All 29 outcome-to-predictor edges (t -> t-1). Example: `median_cites_2yr -> connectivity_t1` is forbidden.

```
topic_growth -> topic_share_t1  [FORBIDDEN]
topic_growth -> cross_topic_rate_t1  [FORBIDDEN]
topic_growth -> connectivity_t1  [FORBIDDEN]
topic_growth -> modularity_t1  [FORBIDDEN]
topic_growth -> bridge_concentration_t1  [FORBIDDEN]
median_cites_2yr -> topic_share_t1  [FORBIDDEN]
median_cites_2yr -> cross_topic_rate_t1  [FORBIDDEN]
median_cites_2yr -> connectivity_t1  [FORBIDDEN]
median_cites_2yr -> modularity_t1  [FORBIDDEN]
median_cites_2yr -> bridge_concentration_t1  [FORBIDDEN]
hit_rate_2yr -> topic_share_t1  [FORBIDDEN]
hit_rate_2yr -> cross_topic_rate_t1  [FORBIDDEN]
hit_rate_2yr -> connectivity_t1  [FORBIDDEN]
hit_rate_2yr -> modularity_t1  [FORBIDDEN]
hit_rate_2yr -> bridge_concentration_t1  [FORBIDDEN]
topic_share_t -> topic_share_t1  [FORBIDDEN]
topic_share_t -> cross_topic_rate_t1  [FORBIDDEN]
topic_share_t -> connectivity_t1  [FORBIDDEN]
topic_share_t -> modularity_t1  [FORBIDDEN]
topic_share_t -> bridge_concentration_t1  [FORBIDDEN]
topic_share_t1 -> year  [FORBIDDEN]
cross_topic_rate_t1 -> year  [FORBIDDEN]
connectivity_t1 -> year  [FORBIDDEN]
modularity_t1 -> year  [FORBIDDEN]
bridge_concentration_t1 -> year  [FORBIDDEN]
topic_growth -> year  [FORBIDDEN]
median_cites_2yr -> year  [FORBIDDEN]
hit_rate_2yr -> year  [FORBIDDEN]
topic_share_t -> year  [FORBIDDEN]
```

## Allowed edges (main model search space)

All 29 predictor-to-outcome edges (t-1 -> t). This is the space PC is permitted to place edges in for the main model -- it is not a guarantee any specific edge will be learned, that's for Step 3 to determine from data.

```
topic_share_t1 -> topic_growth  [allowed]
topic_share_t1 -> median_cites_2yr  [allowed]
topic_share_t1 -> hit_rate_2yr  [allowed]
topic_share_t1 -> topic_share_t  [allowed]
cross_topic_rate_t1 -> topic_growth  [allowed]
cross_topic_rate_t1 -> median_cites_2yr  [allowed]
cross_topic_rate_t1 -> hit_rate_2yr  [allowed]
cross_topic_rate_t1 -> topic_share_t  [allowed]
connectivity_t1 -> topic_growth  [allowed]
connectivity_t1 -> median_cites_2yr  [allowed]
connectivity_t1 -> hit_rate_2yr  [allowed]
connectivity_t1 -> topic_share_t  [allowed]
modularity_t1 -> topic_growth  [allowed]
modularity_t1 -> median_cites_2yr  [allowed]
modularity_t1 -> hit_rate_2yr  [allowed]
modularity_t1 -> topic_share_t  [allowed]
bridge_concentration_t1 -> topic_growth  [allowed]
bridge_concentration_t1 -> median_cites_2yr  [allowed]
bridge_concentration_t1 -> hit_rate_2yr  [allowed]
bridge_concentration_t1 -> topic_share_t  [allowed]
year -> topic_share_t1  [allowed]
year -> cross_topic_rate_t1  [allowed]
year -> connectivity_t1  [allowed]
year -> modularity_t1  [allowed]
year -> bridge_concentration_t1  [allowed]
year -> topic_growth  [allowed]
year -> median_cites_2yr  [allowed]
year -> hit_rate_2yr  [allowed]
year -> topic_share_t  [allowed]
```

## Sensitivity-only edges (excluded from main model)

### Outcome-outcome (t -> t), explicitly specified

Example given: `TopicGrowth_t -> HitRate2yr_t`. These are excluded from the main model and only explored as a separate sensitivity setting in Step 4.

```
topic_growth -> median_cites_2yr  [sensitivity only]
topic_growth -> hit_rate_2yr  [sensitivity only]
topic_growth -> topic_share_t  [sensitivity only]
median_cites_2yr -> topic_growth  [sensitivity only]
median_cites_2yr -> hit_rate_2yr  [sensitivity only]
median_cites_2yr -> topic_share_t  [sensitivity only]
hit_rate_2yr -> topic_growth  [sensitivity only]
hit_rate_2yr -> median_cites_2yr  [sensitivity only]
hit_rate_2yr -> topic_share_t  [sensitivity only]
topic_share_t -> topic_growth  [sensitivity only]
topic_share_t -> median_cites_2yr  [sensitivity only]
topic_share_t -> hit_rate_2yr  [sensitivity only]
```

### Predictor-predictor (t-1 -> t-1), interpretive extension

Not explicitly specified, but treated the same way as outcome-outcome edges here: both tiers are contemporaneous internally, so within-tier edges have no temporal basis for the main model, only a correlational one. Flagged explicitly as an interpretive choice, available as an additional Step 4 sensitivity setting if useful (e.g. checking whether `topic_share_t1` and `modularity_t1`, r=0.43 in the Step 1 correlation analysis, should be modeled as connected).

```
topic_share_t1 -> cross_topic_rate_t1  [sensitivity only]
topic_share_t1 -> connectivity_t1  [sensitivity only]
topic_share_t1 -> modularity_t1  [sensitivity only]
topic_share_t1 -> bridge_concentration_t1  [sensitivity only]
cross_topic_rate_t1 -> topic_share_t1  [sensitivity only]
cross_topic_rate_t1 -> connectivity_t1  [sensitivity only]
cross_topic_rate_t1 -> modularity_t1  [sensitivity only]
cross_topic_rate_t1 -> bridge_concentration_t1  [sensitivity only]
connectivity_t1 -> topic_share_t1  [sensitivity only]
connectivity_t1 -> cross_topic_rate_t1  [sensitivity only]
connectivity_t1 -> modularity_t1  [sensitivity only]
connectivity_t1 -> bridge_concentration_t1  [sensitivity only]
modularity_t1 -> topic_share_t1  [sensitivity only]
modularity_t1 -> cross_topic_rate_t1  [sensitivity only]
modularity_t1 -> connectivity_t1  [sensitivity only]
modularity_t1 -> bridge_concentration_t1  [sensitivity only]
bridge_concentration_t1 -> topic_share_t1  [sensitivity only]
bridge_concentration_t1 -> cross_topic_rate_t1  [sensitivity only]
bridge_concentration_t1 -> connectivity_t1  [sensitivity only]
bridge_concentration_t1 -> modularity_t1  [sensitivity only]
```

## Notes for downstream steps

- These constraints are purely temporal. They say nothing about variable quality -- `bridge_concentration_t1`'s near-degeneracy and `modularity_t1`'s confound with topic size (Step 1 findings) still apply and are handled separately (which predictor subset a given PC setting uses), not by this module.

- `build_background_knowledge(..., size_vars=['n_papers_t1'])` builds an optional 4th tier for `n_papers_t1`, inserted below the regular predictors so it can enter `modularity_t1`'s conditioning set (forbid_within_tier would otherwise block a same-tier variable from ever doing that, regardless of correlation -- see the SIZE_VARS comment in this module). Used only by `pc_learning.py`'s `sensitivity_size_control` group, not the main model; see `pc_settings_comparison.md` for results.

- JSON export (`edge_constraints.json`) mirrors the schema already used in the team's `dag_constraints.json` (`forbidden_edges` + `temporal_tiers`), so the LLM-guided/hybrid parts of the project can consume it directly.

- `build_background_knowledge()` is directly reusable in Step 3: pass it the exact `node_names` list for a given PC run and it assigns tiers only to the variables present, so it works unmodified across the continuous/discretized settings and different citation-outcome choices.
