# Predictive Usefulness -- Step 5 / thesis D2.3 (v4)

Topic-grouped cross-validation (GroupKFold, k=5, grouped by `topic`) comparing four linear models per outcome, using the exact same fold split for all four so every model is scored on identical held-out topics. Grouped rather than plain K-fold because rows are repeated topic-year measurements -- a random split could put the same topic's rows in both train and test, leaking topic-level persistence into the score (same concern as `bootstrap_stability.py`'s topic-block resampling).

`baseline` is the minimal, non-graph comparison per outcome: `year` only for `log1p_median_c2`, `topic_share_t1` + `year` for `topic_share_t`. `graph_parents_nested_cv` is always `baseline`'s own features plus zero or more additional predictors -- **selected separately inside each fold, using only that fold's training topics** (150 bootstrap replicates per fold, continuous/Fisher-Z, adjacency threshold >= 0.5), never using the held-out fold's topics for selection the way a single full-dataset bootstrap would. Because its features are always a superset of `baseline`'s, an improvement over `baseline` cleanly means the added predictors carry predictive information beyond it, not that an unrelated feature set happened to score higher. **This is a predictive-value claim only**: if `graph_parents_nested_cv` outperforms `baseline`, that shows the selected social/network predictors add knowledge beyond the simple temporal effects already in `baseline` -- it does not show those predictors are proven causal, which would require the PC/bootstrap stability evidence above, not this comparison. This threshold is kept numerically identical to the frozen main model's bootstrap threshold for interpretability, even though its statistical meaning differs here (fewer topics per fold, far fewer replicates than the main 500-replicate full-dataset bootstrap) -- not presented as directly comparable to that number. `graph_parents_nested_cv` is a different statistic from any `stable`/`candidate` tier in `final_team_deliverable.md` (which uses the full-dataset, both-representations bootstrap), not the same one restated.

`all_t1_no_modularity` is `all_t1` with `modularity_t1` dropped -- added after `pc_learning.py`'s `sensitivity_size_control` group showed every `modularity_t1 -> outcome` edge in the main model disappears once topic size (`n_papers_t1`) is controllable, replaced by `n_papers_t1 -> modularity_t1`. This checks how much of `all_t1`'s predictive gain over baseline was actually riding on that now-refuted predictor, without changing the original `all_t1` row above it.

## topic_share_t

```
model                    features                                           R2 (mean+/-std)      MAE (mean+/-std)    
baseline                 topic_share_t1, year                               0.804+/-0.119        0.008+/-0.001       
all_t1                   topic_share_t1, cross_topic_rate_t1, connecti...   0.810+/-0.135        0.007+/-0.001       
all_t1_no_modularity     topic_share_t1, cross_topic_rate_t1, connecti...   0.812+/-0.132        0.007+/-0.001       
graph_parents_nested_cv  topic_share_t1, year                               0.804+/-0.119        0.008+/-0.001       
```
- `graph_parents_nested_cv` (baseline features + graph-selected predictors, nested per-fold bootstrap (150 reps/fold, continuous/Fisher-Z, threshold=0.5, base_seed=0 -> per-fold seeds 0..4)): no additional predictor cleared the threshold in any fold

### topic_share_t: predictor-selection threshold robustness

Same 5 folds and settings as `graph_parents_nested_cv` above -- each fold's training-only bootstrap frequency table (150 replicates, continuous/Fisher-Z) is computed **once** and reused for every threshold below (0.30, 0.50, 0.70), never re-bootstrapped per threshold. Baseline features are always kept; only the additional selected predictors vary. The goal is not to find the best-scoring threshold -- it's to check whether the predictive-usefulness conclusion holds up under a stricter or looser selection rule than the frozen 0.5.

```
threshold   R2 (mean+/-std)      MAE (mean+/-std)    
0.30        0.809+/-0.109        0.008+/-0.001       
0.50        0.804+/-0.119        0.008+/-0.001       
0.70        0.804+/-0.119        0.008+/-0.001       
(baseline)  0.804                0.008               
(all_t1)    0.810                0.007               
```
- threshold=0.30: selected per fold beyond baseline: modularity_t1 (1/5 folds)
- threshold=0.50: no additional predictor cleared this threshold in any fold
- threshold=0.70: no additional predictor cleared this threshold in any fold
- **Threshold-dependence check** (informal yardstick, not a statistical test): R2 varies by 0.005 across thresholds 0.30-0.70, not small relative to the 0.006 gap between baseline and all_t1 -- the predictive-usefulness conclusion for this outcome is sensitive to the selection-threshold choice; treat `graph_parents_nested_cv`'s single frozen-threshold result with that in mind.

## log1p_median_c2

```
model                    features                                           R2 (mean+/-std)      MAE (mean+/-std)    
baseline                 year                                               0.121+/-0.232        0.525+/-0.085       
all_t1                   topic_share_t1, cross_topic_rate_t1, connecti...   0.352+/-0.218        0.448+/-0.086       
all_t1_no_modularity     topic_share_t1, cross_topic_rate_t1, connecti...   0.334+/-0.162        0.468+/-0.069       
graph_parents_nested_cv  year                                               0.121+/-0.232        0.525+/-0.085       
```
- `graph_parents_nested_cv` (baseline features + graph-selected predictors, nested per-fold bootstrap (150 reps/fold, continuous/Fisher-Z, threshold=0.5, base_seed=0 -> per-fold seeds 0..4)): no additional predictor cleared the threshold in any fold

### log1p_median_c2: predictor-selection threshold robustness

Same 5 folds and settings as `graph_parents_nested_cv` above -- each fold's training-only bootstrap frequency table (150 replicates, continuous/Fisher-Z) is computed **once** and reused for every threshold below (0.30, 0.50, 0.70), never re-bootstrapped per threshold. Baseline features are always kept; only the additional selected predictors vary. The goal is not to find the best-scoring threshold -- it's to check whether the predictive-usefulness conclusion holds up under a stricter or looser selection rule than the frozen 0.5.

```
threshold   R2 (mean+/-std)      MAE (mean+/-std)    
0.30        0.124+/-0.231        0.524+/-0.081       
0.50        0.121+/-0.232        0.525+/-0.085       
0.70        0.121+/-0.232        0.525+/-0.085       
(baseline)  0.121                0.525               
(all_t1)    0.352                0.448               
```
- threshold=0.30: selected per fold beyond baseline: modularity_t1 (3/5 folds)
- threshold=0.50: no additional predictor cleared this threshold in any fold
- threshold=0.70: no additional predictor cleared this threshold in any fold
- **Threshold-dependence check** (informal yardstick, not a statistical test): R2 varies by only 0.003 across thresholds 0.30-0.70, small relative to the 0.231 gap between baseline and all_t1 -- the predictive-usefulness conclusion for this outcome looks stable to the selection-threshold choice.
