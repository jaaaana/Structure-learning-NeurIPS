# Predictive Usefulness -- Step 5 / thesis D2.3 (v5)

Topic-grouped cross-validation (GroupKFold, k=5, grouped by `topic`) comparing four linear models per outcome. Grouped rather than plain K-fold because rows are repeated topic-year measurements -- a random split could put the same topic's rows in both train and test, leaking topic-level persistence into the score (same concern as `bootstrap_stability.py`'s topic-block resampling).

`graph_parents` is derived directly from Step 4's bootstrap results: a predictor counts as a parent if its mean (continuous + discretized) bootstrap adjacency rate into that outcome is >= 0.5. This is a documented, recomputable threshold, not a hand-picked edge list, and is a first look at what a Step 5 stable-edge graph would contain.

`all_t1_no_modularity` is `all_t1` with `modularity_t1` dropped -- added after `pc_learning.py`'s `sensitivity_size_control` group showed every `modularity_t1 -> outcome` edge in the main model disappears once topic size (`n_papers_t1`) is controllable, replaced by `n_papers_t1 -> modularity_t1`. This checks how much of `all_t1`'s predictive gain over baseline was actually riding on that now-refuted predictor, without changing the original `all_t1` row above it.

## topic_share_t

```
model                features                                                R2 (mean+/-std)      MAE (mean+/-std)    
baseline             topic_share_t1                                          0.688+/-0.170        0.010+/-0.002       
all_t1               topic_share_t1, cross_topic_rate_t1, connectivity_...   0.688+/-0.185        0.010+/-0.002       
all_t1_no_modularity topic_share_t1, cross_topic_rate_t1, connectivity_...   0.696+/-0.171        0.010+/-0.002       
graph_parents        topic_share_t1, year                                    0.693+/-0.161        0.010+/-0.002       
```

## log1p_median_c2

```
model                features                                                R2 (mean+/-std)      MAE (mean+/-std)    
baseline             (none)                                                  -0.210+/-0.149       0.530+/-0.064       
all_t1               topic_share_t1, cross_topic_rate_t1, connectivity_...   0.263+/-0.213        0.412+/-0.046       
all_t1_no_modularity topic_share_t1, cross_topic_rate_t1, connectivity_...   0.140+/-0.263        0.448+/-0.056       
graph_parents        year, cross_topic_rate_t1                               -0.036+/-0.347       0.475+/-0.023       
```
