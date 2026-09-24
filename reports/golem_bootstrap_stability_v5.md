# GOLEM Bootstrap Stability (v5)

Topic-block bootstrap: seed=0, requested B=500 per representation. Topics are sampled with replacement; all years and duplicate draws are retained. Sampling matches PC; settings are fixed, with temporal constraints enabled.

Fit configuration: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Threshold: 0.1.

Pairs use alphabetical base-variable order. Rates use all eligible fits, including empty graphs. `a_to_b_rate`, `b_to_a_rate`, and `undirected_rate` sum to `adjacency_rate`; conditional rates divide by adjacent fits only. Orientation frequency and consistency of a particular direction are distinct.

## continuous

```
 n_boot_requested  n_completed  n_succeeded  n_failed  n_nonconverged  n_degenerate_skipped  row_counts_min  row_counts_mean  row_counts_max
              500          500          204         0             296                     0              79         127.7540             177
```

Only converged replicates enter the denominator, including converged empty graphs. Nonconvergence is not evidence for an absent edge. Frequencies describe the converged subset; substantial attrition can bias stability estimates. No stable/unstable cutoff is imposed.

```
                  a               b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1 log1p_median_c2         204      204          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1            year         204      204          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2  topic_share_t1         204      204          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2            year         204      204          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t  topic_share_t1         204      204          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
cross_topic_rate_t1            year         203      204          0.9951       0.0000       0.9951           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2   modularity_t1         203      204          0.9951       0.0000       0.9951           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
     topic_share_t1            year         202      204          0.9902       0.0000       0.9902           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t            year         196      204          0.9608       0.0000       0.9608           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      modularity_t1            year         179      204          0.8775       0.0000       0.8775           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    connectivity_t1   topic_share_t         132      204          0.6471       0.6471       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1 log1p_median_c2          60      204          0.2941       0.2941       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1   topic_share_t          15      204          0.0735       0.0735       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1   topic_share_t           9      204          0.0441       0.0441       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

### Skipped, failed, and nonconverged replicates

```
 replicate       status                  reason
         1 nonconverged Iteration limit reached
         2 nonconverged Iteration limit reached
         3 nonconverged Iteration limit reached
         4 nonconverged Iteration limit reached
         5 nonconverged Iteration limit reached
        11 nonconverged Iteration limit reached
        16 nonconverged Iteration limit reached
        17 nonconverged Iteration limit reached
        19 nonconverged Iteration limit reached
        20 nonconverged Iteration limit reached
        22 nonconverged Iteration limit reached
        23 nonconverged Iteration limit reached
        24 nonconverged Iteration limit reached
        25 nonconverged Iteration limit reached
        26 nonconverged Iteration limit reached
        28 nonconverged Iteration limit reached
        29 nonconverged Iteration limit reached
        30 nonconverged Iteration limit reached
        31 nonconverged Iteration limit reached
        35 nonconverged Iteration limit reached
        36 nonconverged Iteration limit reached
        37 nonconverged Iteration limit reached
        40 nonconverged Iteration limit reached
        41 nonconverged Iteration limit reached
        43 nonconverged Iteration limit reached
        44 nonconverged Iteration limit reached
        46 nonconverged Iteration limit reached
        48 nonconverged Iteration limit reached
        49 nonconverged Iteration limit reached
        50 nonconverged Iteration limit reached
        51 nonconverged Iteration limit reached
        54 nonconverged Iteration limit reached
        56 nonconverged Iteration limit reached
        57 nonconverged Iteration limit reached
        58 nonconverged Iteration limit reached
        59 nonconverged Iteration limit reached
        60 nonconverged Iteration limit reached
        61 nonconverged Iteration limit reached
        63 nonconverged Iteration limit reached
        65 nonconverged Iteration limit reached
        66 nonconverged Iteration limit reached
        68 nonconverged Iteration limit reached
        69 nonconverged Iteration limit reached
        70 nonconverged Iteration limit reached
        73 nonconverged Iteration limit reached
        78 nonconverged Iteration limit reached
        79 nonconverged Iteration limit reached
        80 nonconverged Iteration limit reached
        81 nonconverged Iteration limit reached
        84 nonconverged Iteration limit reached
        86 nonconverged Iteration limit reached
        87 nonconverged Iteration limit reached
        89 nonconverged Iteration limit reached
        90 nonconverged Iteration limit reached
        91 nonconverged Iteration limit reached
        92 nonconverged Iteration limit reached
        94 nonconverged Iteration limit reached
        97 nonconverged Iteration limit reached
        98 nonconverged Iteration limit reached
        99 nonconverged Iteration limit reached
       100 nonconverged Iteration limit reached
       102 nonconverged Iteration limit reached
       104 nonconverged Iteration limit reached
       105 nonconverged Iteration limit reached
       106 nonconverged Iteration limit reached
       107 nonconverged Iteration limit reached
       110 nonconverged Iteration limit reached
       111 nonconverged Iteration limit reached
       113 nonconverged Iteration limit reached
       114 nonconverged Iteration limit reached
       115 nonconverged Iteration limit reached
       117 nonconverged Iteration limit reached
       118 nonconverged Iteration limit reached
       119 nonconverged Iteration limit reached
       121 nonconverged Iteration limit reached
       122 nonconverged Iteration limit reached
       123 nonconverged Iteration limit reached
       125 nonconverged Iteration limit reached
       126 nonconverged Iteration limit reached
       127 nonconverged Iteration limit reached
       129 nonconverged Iteration limit reached
       131 nonconverged Iteration limit reached
       133 nonconverged Iteration limit reached
       134 nonconverged Iteration limit reached
       135 nonconverged Iteration limit reached
       136 nonconverged Iteration limit reached
       138 nonconverged Iteration limit reached
       139 nonconverged Iteration limit reached
       140 nonconverged Iteration limit reached
       147 nonconverged Iteration limit reached
       151 nonconverged Iteration limit reached
       153 nonconverged Iteration limit reached
       157 nonconverged Iteration limit reached
       160 nonconverged Iteration limit reached
       161 nonconverged Iteration limit reached
       162 nonconverged Iteration limit reached
       164 nonconverged Iteration limit reached
       165 nonconverged Iteration limit reached
       166 nonconverged Iteration limit reached
       167 nonconverged Iteration limit reached
       169 nonconverged Iteration limit reached
       170 nonconverged Iteration limit reached
       173 nonconverged Iteration limit reached
       174 nonconverged Iteration limit reached
       175 nonconverged Iteration limit reached
       176 nonconverged Iteration limit reached
       178 nonconverged Iteration limit reached
       179 nonconverged Iteration limit reached
       181 nonconverged Iteration limit reached
       182 nonconverged Iteration limit reached
       183 nonconverged Iteration limit reached
       184 nonconverged Iteration limit reached
       185 nonconverged Iteration limit reached
       187 nonconverged Iteration limit reached
       188 nonconverged Iteration limit reached
       189 nonconverged Iteration limit reached
       190 nonconverged Iteration limit reached
       191 nonconverged Iteration limit reached
       195 nonconverged Iteration limit reached
       196 nonconverged Iteration limit reached
       197 nonconverged Iteration limit reached
       199 nonconverged Iteration limit reached
       201 nonconverged Iteration limit reached
       203 nonconverged Iteration limit reached
       204 nonconverged Iteration limit reached
       205 nonconverged Iteration limit reached
       207 nonconverged Iteration limit reached
       209 nonconverged Iteration limit reached
       210 nonconverged Iteration limit reached
       211 nonconverged Iteration limit reached
       212 nonconverged Iteration limit reached
       213 nonconverged Iteration limit reached
       214 nonconverged Iteration limit reached
       215 nonconverged Iteration limit reached
       216 nonconverged Iteration limit reached
       224 nonconverged Iteration limit reached
       227 nonconverged Iteration limit reached
       229 nonconverged Iteration limit reached
       230 nonconverged Iteration limit reached
       232 nonconverged Iteration limit reached
       234 nonconverged Iteration limit reached
       235 nonconverged Iteration limit reached
       237 nonconverged Iteration limit reached
       238 nonconverged Iteration limit reached
       239 nonconverged Iteration limit reached
       240 nonconverged Iteration limit reached
       242 nonconverged Iteration limit reached
       248 nonconverged Iteration limit reached
       249 nonconverged Iteration limit reached
       250 nonconverged Iteration limit reached
       253 nonconverged Iteration limit reached
       256 nonconverged Iteration limit reached
       257 nonconverged Iteration limit reached
       259 nonconverged Iteration limit reached
       260 nonconverged Iteration limit reached
       263 nonconverged Iteration limit reached
       266 nonconverged Iteration limit reached
       267 nonconverged Iteration limit reached
       268 nonconverged Iteration limit reached
       270 nonconverged Iteration limit reached
       272 nonconverged Iteration limit reached
       273 nonconverged Iteration limit reached
       274 nonconverged Iteration limit reached
       276 nonconverged Iteration limit reached
       277 nonconverged Iteration limit reached
       278 nonconverged Iteration limit reached
       279 nonconverged Iteration limit reached
       280 nonconverged Iteration limit reached
       282 nonconverged Iteration limit reached
       285 nonconverged Iteration limit reached
       287 nonconverged Iteration limit reached
       289 nonconverged Iteration limit reached
       290 nonconverged Iteration limit reached
       291 nonconverged Iteration limit reached
       292 nonconverged Iteration limit reached
       293 nonconverged Iteration limit reached
       294 nonconverged Iteration limit reached
       298 nonconverged Iteration limit reached
       302 nonconverged Iteration limit reached
       304 nonconverged Iteration limit reached
       305 nonconverged Iteration limit reached
       308 nonconverged Iteration limit reached
       309 nonconverged Iteration limit reached
       312 nonconverged Iteration limit reached
       313 nonconverged Iteration limit reached
       316 nonconverged Iteration limit reached
       318 nonconverged Iteration limit reached
       320 nonconverged Iteration limit reached
       321 nonconverged Iteration limit reached
       322 nonconverged Iteration limit reached
       323 nonconverged Iteration limit reached
       324 nonconverged Iteration limit reached
       326 nonconverged Iteration limit reached
       327 nonconverged Iteration limit reached
       328 nonconverged Iteration limit reached
       329 nonconverged Iteration limit reached
       330 nonconverged Iteration limit reached
       331 nonconverged Iteration limit reached
       332 nonconverged Iteration limit reached
       337 nonconverged Iteration limit reached
       339 nonconverged Iteration limit reached
       340 nonconverged Iteration limit reached
       342 nonconverged Iteration limit reached
       343 nonconverged Iteration limit reached
       346 nonconverged Iteration limit reached
       347 nonconverged Iteration limit reached
       349 nonconverged Iteration limit reached
       350 nonconverged Iteration limit reached
       351 nonconverged Iteration limit reached
       354 nonconverged Iteration limit reached
       355 nonconverged Iteration limit reached
       357 nonconverged Iteration limit reached
       358 nonconverged Iteration limit reached
       359 nonconverged Iteration limit reached
       360 nonconverged Iteration limit reached
       361 nonconverged Iteration limit reached
       364 nonconverged Iteration limit reached
       365 nonconverged Iteration limit reached
       366 nonconverged Iteration limit reached
       368 nonconverged Iteration limit reached
       369 nonconverged Iteration limit reached
       370 nonconverged Iteration limit reached
       371 nonconverged Iteration limit reached
       376 nonconverged Iteration limit reached
       377 nonconverged Iteration limit reached
       381 nonconverged Iteration limit reached
       382 nonconverged Iteration limit reached
       385 nonconverged Iteration limit reached
       386 nonconverged Iteration limit reached
       387 nonconverged Iteration limit reached
       389 nonconverged Iteration limit reached
       391 nonconverged Iteration limit reached
       393 nonconverged Iteration limit reached
       396 nonconverged Iteration limit reached
       398 nonconverged Iteration limit reached
       399 nonconverged Iteration limit reached
       400 nonconverged Iteration limit reached
       401 nonconverged Iteration limit reached
       407 nonconverged Iteration limit reached
       408 nonconverged Iteration limit reached
       412 nonconverged Iteration limit reached
       413 nonconverged Iteration limit reached
       414 nonconverged Iteration limit reached
       415 nonconverged Iteration limit reached
       417 nonconverged Iteration limit reached
       418 nonconverged Iteration limit reached
       419 nonconverged Iteration limit reached
       420 nonconverged Iteration limit reached
       423 nonconverged Iteration limit reached
       424 nonconverged Iteration limit reached
       425 nonconverged Iteration limit reached
       426 nonconverged Iteration limit reached
       427 nonconverged Iteration limit reached
       428 nonconverged Iteration limit reached
       429 nonconverged Iteration limit reached
       430 nonconverged Iteration limit reached
       432 nonconverged Iteration limit reached
       433 nonconverged Iteration limit reached
       434 nonconverged Iteration limit reached
       435 nonconverged Iteration limit reached
       437 nonconverged Iteration limit reached
       440 nonconverged Iteration limit reached
       441 nonconverged Iteration limit reached
       446 nonconverged Iteration limit reached
       447 nonconverged Iteration limit reached
       452 nonconverged Iteration limit reached
       453 nonconverged Iteration limit reached
       454 nonconverged Iteration limit reached
       456 nonconverged Iteration limit reached
       457 nonconverged Iteration limit reached
       460 nonconverged Iteration limit reached
       461 nonconverged Iteration limit reached
       463 nonconverged Iteration limit reached
       465 nonconverged Iteration limit reached
       466 nonconverged Iteration limit reached
       467 nonconverged Iteration limit reached
       468 nonconverged Iteration limit reached
       469 nonconverged Iteration limit reached
       470 nonconverged Iteration limit reached
       473 nonconverged Iteration limit reached
       474 nonconverged Iteration limit reached
       475 nonconverged Iteration limit reached
       476 nonconverged Iteration limit reached
       477 nonconverged Iteration limit reached
       479 nonconverged Iteration limit reached
       480 nonconverged Iteration limit reached
       481 nonconverged Iteration limit reached
       482 nonconverged Iteration limit reached
       485 nonconverged Iteration limit reached
       488 nonconverged Iteration limit reached
       489 nonconverged Iteration limit reached
       490 nonconverged Iteration limit reached
       491 nonconverged Iteration limit reached
       493 nonconverged Iteration limit reached
       496 nonconverged Iteration limit reached
       497 nonconverged Iteration limit reached
```

### Cycle conversion and temporal diagnostics

No eligible results.

### Comparison with PC bootstrap

reports\pc_runs\bootstrap_runs_v5.json

```
                  a               b  adjacency_rate_golem  adjacency_rate_pc  a_to_b_rate_golem  a_to_b_rate_pc  b_to_a_rate_golem  b_to_a_rate_pc  undirected_rate_golem  undirected_rate_pc
    connectivity_t1 log1p_median_c2                1.0000             0.0220             1.0000          0.0220             0.0000          0.0000                 0.0000              0.0000
    connectivity_t1   topic_share_t                0.6471             0.0020             0.6471          0.0020             0.0000          0.0000                 0.0000              0.0000
    connectivity_t1            year                1.0000             1.0000             0.0000          0.0000             1.0000          1.0000                 0.0000              0.0000
cross_topic_rate_t1 log1p_median_c2                0.2941             0.4960             0.2941          0.4960             0.0000          0.0000                 0.0000              0.0000
cross_topic_rate_t1   topic_share_t                0.0735             0.0060             0.0735          0.0060             0.0000          0.0000                 0.0000              0.0000
cross_topic_rate_t1            year                0.9951             0.8320             0.0000          0.0000             0.9951          0.8320                 0.0000              0.0000
    log1p_median_c2   modularity_t1                0.9951             0.3700             0.0000          0.0000             0.9951          0.3700                 0.0000              0.0000
    log1p_median_c2  topic_share_t1                1.0000             0.0040             0.0000          0.0000             1.0000          0.0040                 0.0000              0.0000
    log1p_median_c2            year                1.0000             0.9700             0.0000          0.0000             1.0000          0.9700                 0.0000              0.0000
      modularity_t1   topic_share_t                0.0441             0.0560             0.0441          0.0560             0.0000          0.0000                 0.0000              0.0000
      modularity_t1            year                0.8775             0.2980             0.0000          0.0000             0.8775          0.2980                 0.0000              0.0000
      topic_share_t  topic_share_t1                1.0000             1.0000             0.0000          0.0000             1.0000          1.0000                 0.0000              0.0000
      topic_share_t            year                0.9608             0.6840             0.0000          0.0000             0.9608          0.6840                 0.0000              0.0000
     topic_share_t1            year                0.9902             0.0200             0.0000          0.0000             0.9902          0.0200                 0.0000              0.0000
```

Paired comparisons include only replicates successful in both methods with matching row counts. Historical PC files lack input hashes; identical historical inputs cannot be verified independently.

```
 replicate  shared_adjacencies  golem_only  pc_only  jaccard  direction_agreement  direction_reversals  shared_pc_undirected  shared_golem_undirected
         0                   7           5        0   0.5833                    7                    0                     0                        0
         6                   6           4        0   0.6000                    6                    0                     0                        0
         7                   6           4        0   0.6000                    6                    0                     0                        0
         8                   4           5        1   0.4000                    4                    0                     0                        0
         9                   5           5        0   0.5000                    5                    0                     0                        0
        10                   7           5        0   0.5833                    7                    0                     0                        0
        12                   6           5        0   0.5455                    6                    0                     0                        0
        13                   6           5        0   0.5455                    6                    0                     0                        0
        14                   6           4        0   0.6000                    6                    0                     0                        0
        15                   4           7        1   0.3333                    4                    0                     0                        0
        18                   6           5        0   0.5455                    6                    0                     0                        0
        21                   6           4        1   0.5455                    6                    0                     0                        0
        27                   5           6        1   0.4167                    5                    0                     0                        0
        32                   5           8        0   0.3846                    5                    0                     0                        0
        33                   5           5        0   0.5000                    5                    0                     0                        0
        34                   6           5        0   0.5455                    6                    0                     0                        0
        38                   6           6        0   0.5000                    6                    0                     0                        0
        39                   6           6        0   0.5000                    6                    0                     0                        0
        42                   6           4        1   0.5455                    6                    0                     0                        0
        45                   6           5        0   0.5455                    6                    0                     0                        0
        47                   5           5        0   0.5000                    5                    0                     0                        0
        52                   6           5        1   0.5000                    6                    0                     0                        0
        53                   5           6        1   0.4167                    5                    0                     0                        0
        55                   4           5        0   0.4444                    4                    0                     0                        0
        62                   6           6        0   0.5000                    6                    0                     0                        0
        64                   5           5        1   0.4545                    5                    0                     0                        0
        67                   5           6        0   0.4545                    5                    0                     0                        0
        71                   6           5        0   0.5455                    6                    0                     0                        0
        72                   5           5        0   0.5000                    5                    0                     0                        0
        74                   6           4        0   0.6000                    6                    0                     0                        0
        75                   5           5        0   0.5000                    5                    0                     0                        0
        76                   5           5        1   0.4545                    5                    0                     0                        0
        77                   4           8        1   0.3077                    4                    0                     0                        0
        82                   4           6        0   0.4000                    4                    0                     0                        0
        83                   5           8        0   0.3846                    5                    0                     0                        0
        85                   6           6        0   0.5000                    6                    0                     0                        0
        88                   5           6        0   0.4545                    5                    0                     0                        0
        93                   6           4        0   0.6000                    6                    0                     0                        0
        95                   4           7        1   0.3333                    4                    0                     0                        0
        96                   5           8        0   0.3846                    5                    0                     0                        0
       101                   6           5        0   0.5455                    6                    0                     0                        0
       103                   3           6        1   0.3000                    3                    0                     0                        0
       108                   6           5        1   0.5000                    6                    0                     0                        0
       109                   5           6        1   0.4167                    5                    0                     0                        0
       112                   5           6        0   0.4545                    5                    0                     0                        0
       116                   4           8        0   0.3333                    4                    0                     0                        0
       120                   5           6        1   0.4167                    5                    0                     0                        0
       124                   5           6        0   0.4545                    5                    0                     0                        0
       128                   6           6        0   0.5000                    6                    0                     0                        0
       130                   6           6        0   0.5000                    6                    0                     0                        0
       132                   5           6        2   0.3846                    5                    0                     0                        0
       137                   6           6        0   0.5000                    6                    0                     0                        0
       141                   4           7        0   0.3636                    4                    0                     0                        0
       142                   3           5        2   0.3000                    3                    0                     0                        0
       143                   5           6        0   0.4545                    5                    0                     0                        0
       144                   5           6        1   0.4167                    5                    0                     0                        0
       145                   5           4        0   0.5556                    5                    0                     0                        0
       146                   5           6        0   0.4545                    5                    0                     0                        0
       148                   5           6        1   0.4167                    5                    0                     0                        0
       149                   6           4        0   0.6000                    6                    0                     0                        0
       150                   4           7        0   0.3636                    4                    0                     0                        0
       152                   6           5        1   0.5000                    6                    0                     0                        0
       154                   6           4        0   0.6000                    6                    0                     0                        0
       155                   4           6        0   0.4000                    4                    0                     0                        0
       156                   6           6        0   0.5000                    6                    0                     0                        0
       158                   5           7        1   0.3846                    5                    0                     0                        0
       159                   3           7        2   0.2500                    3                    0                     0                        0
       163                   7           5        0   0.5833                    7                    0                     0                        0
       168                   5           5        0   0.5000                    5                    0                     0                        0
       171                   5           7        0   0.4167                    5                    0                     0                        0
       172                   5           8        0   0.3846                    5                    0                     0                        0
       177                   5           5        0   0.5000                    5                    0                     0                        0
       180                   6           4        0   0.6000                    6                    0                     0                        0
       186                   5           6        1   0.4167                    5                    0                     0                        0
       192                   6           5        1   0.5000                    6                    0                     0                        0
       193                   5           6        1   0.4167                    5                    0                     0                        0
       194                   4           6        0   0.4000                    4                    0                     0                        0
       198                   5           6        1   0.4167                    5                    0                     0                        0
       200                   6           5        1   0.5000                    6                    0                     0                        0
       202                   6           4        0   0.6000                    6                    0                     0                        0
       206                   3           8        0   0.2727                    3                    0                     0                        0
       208                   4           5        1   0.4000                    4                    0                     0                        0
       217                   7           4        0   0.6364                    7                    0                     0                        0
       218                   6           6        0   0.5000                    6                    0                     0                        0
       219                   5           6        1   0.4167                    5                    0                     0                        0
       220                   6           5        0   0.5455                    6                    0                     0                        0
       221                   6           6        0   0.5000                    6                    0                     0                        0
       222                   6           5        0   0.5455                    6                    0                     0                        0
       223                   6           5        1   0.5000                    6                    0                     0                        0
       225                   5           6        1   0.4167                    5                    0                     0                        0
       226                   3           7        1   0.2727                    3                    0                     0                        0
       228                   6           6        0   0.5000                    6                    0                     0                        0
       231                   4           8        1   0.3077                    4                    0                     0                        0
       233                   5           5        0   0.5000                    5                    0                     0                        0
       236                   5           6        0   0.4545                    5                    0                     0                        0
       241                   5           6        0   0.4545                    5                    0                     0                        0
       243                   5           6        0   0.4545                    5                    0                     0                        0
       244                   5           8        0   0.3846                    5                    0                     0                        0
       245                   6           4        1   0.5455                    6                    0                     0                        0
       246                   6           6        0   0.5000                    6                    0                     0                        0
       247                   4           8        1   0.3077                    4                    0                     0                        0
       251                   5           5        0   0.5000                    5                    0                     0                        0
       252                   4           7        1   0.3333                    4                    0                     0                        0
       254                   6           5        0   0.5455                    6                    0                     0                        0
       255                   5           6        1   0.4167                    5                    0                     0                        0
       258                   6           5        0   0.5455                    6                    0                     0                        0
       261                   6           6        0   0.5000                    6                    0                     0                        0
       262                   5           6        1   0.4167                    5                    0                     0                        0
       264                   6           5        0   0.5455                    6                    0                     0                        0
       265                   5           6        0   0.4545                    5                    0                     0                        0
       269                   7           4        0   0.6364                    7                    0                     0                        0
       271                   4           5        1   0.4000                    4                    0                     0                        0
       275                   4           7        0   0.3636                    4                    0                     0                        0
       281                   4           7        0   0.3636                    4                    0                     0                        0
       283                   6           5        1   0.5000                    6                    0                     0                        0
       284                   4           6        1   0.3636                    4                    0                     0                        0
       286                   5           6        0   0.4545                    5                    0                     0                        0
       288                   4           7        0   0.3636                    4                    0                     0                        0
       295                   6           6        0   0.5000                    6                    0                     0                        0
       296                   5           5        1   0.4545                    5                    0                     0                        0
       297                   6           5        0   0.5455                    6                    0                     0                        0
       299                   6           5        0   0.5455                    6                    0                     0                        0
       300                   5           6        0   0.4545                    5                    0                     0                        0
       301                   6           4        1   0.5455                    6                    0                     0                        0
       303                   5           6        1   0.4167                    5                    0                     0                        0
       306                   6           5        0   0.5455                    6                    0                     0                        0
       307                   5           5        0   0.5000                    5                    0                     0                        0
       310                   5           6        0   0.4545                    5                    0                     0                        0
       311                   6           4        0   0.6000                    6                    0                     0                        0
       314                   3           7        1   0.2727                    3                    0                     0                        0
       315                   6           6        0   0.5000                    6                    0                     0                        0
       317                   6           5        0   0.5455                    6                    0                     0                        0
       319                   5           5        0   0.5000                    5                    0                     0                        0
       325                   6           5        0   0.5455                    6                    0                     0                        0
       333                   7           5        0   0.5833                    7                    0                     0                        0
       334                   5           6        0   0.4545                    5                    0                     0                        0
       335                   6           5        0   0.5455                    6                    0                     0                        0
       336                   6           5        0   0.5455                    6                    0                     0                        0
       338                   5           6        1   0.4167                    5                    0                     0                        0
       341                   6           5        0   0.5455                    6                    0                     0                        0
       344                   5           6        1   0.4167                    5                    0                     0                        0
       345                   6           4        0   0.6000                    6                    0                     0                        0
       348                   6           5        0   0.5455                    6                    0                     0                        0
       352                   6           5        0   0.5455                    6                    0                     0                        0
       353                   5           6        0   0.4545                    5                    0                     0                        0
       356                   5           6        1   0.4167                    5                    0                     0                        0
       362                   5           7        0   0.4167                    5                    0                     0                        0
       363                   3           8        1   0.2500                    3                    0                     0                        0
       367                   5           5        0   0.5000                    5                    0                     0                        0
       372                   7           4        0   0.6364                    7                    0                     0                        0
       373                   6           4        0   0.6000                    6                    0                     0                        0
       374                   6           6        0   0.5000                    6                    0                     0                        0
       375                   6           7        0   0.4615                    6                    0                     0                        0
       378                   6           5        1   0.5000                    6                    0                     0                        0
       379                   6           5        0   0.5455                    6                    0                     0                        0
       380                   5           6        1   0.4167                    5                    0                     0                        0
       383                   6           6        0   0.5000                    6                    0                     0                        0
       384                   5           5        1   0.4545                    5                    0                     0                        0
       388                   5           5        1   0.4545                    5                    0                     0                        0
       390                   6           6        0   0.5000                    6                    0                     0                        0
       392                   6           5        0   0.5455                    6                    0                     0                        0
       394                   5           5        1   0.4545                    5                    0                     0                        0
       395                   6           4        1   0.5455                    6                    0                     0                        0
       397                   5           5        0   0.5000                    5                    0                     0                        0
       402                   5           6        0   0.4545                    5                    0                     0                        0
       403                   4           7        1   0.3333                    4                    0                     0                        0
       404                   6           4        0   0.6000                    6                    0                     0                        0
       405                   4           6        0   0.4000                    4                    0                     0                        0
       406                   5           6        1   0.4167                    5                    0                     0                        0
       409                   4           6        1   0.3636                    4                    0                     0                        0
       410                   4           6        1   0.3636                    4                    0                     0                        0
       411                   6           5        0   0.5455                    6                    0                     0                        0
       416                   4           6        1   0.3636                    4                    0                     0                        0
       421                   5           6        1   0.4167                    5                    0                     0                        0
       422                   5           6        1   0.4167                    5                    0                     0                        0
       431                   5           7        0   0.4167                    5                    0                     0                        0
       436                   4           6        1   0.3636                    4                    0                     0                        0
       438                   5           6        1   0.4167                    5                    0                     0                        0
       439                   7           5        0   0.5833                    7                    0                     0                        0
       442                   5           7        0   0.4167                    5                    0                     0                        0
       443                   6           4        0   0.6000                    6                    0                     0                        0
       444                   5           6        0   0.4545                    5                    0                     0                        0
       445                   6           6        0   0.5000                    6                    0                     0                        0
       448                   5           7        0   0.4167                    5                    0                     0                        0
       449                   6           4        0   0.6000                    6                    0                     0                        0
       450                   5           5        1   0.4545                    5                    0                     0                        0
       451                   6           4        1   0.5455                    6                    0                     0                        0
       455                   7           4        0   0.6364                    7                    0                     0                        0
       458                   6           6        0   0.5000                    6                    0                     0                        0
       459                   3           7        1   0.2727                    3                    0                     0                        0
       462                   7           4        0   0.6364                    7                    0                     0                        0
       464                   4           7        0   0.3636                    4                    0                     0                        0
       471                   5           5        1   0.4545                    5                    0                     0                        0
       472                   6           6        0   0.5000                    6                    0                     0                        0
       478                   4           6        2   0.3333                    4                    0                     0                        0
       483                   4           5        1   0.4000                    4                    0                     0                        0
       484                   6           5        0   0.5455                    6                    0                     0                        0
       486                   5           5        0   0.5000                    5                    0                     0                        0
       487                   5           7        1   0.3846                    5                    0                     0                        0
       492                   5           7        0   0.4167                    5                    0                     0                        0
       494                   5           6        0   0.4545                    5                    0                     0                        0
       495                   6           5        1   0.5000                    6                    0                     0                        0
       498                   4           6        0   0.4000                    4                    0                     0                        0
       499                   6           5        0   0.5455                    6                    0                     0                        0
```

## discretized

```
 n_boot_requested  n_completed  n_succeeded  n_failed  n_nonconverged  n_degenerate_skipped  row_counts_min  row_counts_mean  row_counts_max
              500          500          500         0               0                     0              79         127.7540             177
```

Only converged replicates enter the denominator, including converged empty graphs. Nonconvergence is not evidence for an absent edge. Frequencies describe the converged subset; substantial attrition can bias stability estimates. No stable/unstable cutoff is imposed.

```
                  a               b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1 log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1   topic_share_t         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1            year         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
cross_topic_rate_t1 log1p_median_c2         500      500          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1            year         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2   modularity_t1         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2            year         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      modularity_t1            year         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t  topic_share_t1         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t            year         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
     topic_share_t1            year         500      500          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2  topic_share_t1         499      500          0.9980       0.0000       0.9980           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      modularity_t1   topic_share_t         497      500          0.9940       0.9940       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1   topic_share_t         495      500          0.9900       0.9900       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

### Cycle conversion and temporal diagnostics

No eligible results.

### Comparison with PC bootstrap

reports\pc_runs\bootstrap_runs_v5.json

```
                  a               b  adjacency_rate_golem  adjacency_rate_pc  a_to_b_rate_golem  a_to_b_rate_pc  b_to_a_rate_golem  b_to_a_rate_pc  undirected_rate_golem  undirected_rate_pc
    connectivity_t1 log1p_median_c2                1.0000             0.5960             1.0000          0.5960             0.0000          0.0000                 0.0000              0.0000
    connectivity_t1   topic_share_t                1.0000             0.3280             1.0000          0.3280             0.0000          0.0000                 0.0000              0.0000
    connectivity_t1            year                1.0000             0.9340             0.0000          0.0000             1.0000          0.9340                 0.0000              0.0000
cross_topic_rate_t1 log1p_median_c2                1.0000             0.7840             1.0000          0.7840             0.0000          0.0000                 0.0000              0.0000
cross_topic_rate_t1   topic_share_t                0.9900             0.3160             0.9900          0.3160             0.0000          0.0000                 0.0000              0.0000
cross_topic_rate_t1            year                1.0000             0.7220             0.0000          0.0000             1.0000          0.7220                 0.0000              0.0000
    log1p_median_c2   modularity_t1                1.0000             0.5060             0.0000          0.0000             1.0000          0.5060                 0.0000              0.0000
    log1p_median_c2  topic_share_t1                0.9980             0.1600             0.0000          0.0000             0.9980          0.1600                 0.0000              0.0000
    log1p_median_c2            year                1.0000             0.9000             0.0000          0.0000             1.0000          0.9000                 0.0000              0.0000
      modularity_t1   topic_share_t                0.9940             0.0780             0.9940          0.0780             0.0000          0.0000                 0.0000              0.0000
      modularity_t1            year                1.0000             0.5660             0.0000          0.0000             1.0000          0.5660                 0.0000              0.0000
      topic_share_t  topic_share_t1                1.0000             1.0000             0.0000          0.0000             1.0000          1.0000                 0.0000              0.0000
      topic_share_t            year                1.0000             0.3640             0.0000          0.0000             1.0000          0.3640                 0.0000              0.0000
     topic_share_t1            year                1.0000             0.6200             0.0000          0.0000             1.0000          0.6200                 0.0000              0.0000
```

Paired comparisons include only replicates successful in both methods with matching row counts. Historical PC files lack input hashes; identical historical inputs cannot be verified independently.

```
 replicate  shared_adjacencies  golem_only  pc_only  jaccard  direction_agreement  direction_reversals  shared_pc_undirected  shared_golem_undirected
         0                  10           4        0   0.7143                   10                    0                     0                        0
         1                   8           6        0   0.5714                    8                    0                     0                        0
         2                   8           6        0   0.5714                    8                    0                     0                        0
         3                   7           7        0   0.5000                    7                    0                     0                        0
         4                  11           3        0   0.7857                   11                    0                     0                        0
         5                   6           8        0   0.4286                    6                    0                     0                        0
         6                   9           5        0   0.6429                    9                    0                     0                        0
         7                   9           5        0   0.6429                    9                    0                     0                        0
         8                   8           6        0   0.5714                    8                    0                     0                        0
         9                   7           7        0   0.5000                    7                    0                     0                        0
        10                   8           6        0   0.5714                    8                    0                     0                        0
        11                   9           5        0   0.6429                    9                    0                     0                        0
        12                   9           5        0   0.6429                    9                    0                     0                        0
        13                   9           5        0   0.6429                    9                    0                     0                        0
        14                   9           5        0   0.6429                    9                    0                     0                        0
        15                   7           7        0   0.5000                    7                    0                     0                        0
        16                   8           6        0   0.5714                    8                    0                     0                        0
        17                  12           2        0   0.8571                   12                    0                     0                        0
        18                  11           3        0   0.7857                   11                    0                     0                        0
        19                   7           7        0   0.5000                    7                    0                     0                        0
        20                   8           6        0   0.5714                    8                    0                     0                        0
        21                   8           6        0   0.5714                    8                    0                     0                        0
        22                   8           6        0   0.5714                    8                    0                     0                        0
        23                   7           7        0   0.5000                    7                    0                     0                        0
        24                   9           5        0   0.6429                    9                    0                     0                        0
        25                   9           5        0   0.6429                    9                    0                     0                        0
        26                   8           6        0   0.5714                    8                    0                     0                        0
        27                   7           7        0   0.5000                    7                    0                     0                        0
        28                   7           7        0   0.5000                    7                    0                     0                        0
        29                   7           7        0   0.5000                    7                    0                     0                        0
        30                   8           6        0   0.5714                    8                    0                     0                        0
        31                   8           6        0   0.5714                    8                    0                     0                        0
        32                   8           6        0   0.5714                    8                    0                     0                        0
        33                   7           7        0   0.5000                    7                    0                     0                        0
        34                   8           6        0   0.5714                    8                    0                     0                        0
        35                  10           4        0   0.7143                   10                    0                     0                        0
        36                  10           4        0   0.7143                   10                    0                     0                        0
        37                   8           6        0   0.5714                    8                    0                     0                        0
        38                   6           8        0   0.4286                    6                    0                     0                        0
        39                   9           5        0   0.6429                    9                    0                     0                        0
        40                   5           9        0   0.3571                    5                    0                     0                        0
        41                  12           2        0   0.8571                   12                    0                     0                        0
        42                  10           4        0   0.7143                   10                    0                     0                        0
        43                   7           7        0   0.5000                    7                    0                     0                        0
        44                   6           8        0   0.4286                    6                    0                     0                        0
        45                  10           4        0   0.7143                   10                    0                     0                        0
        46                   8           6        0   0.5714                    8                    0                     0                        0
        47                   7           7        0   0.5000                    7                    0                     0                        0
        48                   9           5        0   0.6429                    9                    0                     0                        0
        49                   8           6        0   0.5714                    8                    0                     0                        0
        50                  10           4        0   0.7143                   10                    0                     0                        0
        51                   6           8        0   0.4286                    6                    0                     0                        0
        52                  11           3        0   0.7857                   11                    0                     0                        0
        53                   9           5        0   0.6429                    9                    0                     0                        0
        54                   4          10        0   0.2857                    4                    0                     0                        0
        55                   9           5        0   0.6429                    9                    0                     0                        0
        56                   8           6        0   0.5714                    8                    0                     0                        0
        57                   7           7        0   0.5000                    7                    0                     0                        0
        58                   7           6        0   0.5385                    7                    0                     0                        0
        59                   9           5        0   0.6429                    9                    0                     0                        0
        60                  11           3        0   0.7857                   11                    0                     0                        0
        61                   7           7        0   0.5000                    7                    0                     0                        0
        62                   8           6        0   0.5714                    8                    0                     0                        0
        63                   8           6        0   0.5714                    8                    0                     0                        0
        64                   7           7        0   0.5000                    7                    0                     0                        0
        65                   8           6        0   0.5714                    8                    0                     0                        0
        66                  12           2        0   0.8571                   12                    0                     0                        0
        67                   7           7        0   0.5000                    7                    0                     0                        0
        68                   9           5        0   0.6429                    9                    0                     0                        0
        69                   7           7        0   0.5000                    7                    0                     0                        0
        70                   8           6        0   0.5714                    8                    0                     0                        0
        71                   8           6        0   0.5714                    8                    0                     0                        0
        72                   9           5        0   0.6429                    9                    0                     0                        0
        73                   7           7        0   0.5000                    7                    0                     0                        0
        74                   8           6        0   0.5714                    8                    0                     0                        0
        75                   4          10        0   0.2857                    4                    0                     0                        0
        76                   9           5        0   0.6429                    9                    0                     0                        0
        77                   7           7        0   0.5000                    7                    0                     0                        0
        78                   5           9        0   0.3571                    5                    0                     0                        0
        79                   7           7        0   0.5000                    7                    0                     0                        0
        80                   9           5        0   0.6429                    9                    0                     0                        0
        81                   9           5        0   0.6429                    9                    0                     0                        0
        82                   8           6        0   0.5714                    8                    0                     0                        0
        83                   6           8        0   0.4286                    6                    0                     0                        0
        84                   8           6        0   0.5714                    8                    0                     0                        0
        85                   9           5        0   0.6429                    9                    0                     0                        0
        86                   6           8        0   0.4286                    6                    0                     0                        0
        87                   9           5        0   0.6429                    9                    0                     0                        0
        88                   7           7        0   0.5000                    7                    0                     0                        0
        89                  11           3        0   0.7857                   11                    0                     0                        0
        90                   9           5        0   0.6429                    9                    0                     0                        0
        91                   8           6        0   0.5714                    8                    0                     0                        0
        92                   8           6        0   0.5714                    8                    0                     0                        0
        93                   9           5        0   0.6429                    9                    0                     0                        0
        94                   7           7        0   0.5000                    7                    0                     0                        0
        95                   9           5        0   0.6429                    9                    0                     0                        0
        96                   9           5        0   0.6429                    9                    0                     0                        0
        97                   8           6        0   0.5714                    8                    0                     0                        0
        98                   6           8        0   0.4286                    6                    0                     0                        0
        99                   4          10        0   0.2857                    4                    0                     0                        0
       100                   8           5        0   0.6154                    8                    0                     0                        0
       101                   6           8        0   0.4286                    6                    0                     0                        0
       102                   6           8        0   0.4286                    6                    0                     0                        0
       103                   6           8        0   0.4286                    6                    0                     0                        0
       104                   8           6        0   0.5714                    8                    0                     0                        0
       105                   9           5        0   0.6429                    9                    0                     0                        0
       106                   9           5        0   0.6429                    9                    0                     0                        0
       107                   7           6        0   0.5385                    7                    0                     0                        0
       108                   7           7        0   0.5000                    7                    0                     0                        0
       109                   7           7        0   0.5000                    7                    0                     0                        0
       110                  11           3        0   0.7857                   11                    0                     0                        0
       111                   6           8        0   0.4286                    6                    0                     0                        0
       112                   6           8        0   0.4286                    6                    0                     0                        0
       113                   9           5        0   0.6429                    9                    0                     0                        0
       114                   6           8        0   0.4286                    6                    0                     0                        0
       115                   7           7        0   0.5000                    7                    0                     0                        0
       116                   6           8        0   0.4286                    6                    0                     0                        0
       117                   9           5        0   0.6429                    9                    0                     0                        0
       118                   9           5        0   0.6429                    9                    0                     0                        0
       119                   6           8        0   0.4286                    6                    0                     0                        0
       120                  10           4        0   0.7143                   10                    0                     0                        0
       121                   8           6        0   0.5714                    8                    0                     0                        0
       122                   7           7        0   0.5000                    7                    0                     0                        0
       123                   6           8        0   0.4286                    6                    0                     0                        0
       124                   8           6        0   0.5714                    8                    0                     0                        0
       125                   8           6        0   0.5714                    8                    0                     0                        0
       126                   6           8        0   0.4286                    6                    0                     0                        0
       127                   8           6        0   0.5714                    8                    0                     0                        0
       128                   7           7        0   0.5000                    7                    0                     0                        0
       129                   6           8        0   0.4286                    6                    0                     0                        0
       130                   7           7        0   0.5000                    7                    0                     0                        0
       131                  11           3        0   0.7857                   11                    0                     0                        0
       132                   8           6        0   0.5714                    8                    0                     0                        0
       133                   8           6        0   0.5714                    8                    0                     0                        0
       134                  11           3        0   0.7857                   11                    0                     0                        0
       135                   8           6        0   0.5714                    8                    0                     0                        0
       136                   5           9        0   0.3571                    5                    0                     0                        0
       137                   6           8        0   0.4286                    6                    0                     0                        0
       138                   6           8        0   0.4286                    6                    0                     0                        0
       139                   6           8        0   0.4286                    6                    0                     0                        0
       140                   8           6        0   0.5714                    8                    0                     0                        0
       141                   8           6        0   0.5714                    8                    0                     0                        0
       142                   5           9        0   0.3571                    5                    0                     0                        0
       143                   7           7        0   0.5000                    7                    0                     0                        0
       144                   9           5        0   0.6429                    9                    0                     0                        0
       145                   8           6        0   0.5714                    8                    0                     0                        0
       146                   7           6        0   0.5385                    7                    0                     0                        0
       147                   7           7        0   0.5000                    7                    0                     0                        0
       148                   6           8        0   0.4286                    6                    0                     0                        0
       149                   7           7        0   0.5000                    7                    0                     0                        0
       150                   5           9        0   0.3571                    5                    0                     0                        0
       151                   8           6        0   0.5714                    8                    0                     0                        0
       152                   8           6        0   0.5714                    8                    0                     0                        0
       153                  10           4        0   0.7143                   10                    0                     0                        0
       154                   8           6        0   0.5714                    8                    0                     0                        0
       155                   6           8        0   0.4286                    6                    0                     0                        0
       156                   8           6        0   0.5714                    8                    0                     0                        0
       157                   5           9        0   0.3571                    5                    0                     0                        0
       158                   7           7        0   0.5000                    7                    0                     0                        0
       159                  11           3        0   0.7857                   11                    0                     0                        0
       160                   9           5        0   0.6429                    9                    0                     0                        0
       161                  12           2        0   0.8571                   12                    0                     0                        0
       162                   6           8        0   0.4286                    6                    0                     0                        0
       163                   9           4        0   0.6923                    9                    0                     0                        0
       164                   9           5        0   0.6429                    9                    0                     0                        0
       165                  11           3        0   0.7857                   11                    0                     0                        0
       166                   7           7        0   0.5000                    7                    0                     0                        0
       167                   9           5        0   0.6429                    9                    0                     0                        0
       168                  10           4        0   0.7143                   10                    0                     0                        0
       169                   9           5        0   0.6429                    9                    0                     0                        0
       170                   9           5        0   0.6429                    9                    0                     0                        0
       171                   6           8        0   0.4286                    6                    0                     0                        0
       172                  10           4        0   0.7143                   10                    0                     0                        0
       173                   9           5        0   0.6429                    9                    0                     0                        0
       174                   8           6        0   0.5714                    8                    0                     0                        0
       175                   8           6        0   0.5714                    8                    0                     0                        0
       176                   6           8        0   0.4286                    6                    0                     0                        0
       177                   7           7        0   0.5000                    7                    0                     0                        0
       178                   7           7        0   0.5000                    7                    0                     0                        0
       179                   6           8        0   0.4286                    6                    0                     0                        0
       180                   9           5        0   0.6429                    9                    0                     0                        0
       181                  12           2        0   0.8571                   12                    0                     0                        0
       182                   8           6        0   0.5714                    8                    0                     0                        0
       183                   8           6        0   0.5714                    8                    0                     0                        0
       184                   7           7        0   0.5000                    7                    0                     0                        0
       185                   8           6        0   0.5714                    8                    0                     0                        0
       186                   6           8        0   0.4286                    6                    0                     0                        0
       187                   8           6        0   0.5714                    8                    0                     0                        0
       188                   9           5        0   0.6429                    9                    0                     0                        0
       189                   8           6        0   0.5714                    8                    0                     0                        0
       190                   8           6        0   0.5714                    8                    0                     0                        0
       191                   9           5        0   0.6429                    9                    0                     0                        0
       192                  12           2        0   0.8571                   12                    0                     0                        0
       193                   8           6        0   0.5714                    8                    0                     0                        0
       194                   8           6        0   0.5714                    8                    0                     0                        0
       195                   9           5        0   0.6429                    9                    0                     0                        0
       196                   5           9        0   0.3571                    5                    0                     0                        0
       197                   5           9        0   0.3571                    5                    0                     0                        0
       198                   8           6        0   0.5714                    8                    0                     0                        0
       199                  10           4        0   0.7143                   10                    0                     0                        0
       200                   8           6        0   0.5714                    8                    0                     0                        0
       201                   8           6        0   0.5714                    8                    0                     0                        0
       202                  11           3        0   0.7857                   11                    0                     0                        0
       203                   8           6        0   0.5714                    8                    0                     0                        0
       204                   7           7        0   0.5000                    7                    0                     0                        0
       205                   7           7        0   0.5000                    7                    0                     0                        0
       206                   7           7        0   0.5000                    7                    0                     0                        0
       207                   8           6        0   0.5714                    8                    0                     0                        0
       208                   7           7        0   0.5000                    7                    0                     0                        0
       209                   9           5        0   0.6429                    9                    0                     0                        0
       210                   6           8        0   0.4286                    6                    0                     0                        0
       211                   6           8        0   0.4286                    6                    0                     0                        0
       212                  10           4        0   0.7143                   10                    0                     0                        0
       213                   6           8        0   0.4286                    6                    0                     0                        0
       214                   7           7        0   0.5000                    7                    0                     0                        0
       215                   6           8        0   0.4286                    6                    0                     0                        0
       216                   5           9        0   0.3571                    5                    0                     0                        0
       217                   9           5        0   0.6429                    9                    0                     0                        0
       218                  11           3        0   0.7857                   11                    0                     0                        0
       219                   7           7        0   0.5000                    7                    0                     0                        0
       220                   6           8        0   0.4286                    6                    0                     0                        0
       221                   9           5        0   0.6429                    9                    0                     0                        0
       222                  10           4        0   0.7143                   10                    0                     0                        0
       223                   7           7        0   0.5000                    7                    0                     0                        0
       224                   7           7        0   0.5000                    7                    0                     0                        0
       225                   8           6        0   0.5714                    8                    0                     0                        0
       226                   6           8        0   0.4286                    6                    0                     0                        0
       227                   7           7        0   0.5000                    7                    0                     0                        0
       228                   9           5        0   0.6429                    9                    0                     0                        0
       229                   7           7        0   0.5000                    7                    0                     0                        0
       230                   6           8        0   0.4286                    6                    0                     0                        0
       231                   7           7        0   0.5000                    7                    0                     0                        0
       232                   9           5        0   0.6429                    9                    0                     0                        0
       233                  11           3        0   0.7857                   11                    0                     0                        0
       234                   9           5        0   0.6429                    9                    0                     0                        0
       235                   5           9        0   0.3571                    5                    0                     0                        0
       236                   9           5        0   0.6429                    9                    0                     0                        0
       237                   7           7        0   0.5000                    7                    0                     0                        0
       238                   7           7        0   0.5000                    7                    0                     0                        0
       239                   7           7        0   0.5000                    7                    0                     0                        0
       240                   7           7        0   0.5000                    7                    0                     0                        0
       241                   4          10        0   0.2857                    4                    0                     0                        0
       242                   9           5        0   0.6429                    9                    0                     0                        0
       243                   7           7        0   0.5000                    7                    0                     0                        0
       244                   9           5        0   0.6429                    9                    0                     0                        0
       245                   8           6        0   0.5714                    8                    0                     0                        0
       246                   6           8        0   0.4286                    6                    0                     0                        0
       247                   9           5        0   0.6429                    9                    0                     0                        0
       248                   7           7        0   0.5000                    7                    0                     0                        0
       249                   6           8        0   0.4286                    6                    0                     0                        0
       250                   5           9        0   0.3571                    5                    0                     0                        0
       251                   6           8        0   0.4286                    6                    0                     0                        0
       252                   6           8        0   0.4286                    6                    0                     0                        0
       253                   9           5        0   0.6429                    9                    0                     0                        0
       254                   8           6        0   0.5714                    8                    0                     0                        0
       255                   8           6        0   0.5714                    8                    0                     0                        0
       256                   7           7        0   0.5000                    7                    0                     0                        0
       257                   4          10        0   0.2857                    4                    0                     0                        0
       258                   8           6        0   0.5714                    8                    0                     0                        0
       259                   8           6        0   0.5714                    8                    0                     0                        0
       260                  10           4        0   0.7143                   10                    0                     0                        0
       261                  10           4        0   0.7143                   10                    0                     0                        0
       262                   8           6        0   0.5714                    8                    0                     0                        0
       263                   8           6        0   0.5714                    8                    0                     0                        0
       264                   7           7        0   0.5000                    7                    0                     0                        0
       265                   5           9        0   0.3571                    5                    0                     0                        0
       266                   9           5        0   0.6429                    9                    0                     0                        0
       267                   7           7        0   0.5000                    7                    0                     0                        0
       268                   7           7        0   0.5000                    7                    0                     0                        0
       269                  10           4        0   0.7143                   10                    0                     0                        0
       270                  10           4        0   0.7143                   10                    0                     0                        0
       271                   7           7        0   0.5000                    7                    0                     0                        0
       272                   9           5        0   0.6429                    9                    0                     0                        0
       273                  10           4        0   0.7143                   10                    0                     0                        0
       274                  11           3        0   0.7857                   11                    0                     0                        0
       275                   6           8        0   0.4286                    6                    0                     0                        0
       276                   7           7        0   0.5000                    7                    0                     0                        0
       277                   7           7        0   0.5000                    7                    0                     0                        0
       278                   7           7        0   0.5000                    7                    0                     0                        0
       279                   7           7        0   0.5000                    7                    0                     0                        0
       280                   9           5        0   0.6429                    9                    0                     0                        0
       281                   5           9        0   0.3571                    5                    0                     0                        0
       282                   8           6        0   0.5714                    8                    0                     0                        0
       283                   9           5        0   0.6429                    9                    0                     0                        0
       284                   6           8        0   0.4286                    6                    0                     0                        0
       285                   5           9        0   0.3571                    5                    0                     0                        0
       286                   7           7        0   0.5000                    7                    0                     0                        0
       287                   7           6        0   0.5385                    7                    0                     0                        0
       288                   5           9        0   0.3571                    5                    0                     0                        0
       289                  10           4        0   0.7143                   10                    0                     0                        0
       290                   8           6        0   0.5714                    8                    0                     0                        0
       291                   7           7        0   0.5000                    7                    0                     0                        0
       292                   8           6        0   0.5714                    8                    0                     0                        0
       293                   8           6        0   0.5714                    8                    0                     0                        0
       294                   6           8        0   0.4286                    6                    0                     0                        0
       295                   9           5        0   0.6429                    9                    0                     0                        0
       296                   7           7        0   0.5000                    7                    0                     0                        0
       297                   6           8        0   0.4286                    6                    0                     0                        0
       298                  10           4        0   0.7143                   10                    0                     0                        0
       299                  10           4        0   0.7143                   10                    0                     0                        0
       300                   7           7        0   0.5000                    7                    0                     0                        0
       301                   7           7        0   0.5000                    7                    0                     0                        0
       302                   6           8        0   0.4286                    6                    0                     0                        0
       303                   8           6        0   0.5714                    8                    0                     0                        0
       304                   9           5        0   0.6429                    9                    0                     0                        0
       305                  10           4        0   0.7143                   10                    0                     0                        0
       306                   9           5        0   0.6429                    9                    0                     0                        0
       307                   5           9        0   0.3571                    5                    0                     0                        0
       308                   9           5        0   0.6429                    9                    0                     0                        0
       309                   8           6        0   0.5714                    8                    0                     0                        0
       310                   5           9        0   0.3571                    5                    0                     0                        0
       311                  10           4        0   0.7143                   10                    0                     0                        0
       312                   9           5        0   0.6429                    9                    0                     0                        0
       313                   5           9        0   0.3571                    5                    0                     0                        0
       314                   4          10        0   0.2857                    4                    0                     0                        0
       315                   7           7        0   0.5000                    7                    0                     0                        0
       316                   5           9        0   0.3571                    5                    0                     0                        0
       317                   9           5        0   0.6429                    9                    0                     0                        0
       318                  12           2        0   0.8571                   12                    0                     0                        0
       319                   7           7        0   0.5000                    7                    0                     0                        0
       320                   8           6        0   0.5714                    8                    0                     0                        0
       321                   9           5        0   0.6429                    9                    0                     0                        0
       322                   5           9        0   0.3571                    5                    0                     0                        0
       323                   6           8        0   0.4286                    6                    0                     0                        0
       324                   7           7        0   0.5000                    7                    0                     0                        0
       325                   8           6        0   0.5714                    8                    0                     0                        0
       326                   8           6        0   0.5714                    8                    0                     0                        0
       327                  10           4        0   0.7143                   10                    0                     0                        0
       328                   8           6        0   0.5714                    8                    0                     0                        0
       329                   8           6        0   0.5714                    8                    0                     0                        0
       330                   7           7        0   0.5000                    7                    0                     0                        0
       331                   8           6        0   0.5714                    8                    0                     0                        0
       332                   7           7        0   0.5000                    7                    0                     0                        0
       333                   7           7        0   0.5000                    7                    0                     0                        0
       334                   4          10        0   0.2857                    4                    0                     0                        0
       335                   6           8        0   0.4286                    6                    0                     0                        0
       336                   9           5        0   0.6429                    9                    0                     0                        0
       337                   8           6        0   0.5714                    8                    0                     0                        0
       338                   6           8        0   0.4286                    6                    0                     0                        0
       339                  10           4        0   0.7143                   10                    0                     0                        0
       340                   7           7        0   0.5000                    7                    0                     0                        0
       341                   8           6        0   0.5714                    8                    0                     0                        0
       342                   6           8        0   0.4286                    6                    0                     0                        0
       343                   3          11        0   0.2143                    3                    0                     0                        0
       344                  10           4        0   0.7143                   10                    0                     0                        0
       345                   9           5        0   0.6429                    9                    0                     0                        0
       346                   7           7        0   0.5000                    7                    0                     0                        0
       347                   8           6        0   0.5714                    8                    0                     0                        0
       348                   9           5        0   0.6429                    9                    0                     0                        0
       349                   8           6        0   0.5714                    8                    0                     0                        0
       350                   9           5        0   0.6429                    9                    0                     0                        0
       351                   3          11        0   0.2143                    3                    0                     0                        0
       352                  10           4        0   0.7143                   10                    0                     0                        0
       353                   7           7        0   0.5000                    7                    0                     0                        0
       354                  11           3        0   0.7857                   11                    0                     0                        0
       355                   8           6        0   0.5714                    8                    0                     0                        0
       356                   9           5        0   0.6429                    9                    0                     0                        0
       357                  10           4        0   0.7143                   10                    0                     0                        0
       358                  10           4        0   0.7143                   10                    0                     0                        0
       359                   9           5        0   0.6429                    9                    0                     0                        0
       360                   8           6        0   0.5714                    8                    0                     0                        0
       361                   6           8        0   0.4286                    6                    0                     0                        0
       362                   6           8        0   0.4286                    6                    0                     0                        0
       363                   9           5        0   0.6429                    9                    0                     0                        0
       364                   8           5        0   0.6154                    8                    0                     0                        0
       365                   6           8        0   0.4286                    6                    0                     0                        0
       366                   6           8        0   0.4286                    6                    0                     0                        0
       367                  11           3        0   0.7857                   11                    0                     0                        0
       368                   8           6        0   0.5714                    8                    0                     0                        0
       369                   9           5        0   0.6429                    9                    0                     0                        0
       370                   4          10        0   0.2857                    4                    0                     0                        0
       371                  10           4        0   0.7143                   10                    0                     0                        0
       372                   7           7        0   0.5000                    7                    0                     0                        0
       373                   6           8        0   0.4286                    6                    0                     0                        0
       374                  11           3        0   0.7857                   11                    0                     0                        0
       375                   9           5        0   0.6429                    9                    0                     0                        0
       376                   4          10        0   0.2857                    4                    0                     0                        0
       377                   8           6        0   0.5714                    8                    0                     0                        0
       378                   8           6        0   0.5714                    8                    0                     0                        0
       379                   9           5        0   0.6429                    9                    0                     0                        0
       380                   7           7        0   0.5000                    7                    0                     0                        0
       381                   9           5        0   0.6429                    9                    0                     0                        0
       382                  11           3        0   0.7857                   11                    0                     0                        0
       383                  10           4        0   0.7143                   10                    0                     0                        0
       384                   8           6        0   0.5714                    8                    0                     0                        0
       385                  12           2        0   0.8571                   12                    0                     0                        0
       386                   6           8        0   0.4286                    6                    0                     0                        0
       387                   6           8        0   0.4286                    6                    0                     0                        0
       388                   9           5        0   0.6429                    9                    0                     0                        0
       389                  10           4        0   0.7143                   10                    0                     0                        0
       390                   9           5        0   0.6429                    9                    0                     0                        0
       391                   6           7        0   0.4615                    6                    0                     0                        0
       392                   8           6        0   0.5714                    8                    0                     0                        0
       393                   8           6        0   0.5714                    8                    0                     0                        0
       394                   9           5        0   0.6429                    9                    0                     0                        0
       395                  11           3        0   0.7857                   11                    0                     0                        0
       396                   9           5        0   0.6429                    9                    0                     0                        0
       397                   7           7        0   0.5000                    7                    0                     0                        0
       398                   8           6        0   0.5714                    8                    0                     0                        0
       399                  10           4        0   0.7143                   10                    0                     0                        0
       400                   9           5        0   0.6429                    9                    0                     0                        0
       401                   4          10        0   0.2857                    4                    0                     0                        0
       402                   7           7        0   0.5000                    7                    0                     0                        0
       403                   7           7        0   0.5000                    7                    0                     0                        0
       404                   8           6        0   0.5714                    8                    0                     0                        0
       405                   5           9        0   0.3571                    5                    0                     0                        0
       406                   9           5        0   0.6429                    9                    0                     0                        0
       407                   8           6        0   0.5714                    8                    0                     0                        0
       408                   8           6        0   0.5714                    8                    0                     0                        0
       409                   9           5        0   0.6429                    9                    0                     0                        0
       410                   9           5        0   0.6429                    9                    0                     0                        0
       411                   5           9        0   0.3571                    5                    0                     0                        0
       412                   6           8        0   0.4286                    6                    0                     0                        0
       413                   7           7        0   0.5000                    7                    0                     0                        0
       414                   9           5        0   0.6429                    9                    0                     0                        0
       415                  11           3        0   0.7857                   11                    0                     0                        0
       416                   9           5        0   0.6429                    9                    0                     0                        0
       417                   7           7        0   0.5000                    7                    0                     0                        0
       418                  10           4        0   0.7143                   10                    0                     0                        0
       419                   5           9        0   0.3571                    5                    0                     0                        0
       420                   6           8        0   0.4286                    6                    0                     0                        0
       421                   6           8        0   0.4286                    6                    0                     0                        0
       422                  12           2        0   0.8571                   12                    0                     0                        0
       423                   8           6        0   0.5714                    8                    0                     0                        0
       424                   9           5        0   0.6429                    9                    0                     0                        0
       425                   5           9        0   0.3571                    5                    0                     0                        0
       426                   4          10        0   0.2857                    4                    0                     0                        0
       427                  10           4        0   0.7143                   10                    0                     0                        0
       428                   5           9        0   0.3571                    5                    0                     0                        0
       429                   9           5        0   0.6429                    9                    0                     0                        0
       430                  10           4        0   0.7143                   10                    0                     0                        0
       431                   8           6        0   0.5714                    8                    0                     0                        0
       432                   8           6        0   0.5714                    8                    0                     0                        0
       433                   6           8        0   0.4286                    6                    0                     0                        0
       434                   8           6        0   0.5714                    8                    0                     0                        0
       435                   9           5        0   0.6429                    9                    0                     0                        0
       436                  11           3        0   0.7857                   11                    0                     0                        0
       437                   9           5        0   0.6429                    9                    0                     0                        0
       438                   8           6        0   0.5714                    8                    0                     0                        0
       439                   9           5        0   0.6429                    9                    0                     0                        0
       440                   9           5        0   0.6429                    9                    0                     0                        0
       441                  11           3        0   0.7857                   11                    0                     0                        0
       442                   7           7        0   0.5000                    7                    0                     0                        0
       443                   8           6        0   0.5714                    8                    0                     0                        0
       444                   8           5        0   0.6154                    8                    0                     0                        0
       445                  11           3        0   0.7857                   11                    0                     0                        0
       446                   9           5        0   0.6429                    9                    0                     0                        0
       447                   6           8        0   0.4286                    6                    0                     0                        0
       448                   8           6        0   0.5714                    8                    0                     0                        0
       449                   7           7        0   0.5000                    7                    0                     0                        0
       450                  10           4        0   0.7143                   10                    0                     0                        0
       451                  11           3        0   0.7857                   11                    0                     0                        0
       452                   7           7        0   0.5000                    7                    0                     0                        0
       453                  11           3        0   0.7857                   11                    0                     0                        0
       454                  12           2        0   0.8571                   12                    0                     0                        0
       455                   6           8        0   0.4286                    6                    0                     0                        0
       456                   9           5        0   0.6429                    9                    0                     0                        0
       457                   6           8        0   0.4286                    6                    0                     0                        0
       458                   8           6        0   0.5714                    8                    0                     0                        0
       459                   8           6        0   0.5714                    8                    0                     0                        0
       460                  11           3        0   0.7857                   11                    0                     0                        0
       461                  10           4        0   0.7143                   10                    0                     0                        0
       462                   9           5        0   0.6429                    9                    0                     0                        0
       463                   6           8        0   0.4286                    6                    0                     0                        0
       464                   6           8        0   0.4286                    6                    0                     0                        0
       465                   7           7        0   0.5000                    7                    0                     0                        0
       466                   7           7        0   0.5000                    7                    0                     0                        0
       467                   9           5        0   0.6429                    9                    0                     0                        0
       468                  10           4        0   0.7143                   10                    0                     0                        0
       469                   7           7        0   0.5000                    7                    0                     0                        0
       470                   8           6        0   0.5714                    8                    0                     0                        0
       471                   7           7        0   0.5000                    7                    0                     0                        0
       472                   9           5        0   0.6429                    9                    0                     0                        0
       473                   9           5        0   0.6429                    9                    0                     0                        0
       474                   8           6        0   0.5714                    8                    0                     0                        0
       475                   7           7        0   0.5000                    7                    0                     0                        0
       476                   9           5        0   0.6429                    9                    0                     0                        0
       477                   7           7        0   0.5000                    7                    0                     0                        0
       478                   7           7        0   0.5000                    7                    0                     0                        0
       479                  10           4        0   0.7143                   10                    0                     0                        0
       480                   7           7        0   0.5000                    7                    0                     0                        0
       481                  10           4        0   0.7143                   10                    0                     0                        0
       482                   8           6        0   0.5714                    8                    0                     0                        0
       483                   9           5        0   0.6429                    9                    0                     0                        0
       484                   5           9        0   0.3571                    5                    0                     0                        0
       485                   7           7        0   0.5000                    7                    0                     0                        0
       486                   7           7        0   0.5000                    7                    0                     0                        0
       487                   5           9        0   0.3571                    5                    0                     0                        0
       488                   7           7        0   0.5000                    7                    0                     0                        0
       489                  10           4        0   0.7143                   10                    0                     0                        0
       490                   7           7        0   0.5000                    7                    0                     0                        0
       491                  12           2        0   0.8571                   12                    0                     0                        0
       492                   7           7        0   0.5000                    7                    0                     0                        0
       493                   6           8        0   0.4286                    6                    0                     0                        0
       494                   6           8        0   0.4286                    6                    0                     0                        0
       495                   9           5        0   0.6429                    9                    0                     0                        0
       496                   9           5        0   0.6429                    9                    0                     0                        0
       497                   9           5        0   0.6429                    9                    0                     0                        0
       498                   6           8        0   0.4286                    6                    0                     0                        0
       499                  11           3        0   0.7857                   11                    0                     0                        0
```
