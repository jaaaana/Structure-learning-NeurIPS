# Bootstrap Stability Analysis -- Step 4 (v5)

Topic-level block bootstrap (seed=0, requested B=500) at the frozen main-model setting (alpha=0.05, constrained, temporal + exogenous-year background knowledge applied). Each replicate resamples topics (not rows) with replacement and keeps every row of each sampled topic, per the 2026-08-19 correction: rows are repeated topic-year measurements, so plain row-level bootstrap would treat a topic's own yearly observations as independent draws. This is a separate sensitivity axis from `pc_settings_comparison_v5.md`'s alpha/representation grid -- that grid holds the sample fixed and varies settings; this analysis holds settings fixed and varies the sample.

**Orientation-stability caveat**: in every table below, `orientation_rate_given_adjacent` is computed under the constrained (temporal background knowledge) setting. Under this pipeline's tier structure, every edge that can appear at all is between two different tiers, and `causal-learn` forcibly directs any such edge immediately after skeleton discovery -- before its own v-structure or Meek orientation rules ever run. So `orientation_rate_given_adjacent` here is mechanical (it reflects the constraint being applied, not an independent PC finding); `adjacency_rate` -- not orientation rate -- is the actual stability evidence (it is also the only quantity `final_graph.py`'s stable/candidate/ambiguous tiering ever reads). `same_direction_rate` is only informative for same-tier pairs (two predictors or two outcomes, where background knowledge doesn't force a direction either way): it reports whether replicates that did orient the pair agreed on *which* direction, so a pair that's oriented often but flips between A->B and B->A across replicates shows up as high `orientation_rate_given_adjacent` but low `same_direction_rate` -- a materially weaker finding than a consistently-oriented pair. See 'Orientation provenance' below for genuine, unconstrained-derived orientation evidence.

## continuous / Fisher-Z

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=79, mean=127.8, max=177 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction -- see the caveat above: this is mechanical under the constrained setting here, not independent evidence. `same_direction_rate` = of all adjacent replicates, share that agreed on the same direction (only non-trivial for same-tier pairs -- see caveat above). Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent  same_direction_rate
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0                  1.0
               year     connectivity_t1                  500               500           1.000                  500                              1.0                  1.0
               year     log1p_median_c2                  485               500           0.970                  485                              1.0                  1.0
               year cross_topic_rate_t1                  416               500           0.832                  416                              1.0                  1.0
               year       topic_share_t                  342               500           0.684                  342                              1.0                  1.0
cross_topic_rate_t1     log1p_median_c2                  248               500           0.496                  248                              1.0                  1.0
      modularity_t1     log1p_median_c2                  185               500           0.370                  185                              1.0                  1.0
               year       modularity_t1                  149               500           0.298                  149                              1.0                  1.0
      modularity_t1       topic_share_t                   28               500           0.056                   28                              1.0                  1.0
    connectivity_t1     log1p_median_c2                   11               500           0.022                   11                              1.0                  1.0
               year      topic_share_t1                   10               500           0.020                   10                              1.0                  1.0
cross_topic_rate_t1       topic_share_t                    3               500           0.006                    3                              1.0                  1.0
     topic_share_t1     log1p_median_c2                    2               500           0.004                    2                              1.0                  1.0
    connectivity_t1       topic_share_t                    1               500           0.002                    1                              1.0                  1.0
```

## discretized / chi-square

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample, a node had fewer than 2 distinct values): 0. Failed (PC raised an exception): 0.
- Resampled row count per replicate: min=79, mean=127.8, max=177 (varies because block bootstrap resamples topics, not rows -- a topic drawn twice contributes its rows twice, a topic not drawn contributes none).

`adjacency_rate` = share of successful replicates where PC placed any edge (directed or undirected) between the pair; `orientation_rate_given_adjacent` = of those, share where PC committed to a direction -- see the caveat above: this is mechanical under the constrained setting here, not independent evidence. `same_direction_rate` = of all adjacent replicates, share that agreed on the same direction (only non-trivial for same-tier pairs -- see caveat above). Sorted by adjacency_rate descending -- this table, not the settings-grid recurrence table, is the stability evidence for Step 5 / thesis Chapter 5. No fixed stable/unstable cutoff is applied here; choose and justify a threshold in the writeup.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent  same_direction_rate
     topic_share_t1       topic_share_t                  500               500           1.000                  500                              1.0                  1.0
               year     connectivity_t1                  467               500           0.934                  467                              1.0                  1.0
               year     log1p_median_c2                  450               500           0.900                  450                              1.0                  1.0
cross_topic_rate_t1     log1p_median_c2                  392               500           0.784                  392                              1.0                  1.0
               year cross_topic_rate_t1                  361               500           0.722                  361                              1.0                  1.0
               year      topic_share_t1                  310               500           0.620                  310                              1.0                  1.0
    connectivity_t1     log1p_median_c2                  298               500           0.596                  298                              1.0                  1.0
               year       modularity_t1                  283               500           0.566                  283                              1.0                  1.0
      modularity_t1     log1p_median_c2                  253               500           0.506                  253                              1.0                  1.0
               year       topic_share_t                  182               500           0.364                  182                              1.0                  1.0
    connectivity_t1       topic_share_t                  164               500           0.328                  164                              1.0                  1.0
cross_topic_rate_t1       topic_share_t                  158               500           0.316                  158                              1.0                  1.0
     topic_share_t1     log1p_median_c2                   80               500           0.160                   80                              1.0                  1.0
      modularity_t1       topic_share_t                   39               500           0.078                   39                              1.0                  1.0
```

## Orientation provenance (continuous / Fisher-Z, unconstrained comparison)

Same topic-level resamples as the continuous/Fisher-Z bootstrap above (identical seed), rerun with **no background knowledge at all** -- not just the within-tier restriction, the temporal t-1->t rule too. This is the only way to get independent evidence for a direction the constrained model can only ever assume: if PC's own v-structure/Meek orientation logic, with no help from the temporal assumption, still lands on the same direction most of the time, that is real corroboration; if it does not, the direction rests on the temporal assumption alone.

- Requested: 500 replicates. Succeeded: 500. Skipped (degenerate resample): 0. Failed (PC raised an exception): 0.

`constrained_adjacency_rate` is from the constrained bootstrap above, shown for reference. `same_direction_rate`/`reverse_direction_rate`/`undirected_rate` are shares of unconstrained-adjacent replicates where PC, with no constraint at all, oriented the pair the same way the temporal rule would force, the opposite way, or left it undirected.

```
               from                  to  constrained_adjacency_rate  unconstrained_adjacency_rate  same_direction_rate  reverse_direction_rate  undirected_rate
               year     connectivity_t1                       1.000                         1.000                0.498                   0.498            0.004
     topic_share_t1       topic_share_t                       1.000                         1.000                0.016                   0.430            0.554
               year     log1p_median_c2                       0.970                         0.970                0.151                   0.571            0.278
               year cross_topic_rate_t1                       0.832                         0.824                0.182                   0.561            0.257
               year       topic_share_t                       0.684                         0.682                0.073                   0.613            0.314
cross_topic_rate_t1     log1p_median_c2                       0.496                         0.472                0.174                   0.123            0.703
      modularity_t1     log1p_median_c2                       0.370                         0.316                0.285                   0.165            0.551
               year       modularity_t1                       0.298                         0.298                0.416                   0.584            0.000
    connectivity_t1     log1p_median_c2                       0.022                         0.018                0.889                   0.111            0.000
               year      topic_share_t1                       0.020                         0.016                0.250                   0.625            0.125
      modularity_t1       topic_share_t                       0.056                         0.010                0.400                   0.200            0.400
cross_topic_rate_t1       topic_share_t                       0.006                         0.006                0.000                   1.000            0.000
     topic_share_t1     log1p_median_c2                       0.004                         0.004                0.000                   1.000            0.000
```

### Edges only visible once all constraints are relaxed

Predictor-predictor or outcome-outcome pairs -- banned from the constrained model's skeleton outright (`forbid_within_tier`), so they can never appear in the tables above at any adjacency rate. There is no tier-implied direction here for PC to agree or disagree with (unlike the cross-tier table above), so `same_direction_rate`/`reverse_direction_rate` instead measure *internal* consistency: the share of adjacent replicates that agreed with each other on which of the two (arbitrarily, alphabetically ordered) directions to pick. A pair with high adjacency but a near-even split between the two is not a stable finding either way -- its direction is essentially random noise across replicates, not just unconstrained by assumption.

```
               from                  to  n_adjacent  adjacency_rate  same_direction_rate  reverse_direction_rate  undirected_rate
      modularity_t1      topic_share_t1         336           0.672                0.598                   0.250            0.152
    connectivity_t1       modularity_t1         258           0.516                0.019                   0.965            0.016
cross_topic_rate_t1       modularity_t1         113           0.226                0.177                   0.425            0.398
    connectivity_t1 cross_topic_rate_t1          17           0.034                0.765                   0.059            0.176
    log1p_median_c2       topic_share_t           8           0.016                0.375                   0.125            0.500
    connectivity_t1      topic_share_t1           6           0.012                0.333                   0.667            0.000
cross_topic_rate_t1      topic_share_t1           2           0.004                1.000                   0.000            0.000
```
