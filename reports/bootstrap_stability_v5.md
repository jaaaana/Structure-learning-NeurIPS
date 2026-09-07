# Bootstrap Stability Analysis -- Step 4 (v5)

Topic-level block bootstrap (seed=0, requested B=500) at the frozen main-model setting (alpha=0.05, constrained, temporal + exogenous-year background knowledge applied). Each replicate resamples topics (not rows) with replacement and keeps every row of each sampled topic, per the 2026-08-19 correction: rows are repeated topic-year measurements, so plain row-level bootstrap would treat a topic's own yearly observations as independent draws. This is a separate sensitivity axis from `pc_settings_comparison_v5.md`'s alpha/representation grid -- that grid holds the sample fixed and varies settings; this analysis holds settings fixed and varies the sample.

## continuous / Fisher-Z

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=79, mean=127.8, max=177 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction. Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0
               year     connectivity_t1                  500               500           1.000                  500                              1.0
               year     log1p_median_c2                  485               500           0.970                  485                              1.0
               year cross_topic_rate_t1                  416               500           0.832                  416                              1.0
               year       topic_share_t                  342               500           0.684                  342                              1.0
cross_topic_rate_t1     log1p_median_c2                  248               500           0.496                  248                              1.0
      modularity_t1     log1p_median_c2                  185               500           0.370                  185                              1.0
               year       modularity_t1                  149               500           0.298                  149                              1.0
      modularity_t1       topic_share_t                   28               500           0.056                   28                              1.0
    connectivity_t1     log1p_median_c2                   11               500           0.022                   11                              1.0
               year      topic_share_t1                   10               500           0.020                   10                              1.0
cross_topic_rate_t1       topic_share_t                    3               500           0.006                    3                              1.0
     topic_share_t1     log1p_median_c2                    2               500           0.004                    2                              1.0
    connectivity_t1       topic_share_t                    1               500           0.002                    1                              1.0
```

## discretized / chi-square

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=79, mean=127.8, max=177 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction. Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0
               year     connectivity_t1                  467               500           0.934                  467                              1.0
               year     log1p_median_c2                  450               500           0.900                  450                              1.0
cross_topic_rate_t1     log1p_median_c2                  392               500           0.784                  392                              1.0
               year cross_topic_rate_t1                  361               500           0.722                  361                              1.0
               year      topic_share_t1                  310               500           0.620                  310                              1.0
    connectivity_t1     log1p_median_c2                  298               500           0.596                  298                              1.0
               year       modularity_t1                  283               500           0.566                  283                              1.0
      modularity_t1     log1p_median_c2                  253               500           0.506                  253                              1.0
               year       topic_share_t                  182               500           0.364                  182                              1.0
    connectivity_t1       topic_share_t                  164               500           0.328                  164                              1.0
cross_topic_rate_t1       topic_share_t                  158               500           0.316                  158                              1.0
     topic_share_t1     log1p_median_c2                   80               500           0.160                   80                              1.0
      modularity_t1       topic_share_t                   39               500           0.078                   39                              1.0
```
