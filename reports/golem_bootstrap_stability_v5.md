# GOLEM Bootstrap Stability (v5)

Topic-block bootstrap: seed=0, requested B=500 per run. Constrained continuous and discretized fits, plus paired unconstrained continuous refits. lambda1=0.02, lambda_dag=5.0, learning_rate=0.001, edge threshold=0.1, tolerance=1e-06, max_iter=10000.

Pairs are ordered so the more frequent direction points from `a` to `b`; ties use alphabetical order. Rates use all eligible fits, including empty graphs. `a_to_b_rate`, `b_to_a_rate`, and `undirected_rate` sum to `adjacency_rate`; conditional rates divide by adjacent fits only. The directional conditional rates use all adjacent fits as the denominator, including undirected fits. In constrained runs, a zero reverse-direction rate can follow directly from the tier mask forbidding backward arrows; it is not independent evidence for that direction. Orientation frequency and consistency of a particular direction are distinct.

## continuous representation

```
 n_boot_requested  n_completed  n_succeeded  n_failed  n_nonconverged  n_degenerate_skipped  row_counts_min  row_counts_mean  row_counts_max
              500          500          500         0               0                     0              79         127.7540             177
```

Frequencies use converged replicates, including empty graphs; nonconverged fits are excluded.

```
                  a                   b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     connectivity_t1         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1       topic_share_t         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year cross_topic_rate_t1         499      500          0.9980       0.9980       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1     log1p_median_c2         496      500          0.9920       0.9920       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year      topic_share_t1         495      500          0.9900       0.9900       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       topic_share_t         484      500          0.9680       0.9680       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       modularity_t1         443      500          0.8860       0.8860       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1       topic_share_t         323      500          0.6460       0.6460       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1     log1p_median_c2         119      500          0.2380       0.2380       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1       topic_share_t          20      500          0.0400       0.0400       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1       topic_share_t          14      500          0.0280       0.0280       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

## discretized representation

```
 n_boot_requested  n_completed  n_succeeded  n_failed  n_nonconverged  n_degenerate_skipped  row_counts_min  row_counts_mean  row_counts_max
              500          500          500         0               0                     0              79         127.7540             177
```

Frequencies use converged replicates, including empty graphs; nonconverged fits are excluded.

```
                  a                   b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1       topic_share_t         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     connectivity_t1         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year cross_topic_rate_t1         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       modularity_t1         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1       topic_share_t         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       topic_share_t         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year      topic_share_t1         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1     log1p_median_c2         499      500          0.9980       0.9980       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1       topic_share_t         497      500          0.9940       0.9940       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1       topic_share_t         495      500          0.9900       0.9900       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

## Direction provenance (continuous, paired unconstrained refits)

Same topic-block draws refit without constraints. Direction rates use successful paired fits; same/reverse/undirected rates are conditional on unconstrained adjacency.

Common successful replicate IDs: 474. Requested unconstrained replicates: 500; converged: 474.

```
                  a               b  constrained_adjacency_rate                  constrained_direction  unconstrained_adjacency_rate  same_direction_rate  reverse_direction_rate  undirected_rate
      topic_share_t  topic_share_t1                      1.0000        topic_share_t1 -> topic_share_t                        1.0000               0.0274                  0.0759           0.8966
    log1p_median_c2  topic_share_t1                      1.0000      topic_share_t1 -> log1p_median_c2                        0.9979               0.8203                  0.0021           0.1776
    connectivity_t1 log1p_median_c2                      1.0000     connectivity_t1 -> log1p_median_c2                        1.0000               0.8291                  0.0232           0.1477
    connectivity_t1            year                      1.0000                year -> connectivity_t1                        1.0000               0.5485                  0.0000           0.4515
    log1p_median_c2            year                      1.0000                year -> log1p_median_c2                        1.0000               0.8439                  0.0021           0.1540
cross_topic_rate_t1            year                      0.9979            year -> cross_topic_rate_t1                        1.0000               0.8291                  0.0000           0.1709
    log1p_median_c2   modularity_t1                      0.9916       modularity_t1 -> log1p_median_c2                        0.9895               0.6333                  0.2431           0.1237
     topic_share_t1            year                      0.9895                 year -> topic_share_t1                        0.7743               0.0736                  0.0027           0.9237
      topic_share_t            year                      0.9726                  year -> topic_share_t                        0.9831               0.1867                  0.0043           0.8090
      modularity_t1            year                      0.8819                  year -> modularity_t1                        1.0000               0.7722                  0.0000           0.2278
    connectivity_t1   topic_share_t                      0.6519       connectivity_t1 -> topic_share_t                        0.9641               0.1882                  0.4770           0.3348
cross_topic_rate_t1 log1p_median_c2                      0.2447 cross_topic_rate_t1 -> log1p_median_c2                        0.4198               0.0955                  0.5226           0.3819
cross_topic_rate_t1   topic_share_t                      0.0422   cross_topic_rate_t1 -> topic_share_t                        0.5422               0.0000                  0.8249           0.1751
      modularity_t1   topic_share_t                      0.0295         modularity_t1 -> topic_share_t                        0.4283               0.1182                  0.2217           0.6601
```

## Edges only visible with tier restrictions relaxed

Same-tier edge recurrence in the unconstrained bootstrap.

```
              a                   b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
connectivity_t1     log1p_median_c2         474      474          1.0000       0.8291       0.0232           0.1477                           0.8523                 0.8291                 0.0232                     0.1477
           year     connectivity_t1         474      474          1.0000       0.5485       0.0000           0.4515                           0.5485                 0.5485                 0.0000                     0.4515
           year cross_topic_rate_t1         474      474          1.0000       0.8291       0.0000           0.1709                           0.8291                 0.8291                 0.0000                     0.1709
           year     log1p_median_c2         474      474          1.0000       0.8439       0.0021           0.1540                           0.8460                 0.8439                 0.0021                     0.1540
           year       modularity_t1         474      474          1.0000       0.7722       0.0000           0.2278                           0.7722                 0.7722                 0.0000                     0.2278
  topic_share_t      topic_share_t1         474      474          1.0000       0.0759       0.0274           0.8966                           0.1034                 0.0759                 0.0274                     0.8966
 topic_share_t1     log1p_median_c2         473      474          0.9979       0.8186       0.0021           0.1772                           0.8224                 0.8203                 0.0021                     0.1776
  modularity_t1     log1p_median_c2         469      474          0.9895       0.6266       0.2405           0.1224                           0.8763                 0.6333                 0.2431                     0.1237
           year       topic_share_t         466      474          0.9831       0.1835       0.0042           0.7954                           0.1910                 0.1867                 0.0043                     0.8090
  topic_share_t     connectivity_t1         457      474          0.9641       0.4599       0.1814           0.3228                           0.6652                 0.4770                 0.1882                     0.3348
           year      topic_share_t1         367      474          0.7743       0.0570       0.0021           0.7152                           0.0763                 0.0736                 0.0027                     0.9237
  topic_share_t cross_topic_rate_t1         257      474          0.5422       0.4473       0.0000           0.0949                           0.8249                 0.8249                 0.0000                     0.1751
  topic_share_t       modularity_t1         203      474          0.4283       0.0949       0.0506           0.2827                           0.3399                 0.2217                 0.1182                     0.6601
log1p_median_c2 cross_topic_rate_t1         199      474          0.4198       0.2194       0.0401           0.1603                           0.6181                 0.5226                 0.0955                     0.3819
```
