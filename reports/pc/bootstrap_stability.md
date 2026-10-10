# Bootstrap Stability Analysis -- Step 4 (v4)

Topic-level block bootstrap (seed=0, requested B=500) at the frozen main-model setting (alpha=0.05, constrained, temporal + exogenous-year background knowledge applied). Each replicate resamples topics (not rows) with replacement and keeps every row of each sampled topic, per the 2026-08-19 correction: rows are repeated topic-year measurements, so plain row-level bootstrap would treat a topic's own yearly observations as independent draws. This is a separate sensitivity axis from `pc_settings_comparison.md`'s alpha/representation grid -- that grid holds the sample fixed and varies settings; this analysis holds settings fixed and varies the sample.

**Orientation-stability caveat**: in every table below, `orientation_rate_given_adjacent` is computed under the constrained (temporal background knowledge) setting. Under this pipeline's tier structure, every edge that can appear at all is between two different tiers, and `causal-learn` forcibly directs any such edge immediately after skeleton discovery -- before its own v-structure or Meek orientation rules ever run. So `orientation_rate_given_adjacent` here is mechanical (it reflects the constraint being applied, not an independent PC finding); `adjacency_rate` -- not orientation rate -- is the actual stability evidence (it is also the only quantity `final_graph.py`'s stable/candidate/ambiguous tiering ever reads). `same_direction_rate` is only informative for same-tier pairs (two predictors or two outcomes, where background knowledge doesn't force a direction either way): it reports whether replicates that did orient the pair agreed on *which* direction, so a pair that's oriented often but flips between A->B and B->A across replicates shows up as high `orientation_rate_given_adjacent` but low `same_direction_rate` -- a materially weaker finding than a consistently-oriented pair. See 'Orientation provenance' below for genuine, unconstrained-derived orientation evidence.

## continuous / Fisher-Z

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=81, mean=123.0, max=169 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction -- see the caveat above: this is mechanical under the constrained setting here, not independent evidence. `same_direction_rate` = of all adjacent replicates, share that agreed on the same direction (only non-trivial for same-tier pairs -- see caveat above). Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent  same_direction_rate
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0                  1.0
               year     connectivity_t1                  500               500           1.000                  500                              1.0                  1.0
               year     log1p_median_c2                  500               500           1.000                  500                              1.0                  1.0
      modularity_t1     log1p_median_c2                  205               500           0.410                  205                              1.0                  1.0
               year      topic_share_t1                  182               500           0.364                  182                              1.0                  1.0
      modularity_t1       topic_share_t                  137               500           0.274                  137                              1.0                  1.0
               year       modularity_t1                  124               500           0.248                  124                              1.0                  1.0
               year cross_topic_rate_t1                  101               500           0.202                  101                              1.0                  1.0
cross_topic_rate_t1     log1p_median_c2                  100               500           0.200                  100                              1.0                  1.0
               year       topic_share_t                   81               500           0.162                   81                              1.0                  1.0
    connectivity_t1       topic_share_t                   58               500           0.116                   58                              1.0                  1.0
     topic_share_t1     log1p_median_c2                   14               500           0.028                   14                              1.0                  1.0
    connectivity_t1     log1p_median_c2                    8               500           0.016                    8                              1.0                  1.0
```

## discretized / chi-square

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=81, mean=123.0, max=169 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction -- see the caveat above: this is mechanical under the constrained setting here, not independent evidence. `same_direction_rate` = of all adjacent replicates, share that agreed on the same direction (only non-trivial for same-tier pairs -- see caveat above). Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent  same_direction_rate
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0                  1.0
               year     log1p_median_c2                  491               500           0.982                  491                              1.0                  1.0
               year     connectivity_t1                  472               500           0.944                  472                              1.0                  1.0
    connectivity_t1     log1p_median_c2                  360               500           0.720                  360                              1.0                  1.0
               year      topic_share_t1                  308               500           0.616                  308                              1.0                  1.0
               year cross_topic_rate_t1                  290               500           0.580                  290                              1.0                  1.0
               year       modularity_t1                  268               500           0.536                  268                              1.0                  1.0
cross_topic_rate_t1     log1p_median_c2                  209               500           0.418                  209                              1.0                  1.0
cross_topic_rate_t1       topic_share_t                  174               500           0.348                  174                              1.0                  1.0
      modularity_t1       topic_share_t                  155               500           0.310                  155                              1.0                  1.0
      modularity_t1     log1p_median_c2                  128               500           0.256                  128                              1.0                  1.0
    connectivity_t1       topic_share_t                   81               500           0.162                   81                              1.0                  1.0
     topic_share_t1     log1p_median_c2                   64               500           0.128                   64                              1.0                  1.0
               year       topic_share_t                   48               500           0.096                   48                              1.0                  1.0
```

## Orientation provenance (continuous / Fisher-Z, unconstrained comparison)

Same topic-level resamples as the continuous/Fisher-Z bootstrap above (identical seed), rerun with **no background knowledge at all** -- not just the within-tier restriction, the temporal t-1->t rule too. This is the only way to get independent evidence for a direction the constrained model can only ever assume: if PC's own v-structure/Meek orientation logic, with no help from the temporal assumption, still lands on the same direction most of the time, that is real corroboration; if it does not, the direction rests on the temporal assumption alone.

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample): 0. Failed (PC raised an exception): 0.

`constrained_adjacency_rate` is from the constrained bootstrap above, shown for reference. `same_direction_rate`/`reverse_direction_rate`/`undirected_rate` are shares of unconstrained-adjacent replicates where PC, with no constraint at all, oriented the pair the same way the temporal rule would force, the opposite way, or left it undirected.

```
               from                  to  constrained_adjacency_rate  unconstrained_adjacency_rate  same_direction_rate  reverse_direction_rate  undirected_rate
               year     connectivity_t1                       1.000                         1.000                0.570                   0.424            0.006
     topic_share_t1       topic_share_t                       1.000                         1.000                0.112                   0.308            0.580
               year     log1p_median_c2                       1.000                         1.000                0.086                   0.590            0.324
      modularity_t1     log1p_median_c2                       0.410                         0.358                0.190                   0.128            0.682
               year      topic_share_t1                       0.364                         0.348                0.466                   0.466            0.069
               year       modularity_t1                       0.248                         0.244                0.525                   0.475            0.000
               year cross_topic_rate_t1                       0.202                         0.202                0.168                   0.683            0.149
cross_topic_rate_t1     log1p_median_c2                       0.200                         0.196                0.061                   0.204            0.735
               year       topic_share_t                       0.162                         0.152                0.079                   0.724            0.197
      modularity_t1       topic_share_t                       0.274                         0.106                0.189                   0.321            0.491
    connectivity_t1       topic_share_t                       0.116                         0.102                0.020                   0.980            0.000
     topic_share_t1     log1p_median_c2                       0.028                         0.012                0.000                   1.000            0.000
    connectivity_t1     log1p_median_c2                       0.016                         0.010                0.200                   0.200            0.600
```

### Edges only visible once all constraints are relaxed

Predictor-predictor or outcome-outcome pairs -- banned from the constrained model's skeleton outright (`forbid_within_tier`), so they can never appear in the tables above at any adjacency rate. There is no tier-implied direction here for PC to agree or disagree with (unlike the cross-tier table above), so `same_direction_rate`/`reverse_direction_rate` instead measure *internal* consistency: the share of adjacent replicates that agreed with each other on which of the two (arbitrarily, alphabetically ordered) directions to pick. A pair with high adjacency but a near-even split between the two is not a stable finding either way -- its direction is essentially random noise across replicates, not just unconstrained by assumption.

```
               from                  to  n_adjacent  adjacency_rate  same_direction_rate  reverse_direction_rate  undirected_rate
      modularity_t1      topic_share_t1         339           0.678                0.546                   0.263            0.192
    connectivity_t1       modularity_t1         253           0.506                0.008                   0.976            0.016
cross_topic_rate_t1       modularity_t1         101           0.202                0.238                   0.218            0.545
    connectivity_t1 cross_topic_rate_t1          66           0.132                0.106                   0.894            0.000
    connectivity_t1      topic_share_t1          12           0.024                0.833                   0.083            0.083
    log1p_median_c2       topic_share_t          10           0.020                0.700                   0.200            0.100
cross_topic_rate_t1      topic_share_t1           1           0.002                1.000                   0.000            0.000
```
