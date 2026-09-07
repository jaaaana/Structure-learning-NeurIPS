# Bootstrap Stability Analysis -- Step 4 (v4)

Topic-level block bootstrap (seed=0, requested B=500) at the frozen main-model setting (alpha=0.05, constrained, temporal + exogenous-year background knowledge applied). Each replicate resamples topics (not rows) with replacement and keeps every row of each sampled topic, per the 2026-08-19 correction: rows are repeated topic-year measurements, so plain row-level bootstrap would treat a topic's own yearly observations as independent draws. This is a separate sensitivity axis from `pc_settings_comparison.md`'s alpha/representation grid -- that grid holds the sample fixed and varies settings; this analysis holds settings fixed and varies the sample.

## continuous / Fisher-Z

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=81, mean=123.0, max=169 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction. Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0
               year     connectivity_t1                  500               500           1.000                  500                              1.0
               year     log1p_median_c2                  500               500           1.000                  500                              1.0
      modularity_t1     log1p_median_c2                  205               500           0.410                  205                              1.0
               year      topic_share_t1                  182               500           0.364                  182                              1.0
      modularity_t1       topic_share_t                  137               500           0.274                  137                              1.0
               year       modularity_t1                  124               500           0.248                  124                              1.0
               year cross_topic_rate_t1                  101               500           0.202                  101                              1.0
cross_topic_rate_t1     log1p_median_c2                  100               500           0.200                  100                              1.0
               year       topic_share_t                   81               500           0.162                   81                              1.0
    connectivity_t1       topic_share_t                   58               500           0.116                   58                              1.0
     topic_share_t1     log1p_median_c2                   14               500           0.028                   14                              1.0
    connectivity_t1     log1p_median_c2                    8               500           0.016                    8                              1.0
```

## discretized / chi-square

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=81, mean=123.0, max=169 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction. Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0
               year     log1p_median_c2                  491               500           0.982                  491                              1.0
               year     connectivity_t1                  472               500           0.944                  472                              1.0
    connectivity_t1     log1p_median_c2                  360               500           0.720                  360                              1.0
               year      topic_share_t1                  308               500           0.616                  308                              1.0
               year cross_topic_rate_t1                  290               500           0.580                  290                              1.0
               year       modularity_t1                  268               500           0.536                  268                              1.0
cross_topic_rate_t1     log1p_median_c2                  209               500           0.418                  209                              1.0
cross_topic_rate_t1       topic_share_t                  174               500           0.348                  174                              1.0
      modularity_t1       topic_share_t                  155               500           0.310                  155                              1.0
      modularity_t1     log1p_median_c2                  128               500           0.256                  128                              1.0
    connectivity_t1       topic_share_t                   81               500           0.162                   81                              1.0
     topic_share_t1     log1p_median_c2                   64               500           0.128                   64                              1.0
               year       topic_share_t                   48               500           0.096                   48                              1.0
```
