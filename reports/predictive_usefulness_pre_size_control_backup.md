# Predictive Usefulness -- Step 5 / thesis D2.3 (v4)

Topic-grouped cross-validation (GroupKFold, k=5, grouped by `topic`) comparing three linear models per outcome. Grouped rather than plain K-fold because rows are repeated topic-year measurements -- a random split could put the same topic's rows in both train and test, leaking topic-level persistence into the score (same concern as `bootstrap_stability.py`'s topic-block resampling).

`graph_parents` is derived directly from Step 4's bootstrap results: a predictor counts as a parent if its mean (continuous + discretized) bootstrap adjacency rate into that outcome is >= 0.5. This is a documented, recomputable threshold, not a hand-picked edge list, and is a first look at what a Step 5 stable-edge graph would contain.

## topic_share_t

```
model           features                                                R2 (mean+/-std)      MAE (mean+/-std)    
baseline        topic_share_t1                                          0.806+/-0.124        0.008+/-0.001       
all_t1          topic_share_t1, cross_topic_rate_t1, connectivity_...   0.810+/-0.135        0.007+/-0.001       
graph_parents   topic_share_t1                                          0.806+/-0.124        0.008+/-0.001       
```

## log1p_median_c2

```
model           features                                                R2 (mean+/-std)      MAE (mean+/-std)    
baseline        (none)                                                  -0.163+/-0.211       0.581+/-0.097       
all_t1          topic_share_t1, cross_topic_rate_t1, connectivity_...   0.352+/-0.218        0.448+/-0.086       
graph_parents   year                                                    0.121+/-0.232        0.525+/-0.085       
```
