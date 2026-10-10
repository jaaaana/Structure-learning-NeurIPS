# GOLEM Predictive Usefulness (v5)
Five-fold topic-grouped cross-validation. Predictor selection uses training topics only (150 bootstrap fits per fold; lambda1=0.02; lambda_dag=5.0; tolerance=1e-06; max_iter=10000; edge threshold=0.1; selection frequency threshold=0.5). Only converged fits count toward selection.
All models use the same five GroupKFold splits, grouped by topic. This keeps each topic's yearly rows together and prevents a topic from appearing in both training and held-out data.
`baseline` is the non-graph comparison: `topic_share_t ~ topic_share_t1 + year` and `log1p_median_c2 ~ year`. `golem_parents_nested_cv` keeps those baseline features and adds GOLEM-selected parents, selected separately in each training fold using topic-block bootstrap resamples (150 fits per fold; base seed 0; fold seeds 0..4). The held-out fold is not used for selection. An improvement over baseline therefore measures the added predictors' value beyond the baseline features.
`all_t1` and `all_t1_no_modularity` are fixed-feature benchmarks; the latter omits the size-associated `modularity_t1` to show whether performance depends on that feature. These scores measure predictive usefulness, not causal effects.
## topic_share_t
```
model                    features                                           R2 (mean+/-std)      MAE (mean+/-std)
------------------------ -------------------------------------------------- ------------------- -------------------
baseline                 topic_share_t1, year                               0.672+/-0.162        0.010+/-0.002
all_t1                   topic_share_t1, cross_topic_rate_t1, connecti...   0.666+/-0.189        0.010+/-0.001
all_t1_no_modularity     topic_share_t1, cross_topic_rate_t1, connecti...   0.668+/-0.181        0.010+/-0.001
golem_parents_nested_cv  topic_share_t1, year                               0.677+/-0.160        0.010+/-0.001
```
- `golem_parents_nested_cv` (baseline features + graph-selected predictors, nested per-fold bootstrap (150 reps/fold, threshold=0.5)): connectivity_t1_log (4/5 folds)

### topic_share_t: predictor-selection threshold robustness
Each fold's training-only bootstrap frequency table is computed once and reused for every threshold shown here. Baseline features are retained; this checks sensitivity to the selection cutoff rather than choosing the best-scoring cutoff.

```
threshold   R2 (mean+/-std)      MAE (mean+/-std)
---------   -------------------  -------------------
0.30        0.681+/-0.165        0.010+/-0.001
0.50        0.677+/-0.160        0.010+/-0.001
0.70        0.672+/-0.157        0.010+/-0.001
(baseline)     0.672+/-0.162        0.010+/-0.002
(all_t1)     0.666+/-0.189        0.010+/-0.001
```
- threshold=0.30: selected per fold beyond baseline: connectivity_t1_log (5/5 folds)
- threshold=0.50: selected per fold beyond baseline: connectivity_t1_log (4/5 folds)
- threshold=0.70: selected per fold beyond baseline: connectivity_t1_log (3/5 folds)
- **Threshold-dependence check** (informal yardstick, not a statistical test): R2 varies by 0.009 across thresholds 0.30-0.70, not small relative to the 0.006 baseline-to-all_t1 gap; the conclusion is sensitive to the cutoff, so interpret the frozen-threshold result with care.

#### GOLEM fit convergence by fold
fold | training topics | converged / requested | nonconverged | failed | degenerate
---: | ---: | ---: | ---: | ---: | ---:
0 | 17 | 150/150 | 0 | 0 | 0
1 | 18 | 150/150 | 0 | 0 | 0
2 | 17 | 150/150 | 0 | 0 | 0
3 | 18 | 150/150 | 0 | 0 | 0
4 | 18 | 150/150 | 0 | 0 | 0

## log1p_median_c2
```
model                    features                                           R2 (mean+/-std)      MAE (mean+/-std)
------------------------ -------------------------------------------------- ------------------- -------------------
baseline                 year                                               -0.046+/-0.323        0.482+/-0.060
all_t1                   topic_share_t1, cross_topic_rate_t1, connecti...   0.252+/-0.185        0.412+/-0.035
all_t1_no_modularity     topic_share_t1, cross_topic_rate_t1, connecti...   0.154+/-0.284        0.439+/-0.065
golem_parents_nested_cv  year                                               0.261+/-0.187        0.411+/-0.036
```
- `golem_parents_nested_cv` (baseline features + graph-selected predictors, nested per-fold bootstrap (150 reps/fold, threshold=0.5)): connectivity_t1_log (5/5 folds), modularity_t1 (5/5 folds), topic_share_t1 (5/5 folds)

### log1p_median_c2: predictor-selection threshold robustness
Each fold's training-only bootstrap frequency table is computed once and reused for every threshold shown here. Baseline features are retained; this checks sensitivity to the selection cutoff rather than choosing the best-scoring cutoff.

```
threshold   R2 (mean+/-std)      MAE (mean+/-std)
---------   -------------------  -------------------
0.30        0.254+/-0.182        0.412+/-0.035
0.50        0.261+/-0.187        0.411+/-0.036
0.70        0.261+/-0.187        0.411+/-0.036
(baseline)     -0.046+/-0.323        0.482+/-0.060
(all_t1)     0.252+/-0.185        0.412+/-0.035
```
- threshold=0.30: selected per fold beyond baseline: connectivity_t1_log (5/5 folds), modularity_t1 (5/5 folds), topic_share_t1 (5/5 folds), cross_topic_rate_t1 (2/5 folds)
- threshold=0.50: selected per fold beyond baseline: connectivity_t1_log (5/5 folds), modularity_t1 (5/5 folds), topic_share_t1 (5/5 folds)
- threshold=0.70: selected per fold beyond baseline: connectivity_t1_log (5/5 folds), modularity_t1 (5/5 folds), topic_share_t1 (5/5 folds)
- **Threshold-dependence check** (informal yardstick, not a statistical test): R2 varies by only 0.006 across thresholds 0.30-0.70, small relative to the 0.298 baseline-to-all_t1 gap; the predictive-usefulness conclusion looks stable to this cutoff choice.

#### GOLEM fit convergence by fold
fold | training topics | converged / requested | nonconverged | failed | degenerate
---: | ---: | ---: | ---: | ---: | ---:
0 | 17 | 150/150 | 0 | 0 | 0
1 | 18 | 150/150 | 0 | 0 | 0
2 | 17 | 150/150 | 0 | 0 | 0
3 | 18 | 150/150 | 0 | 0 | 0
4 | 18 | 150/150 | 0 | 0 | 0

