# GOLEM Settings Comparison (v5)

**67 graph settings from 31 fitted models:** 29 converged, 2 reached the iteration limit, 0 failed numerically.

## Settings grid

Sensitivity outcomes and no-year runs freeze sparsity=0.02 and threshold=0.10. Size-control uses the continuous grid. `sensitivity_relaxed_tiers` is one continuous fit with temporal and exogenous-year restrictions retained, but predictor-predictor and outcome-outcome edges allowed.

Optimizer: lambda_dag=5.0, learning_rate=0.001, tolerance=1e-06, max_iter=10000.

```
 id                            group representation  constrained  lambda1  threshold       status  iterations  directed  undirected  violations_before  violations_after
  0                             main     continuous         True   0.0100     0.0500    converged        3700        11           0                  0                 0
  1                             main     continuous         True   0.0100     0.1000    converged        3700        11           0                  0                 0
  2                             main     continuous         True   0.0100     0.2000    converged        3700        10           0                  0                 0
  3                             main     continuous         True   0.0200     0.0500    converged        3600        11           0                  0                 0
  4                             main     continuous         True   0.0200     0.1000    converged        3600        11           0                  0                 0
  5                             main     continuous         True   0.0200     0.2000    converged        3600         9           0                  0                 0
  6                             main     continuous         True   0.0500     0.0500    converged        3500        10           0                  0                 0
  7                             main     continuous         True   0.0500     0.1000    converged        3500        10           0                  0                 0
  8                             main     continuous         True   0.0500     0.2000    converged        3500         8           0                  0                 0
  9                             main     continuous        False   0.0100     0.0500    converged        5600         9          10                  5                 1
 10                             main     continuous        False   0.0100     0.1000    converged        5600        13           3                  3                 1
 11                             main     continuous        False   0.0100     0.2000    converged        5600        13           3                  3                 1
 12                             main     continuous        False   0.0200     0.0500    converged        7700         0          19                  5                 0
 13                             main     continuous        False   0.0200     0.1000    converged        7700        13           3                  3                 1
 14                             main     continuous        False   0.0200     0.2000    converged        7700        15           0                  2                 2
 15                             main     continuous        False   0.0500     0.0500 nonconverged       10000        11           6                  6                 1
 16                             main     continuous        False   0.0500     0.1000 nonconverged       10000        12           3                  4                 2
 17                             main     continuous        False   0.0500     0.2000 nonconverged       10000        12           0                  1                 1
 18                             main    discretized         True   0.0100     0.0500    converged        3600        14           0                  0                 0
 19                             main    discretized         True   0.0100     0.1000    converged        3600        14           0                  0                 0
 20                             main    discretized         True   0.0100     0.2000    converged        3600        14           0                  0                 0
 21                             main    discretized         True   0.0200     0.0500    converged        3500        14           0                  0                 0
 22                             main    discretized         True   0.0200     0.1000    converged        3500        14           0                  0                 0
 23                             main    discretized         True   0.0200     0.2000    converged        3500        14           0                  0                 0
 24                             main    discretized         True   0.0500     0.0500    converged        3000        14           0                  0                 0
 25                             main    discretized         True   0.0500     0.1000    converged        3000        14           0                  0                 0
 26                             main    discretized         True   0.0500     0.2000    converged        3000        14           0                  0                 0
 27                             main    discretized        False   0.0100     0.0500    converged        4800         0          21                  3                 0
 28                             main    discretized        False   0.0100     0.1000    converged        4800        21           0                  2                 2
 29                             main    discretized        False   0.0100     0.2000    converged        4800        21           0                  2                 2
 30                             main    discretized        False   0.0200     0.0500    converged        8700         0          21                  3                 0
 31                             main    discretized        False   0.0200     0.1000    converged        8700         0          21                  3                 0
 32                             main    discretized        False   0.0200     0.2000    converged        8700        21           0                  2                 2
 33                             main    discretized        False   0.0500     0.0500    converged        3800         0          21                 10                 0
 34                             main    discretized        False   0.0500     0.1000    converged        3800         0          21                 10                 0
 35                             main    discretized        False   0.0500     0.2000    converged        3800         0          20                 10                 0
 36 sensitivity_outcome:topic_growth     continuous         True   0.0200     0.1000    converged        2100         7           0                  0                 0
 37 sensitivity_outcome:topic_growth     continuous        False   0.0200     0.1000    converged        3100        10           0                  0                 0
 38 sensitivity_outcome:topic_growth    discretized         True   0.0200     0.1000    converged        2900         9           0                  0                 0
 39 sensitivity_outcome:topic_growth    discretized        False   0.0200     0.1000    converged        5200         0          15                  2                 0
 40 sensitivity_outcome:hit_rate_2yr     continuous         True   0.0200     0.1000    converged        2800         9           0                  0                 0
 41 sensitivity_outcome:hit_rate_2yr     continuous        False   0.0200     0.1000    converged        4200        11           1                  2                 1
 42 sensitivity_outcome:hit_rate_2yr    discretized         True   0.0200     0.1000    converged        2900         9           0                  0                 0
 43 sensitivity_outcome:hit_rate_2yr    discretized        False   0.0200     0.1000    converged        8000         0          15                  5                 0
 44              sensitivity_no_year     continuous         True   0.0200     0.1000    converged        2800         3           0                  0                 0
 45              sensitivity_no_year     continuous        False   0.0200     0.1000    converged        4500         4           6                  4                 0
 46              sensitivity_no_year    discretized         True   0.0200     0.1000    converged        3500         8           0                  0                 0
 47              sensitivity_no_year    discretized        False   0.0200     0.1000    converged        7100         0          15                  4                 0
 48         sensitivity_size_control     continuous         True   0.0100     0.0500    converged        4700        15           0                  0                 0
 49         sensitivity_size_control     continuous         True   0.0100     0.1000    converged        4700        14           0                  0                 0
 50         sensitivity_size_control     continuous         True   0.0100     0.2000    converged        4700        12           0                  0                 0
 51         sensitivity_size_control     continuous         True   0.0200     0.0500    converged        5000        15           0                  0                 0
 52         sensitivity_size_control     continuous         True   0.0200     0.1000    converged        5000        14           0                  0                 0
 53         sensitivity_size_control     continuous         True   0.0200     0.2000    converged        5000        12           0                  0                 0
 54         sensitivity_size_control     continuous         True   0.0500     0.0500    converged        5300        14           0                  0                 0
 55         sensitivity_size_control     continuous         True   0.0500     0.1000    converged        5300        12           0                  0                 0
 56         sensitivity_size_control     continuous         True   0.0500     0.2000    converged        5300        11           0                  0                 0
 57         sensitivity_size_control     continuous        False   0.0100     0.0500    converged        4400         0          27                  8                 0
 58         sensitivity_size_control     continuous        False   0.0100     0.1000    converged        4400         6          20                  5                 0
 59         sensitivity_size_control     continuous        False   0.0100     0.2000    converged        4400        12           8                  2                 0
 60         sensitivity_size_control     continuous        False   0.0200     0.0500    converged        9300         0          25                  7                 0
 61         sensitivity_size_control     continuous        False   0.0200     0.1000    converged        9300         0          25                  6                 0
 62         sensitivity_size_control     continuous        False   0.0200     0.2000    converged        9300        12           9                  3                 0
 63         sensitivity_size_control     continuous        False   0.0500     0.0500 nonconverged       10000         0          23                  5                 0
 64         sensitivity_size_control     continuous        False   0.0500     0.1000 nonconverged       10000         0          23                  5                 0
 65         sensitivity_size_control     continuous        False   0.0500     0.2000 nonconverged       10000        11           8                  2                 0
 66        sensitivity_relaxed_tiers     continuous         True   0.0200     0.1000    converged        7300        16           0                  0                 0
```

## Edge detail per setting

### Setting 0: main / continuous / lambda1=0.01 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8062           0.0000
     topic_share_t1   ->     log1p_median_c2           0.4336           0.0000
connectivity_t1_log   ->       topic_share_t           0.1440           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8025           0.0000
      modularity_t1   ->     log1p_median_c2           0.3474           0.0000 possible size confound
               year   ->      topic_share_t1           0.4597           0.0000
               year   -> cross_topic_rate_t1           0.4361           0.0000
               year   -> connectivity_t1_log           0.6706           0.0000
               year   ->       modularity_t1           0.2367           0.0000 possible size confound
               year   ->       topic_share_t           0.2312           0.0000
               year   ->     log1p_median_c2           1.3102           0.0000
```

### Setting 1: main / continuous / lambda1=0.01 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8062           0.0000
     topic_share_t1   ->     log1p_median_c2           0.4336           0.0000
connectivity_t1_log   ->       topic_share_t           0.1440           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8025           0.0000
      modularity_t1   ->     log1p_median_c2           0.3474           0.0000 possible size confound
               year   ->      topic_share_t1           0.4597           0.0000
               year   -> cross_topic_rate_t1           0.4361           0.0000
               year   -> connectivity_t1_log           0.6706           0.0000
               year   ->       modularity_t1           0.2367           0.0000 possible size confound
               year   ->       topic_share_t           0.2312           0.0000
               year   ->     log1p_median_c2           1.3102           0.0000
```

### Setting 2: main / continuous / lambda1=0.01 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8062           0.0000
     topic_share_t1   ->     log1p_median_c2           0.4336           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8025           0.0000
      modularity_t1   ->     log1p_median_c2           0.3474           0.0000 possible size confound
               year   ->      topic_share_t1           0.4597           0.0000
               year   -> cross_topic_rate_t1           0.4361           0.0000
               year   -> connectivity_t1_log           0.6706           0.0000
               year   ->       modularity_t1           0.2367           0.0000 possible size confound
               year   ->       topic_share_t           0.2312           0.0000
               year   ->     log1p_median_c2           1.3102           0.0000
```

### Setting 3: main / continuous / lambda1=0.02 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3600.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8045           0.0000
     topic_share_t1   ->     log1p_median_c2           0.3843           0.0000
connectivity_t1_log   ->       topic_share_t           0.1138           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.7259           0.0000
      modularity_t1   ->     log1p_median_c2           0.2864           0.0000 possible size confound
               year   ->      topic_share_t1           0.4528           0.0000
               year   -> cross_topic_rate_t1           0.4293           0.0000
               year   -> connectivity_t1_log           0.6637           0.0000
               year   ->       modularity_t1           0.2299           0.0000 possible size confound
               year   ->       topic_share_t           0.1972           0.0000
               year   ->     log1p_median_c2           1.2102           0.0000
```

### Setting 4: main / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3600.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8045           0.0000
     topic_share_t1   ->     log1p_median_c2           0.3843           0.0000
connectivity_t1_log   ->       topic_share_t           0.1138           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.7259           0.0000
      modularity_t1   ->     log1p_median_c2           0.2864           0.0000 possible size confound
               year   ->      topic_share_t1           0.4528           0.0000
               year   -> cross_topic_rate_t1           0.4293           0.0000
               year   -> connectivity_t1_log           0.6637           0.0000
               year   ->       modularity_t1           0.2299           0.0000 possible size confound
               year   ->       topic_share_t           0.1972           0.0000
               year   ->     log1p_median_c2           1.2102           0.0000
```

### Setting 5: main / continuous / lambda1=0.02 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3600.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8045           0.0000
     topic_share_t1   ->     log1p_median_c2           0.3843           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.7259           0.0000
      modularity_t1   ->     log1p_median_c2           0.2864           0.0000 possible size confound
               year   ->      topic_share_t1           0.4528           0.0000
               year   -> cross_topic_rate_t1           0.4293           0.0000
               year   -> connectivity_t1_log           0.6637           0.0000
               year   ->       modularity_t1           0.2299           0.0000 possible size confound
               year   ->     log1p_median_c2           1.2102           0.0000
```

### Setting 6: main / continuous / lambda1=0.05 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7963           0.0000
     topic_share_t1   ->     log1p_median_c2           0.2342           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.4924           0.0000
      modularity_t1   ->     log1p_median_c2           0.1007           0.0000 possible size confound
               year   ->      topic_share_t1           0.4320           0.0000
               year   -> cross_topic_rate_t1           0.4085           0.0000
               year   -> connectivity_t1_log           0.6429           0.0000
               year   ->       modularity_t1           0.2090           0.0000 possible size confound
               year   ->       topic_share_t           0.1365           0.0000
               year   ->     log1p_median_c2           0.9056           0.0000
```

### Setting 7: main / continuous / lambda1=0.05 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7963           0.0000
     topic_share_t1   ->     log1p_median_c2           0.2342           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.4924           0.0000
      modularity_t1   ->     log1p_median_c2           0.1007           0.0000 possible size confound
               year   ->      topic_share_t1           0.4320           0.0000
               year   -> cross_topic_rate_t1           0.4085           0.0000
               year   -> connectivity_t1_log           0.6429           0.0000
               year   ->       modularity_t1           0.2090           0.0000 possible size confound
               year   ->       topic_share_t           0.1365           0.0000
               year   ->     log1p_median_c2           0.9056           0.0000
```

### Setting 8: main / continuous / lambda1=0.05 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7963           0.0000
     topic_share_t1   ->     log1p_median_c2           0.2342           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.4924           0.0000
               year   ->      topic_share_t1           0.4320           0.0000
               year   -> cross_topic_rate_t1           0.4085           0.0000
               year   -> connectivity_t1_log           0.6429           0.0000
               year   ->       modularity_t1           0.2090           0.0000 possible size confound
               year   ->     log1p_median_c2           0.9056           0.0000
```

### Setting 9: main / continuous / lambda1=0.01 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5600.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->     log1p_median_c2           0.8122           0.0334
connectivity_t1_log   -> cross_topic_rate_t1           0.5262           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.7945           0.0002
      modularity_t1   -> cross_topic_rate_t1           0.0999           0.0004 possible size confound
      modularity_t1   ->     log1p_median_c2           0.3876           0.0492 possible size confound
               year   -> cross_topic_rate_t1           0.8065           0.0188
               year   ->     log1p_median_c2           1.2733           0.0087
      topic_share_t   -> cross_topic_rate_t1           0.0709           0.0296
      topic_share_t   ->     log1p_median_c2           0.4166           0.0003
connectivity_t1_log   --       modularity_t1           0.7938           0.0006 possible size confound
connectivity_t1_log   --       topic_share_t           0.0001           0.5779
connectivity_t1_log   --      topic_share_t1           0.0690           0.4560
connectivity_t1_log   --                year           0.0493           0.7423
      modularity_t1   --       topic_share_t           0.0526           0.0088 possible size confound
      modularity_t1   --      topic_share_t1           0.0730           0.5156 possible size confound
      modularity_t1   --                year           0.0100           0.9946 possible size confound
      topic_share_t   --      topic_share_t1           0.8039           0.0515
      topic_share_t   --                year           0.0872           0.2874
     topic_share_t1   --                year           0.2090           0.0585
```

### Setting 10: main / continuous / lambda1=0.01 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5600.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4560           0.0690
     topic_share_t1   ->       modularity_t1           0.5156           0.0730 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.8122           0.0334
connectivity_t1_log   -> cross_topic_rate_t1           0.5262           0.0000
connectivity_t1_log   ->       modularity_t1           0.7938           0.0006 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7945           0.0002
      modularity_t1   ->     log1p_median_c2           0.3876           0.0492 possible size confound
               year   -> cross_topic_rate_t1           0.8065           0.0188
               year   -> connectivity_t1_log           0.7423           0.0493
               year   ->       modularity_t1           0.9946           0.0100 possible size confound
               year   ->     log1p_median_c2           1.2733           0.0087
      topic_share_t   -> connectivity_t1_log           0.5779           0.0001
      topic_share_t   ->     log1p_median_c2           0.4166           0.0003
      topic_share_t   --      topic_share_t1           0.8039           0.0515
      topic_share_t   --                year           0.0872           0.2874
     topic_share_t1   --                year           0.2090           0.0585
```

### Setting 11: main / continuous / lambda1=0.01 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5600.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4560           0.0690
     topic_share_t1   ->       modularity_t1           0.5156           0.0730 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.8122           0.0334
connectivity_t1_log   -> cross_topic_rate_t1           0.5262           0.0000
connectivity_t1_log   ->       modularity_t1           0.7938           0.0006 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7945           0.0002
      modularity_t1   ->     log1p_median_c2           0.3876           0.0492 possible size confound
               year   -> cross_topic_rate_t1           0.8065           0.0188
               year   -> connectivity_t1_log           0.7423           0.0493
               year   ->       modularity_t1           0.9946           0.0100 possible size confound
               year   ->     log1p_median_c2           1.2733           0.0087
      topic_share_t   -> connectivity_t1_log           0.5779           0.0001
      topic_share_t   ->     log1p_median_c2           0.4166           0.0003
      topic_share_t   --      topic_share_t1           0.8039           0.0515
      topic_share_t   --                year           0.0872           0.2874
     topic_share_t1   --                year           0.2090           0.0585
```

### Setting 12: main / continuous / lambda1=0.02 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 7700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.4102           0.0039
connectivity_t1_log   --     log1p_median_c2           0.7305           0.0001
connectivity_t1_log   --       modularity_t1           0.8026           0.0002 possible size confound
connectivity_t1_log   --       topic_share_t           0.0004           0.5412
connectivity_t1_log   --      topic_share_t1           0.0653           0.4237
connectivity_t1_log   --                year           0.0495           0.7353
cross_topic_rate_t1   --     log1p_median_c2           0.0002           0.0650
cross_topic_rate_t1   --      topic_share_t1           0.0691           0.0002
cross_topic_rate_t1   --                year           0.0283           0.6467
    log1p_median_c2   --       modularity_t1           0.0340           0.3274 possible size confound
    log1p_median_c2   --       topic_share_t           0.0005           0.3863
    log1p_median_c2   --      topic_share_t1           0.0329           0.7435
    log1p_median_c2   --                year           0.0099           1.1919
      modularity_t1   --       topic_share_t           0.0509           0.0001 possible size confound
      modularity_t1   --      topic_share_t1           0.0651           0.5201 possible size confound
      modularity_t1   --                year           0.0092           1.0180 possible size confound
      topic_share_t   --      topic_share_t1           0.7890           0.0530
      topic_share_t   --                year           0.0830           0.2956
     topic_share_t1   --                year           0.1980           0.0510
```

### Setting 13: main / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 7700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4237           0.0653
     topic_share_t1   ->       modularity_t1           0.5201           0.0651 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.7435           0.0329
connectivity_t1_log   -> cross_topic_rate_t1           0.4102           0.0039
connectivity_t1_log   ->       modularity_t1           0.8026           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7305           0.0001
      modularity_t1   ->     log1p_median_c2           0.3274           0.0340 possible size confound
               year   -> cross_topic_rate_t1           0.6467           0.0283
               year   -> connectivity_t1_log           0.7353           0.0495
               year   ->       modularity_t1           1.0180           0.0092 possible size confound
               year   ->     log1p_median_c2           1.1919           0.0099
      topic_share_t   -> connectivity_t1_log           0.5412           0.0004
      topic_share_t   ->     log1p_median_c2           0.3863           0.0005
      topic_share_t   --      topic_share_t1           0.7890           0.0530
      topic_share_t   --                year           0.0830           0.2956
     topic_share_t1   --                year           0.1980           0.0510
```

### Setting 14: main / continuous / lambda1=0.02 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 7700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4237           0.0653
     topic_share_t1   ->       modularity_t1           0.5201           0.0651 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.7435           0.0329
connectivity_t1_log   -> cross_topic_rate_t1           0.4102           0.0039
connectivity_t1_log   ->       modularity_t1           0.8026           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7305           0.0001
      modularity_t1   ->     log1p_median_c2           0.3274           0.0340 possible size confound
               year   -> cross_topic_rate_t1           0.6467           0.0283
               year   -> connectivity_t1_log           0.7353           0.0495
               year   ->       modularity_t1           1.0180           0.0092 possible size confound
               year   ->       topic_share_t           0.2956           0.0830
               year   ->     log1p_median_c2           1.1919           0.0099
      topic_share_t   ->      topic_share_t1           0.7890           0.0530
      topic_share_t   -> connectivity_t1_log           0.5412           0.0004
      topic_share_t   ->     log1p_median_c2           0.3863           0.0005
```

### Setting 15: main / continuous / lambda1=0.05 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5336           0.0204 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.4324           0.0195
cross_topic_rate_t1   ->     log1p_median_c2           0.0576           0.0092
connectivity_t1_log   -> cross_topic_rate_t1           0.3700           0.0007
connectivity_t1_log   ->       modularity_t1           0.8114           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.3633           0.0136
               year   -> cross_topic_rate_t1           0.6376           0.0254
               year   ->       modularity_t1           1.0860           0.0063 possible size confound
               year   ->     log1p_median_c2           0.7155           0.0292
      topic_share_t   ->     log1p_median_c2           0.2884           0.0012
    log1p_median_c2   ->       modularity_t1           0.1428           0.0001 possible size confound
connectivity_t1_log   --       topic_share_t           0.0013           0.1911
connectivity_t1_log   --      topic_share_t1           0.0002           0.0630
connectivity_t1_log   --                year           0.0522           0.6991
      topic_share_t   --      topic_share_t1           0.7670           0.0580
      topic_share_t   --                year           0.0710           0.2878
     topic_share_t1   --                year           0.1963           0.0263
```

### Setting 16: main / continuous / lambda1=0.05 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5336           0.0204 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.4324           0.0195
connectivity_t1_log   -> cross_topic_rate_t1           0.3700           0.0007
connectivity_t1_log   ->       modularity_t1           0.8114           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.3633           0.0136
               year   -> cross_topic_rate_t1           0.6376           0.0254
               year   -> connectivity_t1_log           0.6991           0.0522
               year   ->       modularity_t1           1.0860           0.0063 possible size confound
               year   ->     log1p_median_c2           0.7155           0.0292
      topic_share_t   -> connectivity_t1_log           0.1911           0.0013
      topic_share_t   ->     log1p_median_c2           0.2884           0.0012
    log1p_median_c2   ->       modularity_t1           0.1428           0.0001 possible size confound
      topic_share_t   --      topic_share_t1           0.7670           0.0580
      topic_share_t   --                year           0.0710           0.2878
     topic_share_t1   --                year           0.1963           0.0263
```

### Setting 17: main / continuous / lambda1=0.05 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5336           0.0204 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.4324           0.0195
connectivity_t1_log   -> cross_topic_rate_t1           0.3700           0.0007
connectivity_t1_log   ->       modularity_t1           0.8114           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.3633           0.0136
               year   -> cross_topic_rate_t1           0.6376           0.0254
               year   -> connectivity_t1_log           0.6991           0.0522
               year   ->       modularity_t1           1.0860           0.0063 possible size confound
               year   ->       topic_share_t           0.2878           0.0710
               year   ->     log1p_median_c2           0.7155           0.0292
      topic_share_t   ->      topic_share_t1           0.7670           0.0580
      topic_share_t   ->     log1p_median_c2           0.2884           0.0012
```

### Setting 18: main / discretized / lambda1=0.01 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3600.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.1651           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3124           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4815           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7343           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.5294           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9518           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.3664           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7166           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1477           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.1124           0.0000
               year_bin   ->     connectivity_t1_bin           1.7546           0.0000
               year_bin   ->       modularity_t1_bin           0.8367           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.6126           0.0000
               year_bin   ->     log1p_median_c2_bin           1.5200           0.0000
```

### Setting 19: main / discretized / lambda1=0.01 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3600.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.1651           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3124           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4815           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7343           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.5294           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9518           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.3664           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7166           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1477           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.1124           0.0000
               year_bin   ->     connectivity_t1_bin           1.7546           0.0000
               year_bin   ->       modularity_t1_bin           0.8367           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.6126           0.0000
               year_bin   ->     log1p_median_c2_bin           1.5200           0.0000
```

### Setting 20: main / discretized / lambda1=0.01 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3600.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.1651           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3124           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4815           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7343           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.5294           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9518           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.3664           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7166           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1477           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.1124           0.0000
               year_bin   ->     connectivity_t1_bin           1.7546           0.0000
               year_bin   ->       modularity_t1_bin           0.8367           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.6126           0.0000
               year_bin   ->     log1p_median_c2_bin           1.5200           0.0000
```

### Setting 21: main / discretized / lambda1=0.02 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.1209           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3019           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4568           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7235           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.4981           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9279           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.3461           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7069           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1255           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0913           0.0000
               year_bin   ->     connectivity_t1_bin           1.7159           0.0000
               year_bin   ->       modularity_t1_bin           0.8240           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.5752           0.0000
               year_bin   ->     log1p_median_c2_bin           1.4805           0.0000
```

### Setting 22: main / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.1209           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3019           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4568           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7235           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.4981           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9279           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.3461           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7069           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1255           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0913           0.0000
               year_bin   ->     connectivity_t1_bin           1.7159           0.0000
               year_bin   ->       modularity_t1_bin           0.8240           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.5752           0.0000
               year_bin   ->     log1p_median_c2_bin           1.4805           0.0000
```

### Setting 23: main / discretized / lambda1=0.02 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.1209           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3019           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4568           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7235           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.4981           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9279           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.3461           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7069           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1255           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0913           0.0000
               year_bin   ->     connectivity_t1_bin           1.7159           0.0000
               year_bin   ->       modularity_t1_bin           0.8240           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.5752           0.0000
               year_bin   ->     log1p_median_c2_bin           1.4805           0.0000
```

### Setting 24: main / discretized / lambda1=0.05 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3000.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0768           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.2687           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4064           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.6935           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.4095           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.8722           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.2843           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.6760           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.0836           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0488           0.0000
               year_bin   ->     connectivity_t1_bin           1.6597           0.0000
               year_bin   ->       modularity_t1_bin           0.7869           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.4731           0.0000
               year_bin   ->     log1p_median_c2_bin           1.3949           0.0000
```

### Setting 25: main / discretized / lambda1=0.05 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3000.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0768           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.2687           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4064           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.6935           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.4095           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.8722           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.2843           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.6760           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.0836           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0488           0.0000
               year_bin   ->     connectivity_t1_bin           1.6597           0.0000
               year_bin   ->       modularity_t1_bin           0.7869           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.4731           0.0000
               year_bin   ->     log1p_median_c2_bin           1.3949           0.0000
```

### Setting 26: main / discretized / lambda1=0.05 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3000.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0768           0.0000
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.2687           0.0000
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4064           0.0000
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.6935           0.0000
    connectivity_t1_bin   ->       topic_share_t_bin           0.4095           0.0000
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.8722           0.0000
      modularity_t1_bin   ->       topic_share_t_bin           0.2843           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.6760           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.0836           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0488           0.0000
               year_bin   ->     connectivity_t1_bin           1.6597           0.0000
               year_bin   ->       modularity_t1_bin           0.7869           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.4731           0.0000
               year_bin   ->     log1p_median_c2_bin           1.3949           0.0000
```

### Setting 27: main / discretized / lambda1=0.01 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4800.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0063           3.8476
    connectivity_t1_bin   --     log1p_median_c2_bin           3.0745           0.0081
    connectivity_t1_bin   --       modularity_t1_bin           1.1188           0.0130 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0066           8.9015
    connectivity_t1_bin   --       topic_share_t_bin           7.9301           0.0076
    connectivity_t1_bin   --                year_bin           0.0070           2.6985
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.7603           0.0131
cross_topic_rate_t1_bin   --       modularity_t1_bin           0.4328           0.0313 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           7.1771           0.0133
cross_topic_rate_t1_bin   --       topic_share_t_bin           1.5965           0.0073
cross_topic_rate_t1_bin   --                year_bin           0.0148           8.3522
    log1p_median_c2_bin   --       modularity_t1_bin           5.6032           0.0139 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0082           1.5550
    log1p_median_c2_bin   --       topic_share_t_bin           0.0098           6.3465
    log1p_median_c2_bin   --                year_bin           0.0210           1.5714
      modularity_t1_bin   --      topic_share_t1_bin           0.0166           1.2336 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.0113           2.2138 possible size confound
      modularity_t1_bin   --                year_bin           0.0566           1.4224 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           4.1714           0.0057
     topic_share_t1_bin   --                year_bin           0.0073           3.6022
      topic_share_t_bin   --                year_bin           0.0099           0.7680
```

### Setting 28: main / discretized / lambda1=0.01 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4800.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->     connectivity_t1_bin           8.9015           0.0066
     topic_share_t1_bin   ->       modularity_t1_bin           1.2336           0.0166 possible size confound
     topic_share_t1_bin   ->       topic_share_t_bin           4.1714           0.0057
     topic_share_t1_bin   ->     log1p_median_c2_bin           1.5550           0.0082
cross_topic_rate_t1_bin   ->      topic_share_t1_bin           7.1771           0.0133
cross_topic_rate_t1_bin   ->     connectivity_t1_bin           3.8476           0.0063
cross_topic_rate_t1_bin   ->       modularity_t1_bin           0.4328           0.0313 possible size confound
cross_topic_rate_t1_bin   ->       topic_share_t_bin           1.5965           0.0073
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7603           0.0131
    connectivity_t1_bin   ->       modularity_t1_bin           1.1188           0.0130 possible size confound
    connectivity_t1_bin   ->       topic_share_t_bin           7.9301           0.0076
    connectivity_t1_bin   ->     log1p_median_c2_bin           3.0745           0.0081
               year_bin   ->      topic_share_t1_bin           3.6022           0.0073
               year_bin   -> cross_topic_rate_t1_bin           8.3522           0.0148
               year_bin   ->     connectivity_t1_bin           2.6985           0.0070
               year_bin   ->       modularity_t1_bin           1.4224           0.0566 possible size confound
               year_bin   ->       topic_share_t_bin           0.7680           0.0099
               year_bin   ->     log1p_median_c2_bin           1.5714           0.0210
      topic_share_t_bin   ->       modularity_t1_bin           2.2138           0.0113 possible size confound
      topic_share_t_bin   ->     log1p_median_c2_bin           6.3465           0.0098
    log1p_median_c2_bin   ->       modularity_t1_bin           5.6032           0.0139 possible size confound
```

### Setting 29: main / discretized / lambda1=0.01 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4800.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->     connectivity_t1_bin           8.9015           0.0066
     topic_share_t1_bin   ->       modularity_t1_bin           1.2336           0.0166 possible size confound
     topic_share_t1_bin   ->       topic_share_t_bin           4.1714           0.0057
     topic_share_t1_bin   ->     log1p_median_c2_bin           1.5550           0.0082
cross_topic_rate_t1_bin   ->      topic_share_t1_bin           7.1771           0.0133
cross_topic_rate_t1_bin   ->     connectivity_t1_bin           3.8476           0.0063
cross_topic_rate_t1_bin   ->       modularity_t1_bin           0.4328           0.0313 possible size confound
cross_topic_rate_t1_bin   ->       topic_share_t_bin           1.5965           0.0073
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7603           0.0131
    connectivity_t1_bin   ->       modularity_t1_bin           1.1188           0.0130 possible size confound
    connectivity_t1_bin   ->       topic_share_t_bin           7.9301           0.0076
    connectivity_t1_bin   ->     log1p_median_c2_bin           3.0745           0.0081
               year_bin   ->      topic_share_t1_bin           3.6022           0.0073
               year_bin   -> cross_topic_rate_t1_bin           8.3522           0.0148
               year_bin   ->     connectivity_t1_bin           2.6985           0.0070
               year_bin   ->       modularity_t1_bin           1.4224           0.0566 possible size confound
               year_bin   ->       topic_share_t_bin           0.7680           0.0099
               year_bin   ->     log1p_median_c2_bin           1.5714           0.0210
      topic_share_t_bin   ->       modularity_t1_bin           2.2138           0.0113 possible size confound
      topic_share_t_bin   ->     log1p_median_c2_bin           6.3465           0.0098
    log1p_median_c2_bin   ->       modularity_t1_bin           5.6032           0.0139 possible size confound
```

### Setting 30: main / discretized / lambda1=0.02 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8700.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0076           3.1157
    connectivity_t1_bin   --     log1p_median_c2_bin           2.5579           0.0095
    connectivity_t1_bin   --       modularity_t1_bin           0.7533           0.0185 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0068           8.4057
    connectivity_t1_bin   --       topic_share_t_bin           7.2027           0.0081
    connectivity_t1_bin   --                year_bin           0.0094           2.3684
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.7023           0.0177
cross_topic_rate_t1_bin   --       modularity_t1_bin           0.3949           0.0535 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           6.3559           0.0164
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.9976           0.0096
cross_topic_rate_t1_bin   --                year_bin           0.0181           7.4297
    log1p_median_c2_bin   --       modularity_t1_bin           3.4492           0.0445 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0098           1.1238
    log1p_median_c2_bin   --       topic_share_t_bin           0.0103           5.9736
    log1p_median_c2_bin   --                year_bin           0.0311           1.5008
      modularity_t1_bin   --      topic_share_t1_bin           0.0259           1.1683 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.0148           1.4023 possible size confound
      modularity_t1_bin   --                year_bin           0.1043           1.3416 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           3.6399           0.0070
     topic_share_t1_bin   --                year_bin           0.0103           2.7881
      topic_share_t_bin   --                year_bin           0.0145           0.6732
```

### Setting 31: main / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8700.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0076           3.1157
    connectivity_t1_bin   --     log1p_median_c2_bin           2.5579           0.0095
    connectivity_t1_bin   --       modularity_t1_bin           0.7533           0.0185 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0068           8.4057
    connectivity_t1_bin   --       topic_share_t_bin           7.2027           0.0081
    connectivity_t1_bin   --                year_bin           0.0094           2.3684
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.7023           0.0177
cross_topic_rate_t1_bin   --       modularity_t1_bin           0.3949           0.0535 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           6.3559           0.0164
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.9976           0.0096
cross_topic_rate_t1_bin   --                year_bin           0.0181           7.4297
    log1p_median_c2_bin   --       modularity_t1_bin           3.4492           0.0445 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0098           1.1238
    log1p_median_c2_bin   --       topic_share_t_bin           0.0103           5.9736
    log1p_median_c2_bin   --                year_bin           0.0311           1.5008
      modularity_t1_bin   --      topic_share_t1_bin           0.0259           1.1683 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.0148           1.4023 possible size confound
      modularity_t1_bin   --                year_bin           0.1043           1.3416 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           3.6399           0.0070
     topic_share_t1_bin   --                year_bin           0.0103           2.7881
      topic_share_t_bin   --                year_bin           0.0145           0.6732
```

### Setting 32: main / discretized / lambda1=0.02 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8700.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->     connectivity_t1_bin           8.4057           0.0068
     topic_share_t1_bin   ->       modularity_t1_bin           1.1683           0.0259 possible size confound
     topic_share_t1_bin   ->       topic_share_t_bin           3.6399           0.0070
     topic_share_t1_bin   ->     log1p_median_c2_bin           1.1238           0.0098
cross_topic_rate_t1_bin   ->      topic_share_t1_bin           6.3559           0.0164
cross_topic_rate_t1_bin   ->     connectivity_t1_bin           3.1157           0.0076
cross_topic_rate_t1_bin   ->       modularity_t1_bin           0.3949           0.0535 possible size confound
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.9976           0.0096
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7023           0.0177
    connectivity_t1_bin   ->       modularity_t1_bin           0.7533           0.0185 possible size confound
    connectivity_t1_bin   ->       topic_share_t_bin           7.2027           0.0081
    connectivity_t1_bin   ->     log1p_median_c2_bin           2.5579           0.0095
               year_bin   ->      topic_share_t1_bin           2.7881           0.0103
               year_bin   -> cross_topic_rate_t1_bin           7.4297           0.0181
               year_bin   ->     connectivity_t1_bin           2.3684           0.0094
               year_bin   ->       modularity_t1_bin           1.3416           0.1043 possible size confound
               year_bin   ->       topic_share_t_bin           0.6732           0.0145
               year_bin   ->     log1p_median_c2_bin           1.5008           0.0311
      topic_share_t_bin   ->       modularity_t1_bin           1.4023           0.0148 possible size confound
      topic_share_t_bin   ->     log1p_median_c2_bin           5.9736           0.0103
    log1p_median_c2_bin   ->       modularity_t1_bin           3.4492           0.0445 possible size confound
```

### Setting 33: main / discretized / lambda1=0.05 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 3800.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0110           6.4224
    connectivity_t1_bin   --     log1p_median_c2_bin           0.0162           1.0340
    connectivity_t1_bin   --       modularity_t1_bin           3.7377           0.0165 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0404           0.1768
    connectivity_t1_bin   --       topic_share_t_bin           0.0806           0.5153
    connectivity_t1_bin   --                year_bin           0.0102           2.8178
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0118           2.1208
cross_topic_rate_t1_bin   --       modularity_t1_bin           1.4496           0.0175 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0236           0.7907
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0409           0.3820
cross_topic_rate_t1_bin   --                year_bin           0.0112           6.6014
    log1p_median_c2_bin   --       modularity_t1_bin           0.8912           0.0488 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0156           4.3944
    log1p_median_c2_bin   --       topic_share_t_bin           0.0190           1.7498
    log1p_median_c2_bin   --                year_bin           5.5200           0.0302
      modularity_t1_bin   --      topic_share_t1_bin           0.1393           0.7793 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.3005           0.4988 possible size confound
      modularity_t1_bin   --                year_bin           0.0249           1.0733 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           0.0457           5.7845
     topic_share_t1_bin   --                year_bin           1.6045           0.0156
      topic_share_t_bin   --                year_bin           0.5079           0.0242
```

### Setting 34: main / discretized / lambda1=0.05 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 3800.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0110           6.4224
    connectivity_t1_bin   --     log1p_median_c2_bin           0.0162           1.0340
    connectivity_t1_bin   --       modularity_t1_bin           3.7377           0.0165 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0404           0.1768
    connectivity_t1_bin   --       topic_share_t_bin           0.0806           0.5153
    connectivity_t1_bin   --                year_bin           0.0102           2.8178
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0118           2.1208
cross_topic_rate_t1_bin   --       modularity_t1_bin           1.4496           0.0175 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0236           0.7907
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0409           0.3820
cross_topic_rate_t1_bin   --                year_bin           0.0112           6.6014
    log1p_median_c2_bin   --       modularity_t1_bin           0.8912           0.0488 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0156           4.3944
    log1p_median_c2_bin   --       topic_share_t_bin           0.0190           1.7498
    log1p_median_c2_bin   --                year_bin           5.5200           0.0302
      modularity_t1_bin   --      topic_share_t1_bin           0.1393           0.7793 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.3005           0.4988 possible size confound
      modularity_t1_bin   --                year_bin           0.0249           1.0733 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           0.0457           5.7845
     topic_share_t1_bin   --                year_bin           1.6045           0.0156
      topic_share_t_bin   --                year_bin           0.5079           0.0242
```

### Setting 35: main / discretized / lambda1=0.05 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 3800.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0110           6.4224
    connectivity_t1_bin   --     log1p_median_c2_bin           0.0162           1.0340
    connectivity_t1_bin   --       modularity_t1_bin           3.7377           0.0165 possible size confound
    connectivity_t1_bin   --       topic_share_t_bin           0.0806           0.5153
    connectivity_t1_bin   --                year_bin           0.0102           2.8178
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0118           2.1208
cross_topic_rate_t1_bin   --       modularity_t1_bin           1.4496           0.0175 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0236           0.7907
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0409           0.3820
cross_topic_rate_t1_bin   --                year_bin           0.0112           6.6014
    log1p_median_c2_bin   --       modularity_t1_bin           0.8912           0.0488 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0156           4.3944
    log1p_median_c2_bin   --       topic_share_t_bin           0.0190           1.7498
    log1p_median_c2_bin   --                year_bin           5.5200           0.0302
      modularity_t1_bin   --      topic_share_t1_bin           0.1393           0.7793 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.3005           0.4988 possible size confound
      modularity_t1_bin   --                year_bin           0.0249           1.0733 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           0.0457           5.7845
     topic_share_t1_bin   --                year_bin           1.6045           0.0156
      topic_share_t_bin   --                year_bin           0.5079           0.0242
```

### Setting 36: sensitivity_outcome:topic_growth / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 2100.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->        topic_growth           0.1919           0.0000
connectivity_t1_log   ->        topic_growth           0.2482           0.0000
               year   ->      topic_share_t1           0.4500           0.0000
               year   -> cross_topic_rate_t1           0.4264           0.0000
               year   -> connectivity_t1_log           0.6608           0.0000
               year   ->       modularity_t1           0.2270           0.0000 possible size confound
               year   ->        topic_growth           0.4198           0.0000
```

### Setting 37: sensitivity_outcome:topic_growth / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 3100.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5272           0.0085 possible size confound
     topic_share_t1   ->        topic_growth           0.1784           0.0207
connectivity_t1_log   -> cross_topic_rate_t1           0.4507           0.0190
connectivity_t1_log   ->       modularity_t1           0.8130           0.0182 possible size confound
connectivity_t1_log   ->        topic_growth           0.2482           0.0037
               year   ->      topic_share_t1           0.4252           0.0623
               year   -> cross_topic_rate_t1           0.7232           0.0176
               year   -> connectivity_t1_log           0.6164           0.0494
               year   ->       modularity_t1           1.0460           0.0027 possible size confound
               year   ->        topic_growth           0.3954           0.0159
```

### Setting 38: sensitivity_outcome:topic_growth / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 2900.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->        topic_growth_bin           0.8318           0.0000
cross_topic_rate_t1_bin   ->        topic_growth_bin           0.4898           0.0000
    connectivity_t1_bin   ->        topic_growth_bin           0.5008           0.0000
      modularity_t1_bin   ->        topic_growth_bin           0.5210           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1263           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0913           0.0000
               year_bin   ->     connectivity_t1_bin           1.7255           0.0000
               year_bin   ->       modularity_t1_bin           0.8218           0.0000 possible size confound
               year_bin   ->        topic_growth_bin           0.9426           0.0000
```

### Setting 39: sensitivity_outcome:topic_growth / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5200.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           5.9267           0.0229
    connectivity_t1_bin   --       modularity_t1_bin           0.0222           6.2166 possible size confound
    connectivity_t1_bin   --        topic_growth_bin           0.6742           0.0670
    connectivity_t1_bin   --      topic_share_t1_bin           2.6091           0.0203
    connectivity_t1_bin   --                year_bin           0.0198           3.1937
cross_topic_rate_t1_bin   --       modularity_t1_bin           0.0244           2.6121 possible size confound
cross_topic_rate_t1_bin   --        topic_growth_bin           1.2800           0.0434
cross_topic_rate_t1_bin   --      topic_share_t1_bin           6.2387           0.0197
cross_topic_rate_t1_bin   --                year_bin           0.0290           1.8056
      modularity_t1_bin   --        topic_growth_bin           0.4842           0.1219 possible size confound
      modularity_t1_bin   --      topic_share_t1_bin           1.6188           0.0299 possible size confound
      modularity_t1_bin   --                year_bin           0.0218           7.4079 possible size confound
       topic_growth_bin   --      topic_share_t1_bin           0.0860           2.2318
       topic_growth_bin   --                year_bin           0.1986           0.8842
     topic_share_t1_bin   --                year_bin           0.0426           1.8688
```

### Setting 40: sensitivity_outcome:hit_rate_2yr / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 2800.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->        hit_rate_2yr           0.4089           0.0000
cross_topic_rate_t1   ->        hit_rate_2yr           0.1031           0.0000
connectivity_t1_log   ->        hit_rate_2yr           0.8121           0.0000
      modularity_t1   ->        hit_rate_2yr           0.2430           0.0000 possible size confound
               year   ->      topic_share_t1           0.4509           0.0000
               year   -> cross_topic_rate_t1           0.4273           0.0000
               year   -> connectivity_t1_log           0.6618           0.0000
               year   ->       modularity_t1           0.2279           0.0000 possible size confound
               year   ->        hit_rate_2yr           0.6647           0.0000
```

### Setting 41: sensitivity_outcome:hit_rate_2yr / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4200.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.4997           0.0254 possible size confound
     topic_share_t1   ->        hit_rate_2yr           0.4683           0.0117
connectivity_t1_log   -> cross_topic_rate_t1           0.3462           0.0087
connectivity_t1_log   ->       modularity_t1           0.7588           0.0132 possible size confound
connectivity_t1_log   ->        hit_rate_2yr           0.9608           0.0056
      modularity_t1   ->        hit_rate_2yr           0.3448           0.0498 possible size confound
               year   -> cross_topic_rate_t1           0.6452           0.0248
               year   -> connectivity_t1_log           0.6416           0.0509
               year   ->       modularity_t1           0.9905           0.0047 possible size confound
               year   ->        hit_rate_2yr           0.8648           0.0010
       hit_rate_2yr   -> cross_topic_rate_t1           0.1212           0.0001
     topic_share_t1   --                year           0.1286           0.3000
```

### Setting 42: sensitivity_outcome:hit_rate_2yr / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 2900.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->        hit_rate_2yr_bin           0.6657           0.0000
cross_topic_rate_t1_bin   ->        hit_rate_2yr_bin           0.7544           0.0000
    connectivity_t1_bin   ->        hit_rate_2yr_bin           1.1852           0.0000
      modularity_t1_bin   ->        hit_rate_2yr_bin           0.3853           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1267           0.0000
               year_bin   -> cross_topic_rate_t1_bin           1.0917           0.0000
               year_bin   ->     connectivity_t1_bin           1.7259           0.0000
               year_bin   ->       modularity_t1_bin           0.8220           0.0000 possible size confound
               year_bin   ->        hit_rate_2yr_bin           0.7660           0.0000
```

### Setting 43: sensitivity_outcome:hit_rate_2yr / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8000.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0242           2.6441
    connectivity_t1_bin   --        hit_rate_2yr_bin           0.0356           1.3597
    connectivity_t1_bin   --       modularity_t1_bin           0.0215           6.6657 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           4.6534           0.0264
    connectivity_t1_bin   --                year_bin           0.0647           1.8782
cross_topic_rate_t1_bin   --        hit_rate_2yr_bin           0.0250           6.1289
cross_topic_rate_t1_bin   --       modularity_t1_bin           5.5745           0.0242 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           1.4492           0.0401
cross_topic_rate_t1_bin   --                year_bin           0.0251           2.6079
       hit_rate_2yr_bin   --       modularity_t1_bin           2.4759           0.0265 possible size confound
       hit_rate_2yr_bin   --      topic_share_t1_bin           0.6961           0.0714
       hit_rate_2yr_bin   --                year_bin           0.0245           5.9584
      modularity_t1_bin   --      topic_share_t1_bin           2.2998           0.0267 possible size confound
      modularity_t1_bin   --                year_bin           0.0399           1.2069 possible size confound
     topic_share_t1_bin   --                year_bin           0.1436           2.0192
```

### Setting 44: sensitivity_no_year / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 2800.

```
                  a edge               b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->   topic_share_t           0.8814           0.0000
cross_topic_rate_t1   -> log1p_median_c2           0.2983           0.0000
      modularity_t1   -> log1p_median_c2           0.2128           0.0000 possible size confound
```

### Setting 45: sensitivity_no_year / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4500.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5547           0.0084 possible size confound
     topic_share_t1   ->       topic_share_t           0.8427           0.0249
     topic_share_t1   ->     log1p_median_c2           0.7973           0.0005
      modularity_t1   -> connectivity_t1_log           0.1589           0.0448 possible size confound
cross_topic_rate_t1   --     log1p_median_c2           0.0433           0.2841
cross_topic_rate_t1   --       modularity_t1           0.0424           0.2053 possible size confound
cross_topic_rate_t1   --       topic_share_t           0.1689           0.2079
    log1p_median_c2   --       modularity_t1           0.2739           0.0064 possible size confound
    log1p_median_c2   --       topic_share_t           0.0399           0.9714
      modularity_t1   --       topic_share_t           0.1116           0.3345 possible size confound
```

### Setting 46: sensitivity_no_year / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3500.

```
                      a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->   topic_share_t_bin           2.1818           0.0000
     topic_share_t1_bin   -> log1p_median_c2_bin           0.5190           0.0000
cross_topic_rate_t1_bin   ->   topic_share_t_bin           0.5079           0.0000
cross_topic_rate_t1_bin   -> log1p_median_c2_bin           1.1469           0.0000
    connectivity_t1_bin   ->   topic_share_t_bin           0.3584           0.0000
    connectivity_t1_bin   -> log1p_median_c2_bin           1.2062           0.0000
      modularity_t1_bin   ->   topic_share_t_bin           0.3447           0.0000 possible size confound
      modularity_t1_bin   -> log1p_median_c2_bin           0.8616           0.0000 possible size confound
```

### Setting 47: sensitivity_no_year / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 7100.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           1.1636           0.0372
    connectivity_t1_bin   --     log1p_median_c2_bin           2.6076           0.0254
    connectivity_t1_bin   --       modularity_t1_bin           0.6030           0.0959 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0225           6.7035
    connectivity_t1_bin   --       topic_share_t_bin           6.4025           0.0219
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0262           5.8087
cross_topic_rate_t1_bin   --       modularity_t1_bin           3.4766           0.0494 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0582           0.7889
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0263           2.4022
    log1p_median_c2_bin   --       modularity_t1_bin           1.6614           0.0389 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0327           1.2102
    log1p_median_c2_bin   --       topic_share_t_bin           0.0239           5.4128
      modularity_t1_bin   --      topic_share_t1_bin           0.1720           0.5668 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.0554           0.7453 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           3.4257           0.0216
```

### Setting 48: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7835           0.0000
     topic_share_t1   ->     log1p_median_c2           0.1946           0.0000
connectivity_t1_log   ->       topic_share_t           0.1494           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8799           0.0000
      modularity_t1   ->     log1p_median_c2           0.4184           0.0000 possible size confound
               year   ->      topic_share_t1           0.9397           0.0000
               year   -> cross_topic_rate_t1           0.4129           0.0000
               year   -> connectivity_t1_log           0.6264           0.0000
               year   ->     n_papers_t1_log           0.5092           0.0000
               year   ->       topic_share_t           0.2601           0.0000
               year   ->     log1p_median_c2           1.1188           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.9301           0.0000
    n_papers_t1_log   -> connectivity_t1_log           0.0878           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5419           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3179           0.0000
```

### Setting 49: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7835           0.0000
     topic_share_t1   ->     log1p_median_c2           0.1946           0.0000
connectivity_t1_log   ->       topic_share_t           0.1494           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8799           0.0000
      modularity_t1   ->     log1p_median_c2           0.4184           0.0000 possible size confound
               year   ->      topic_share_t1           0.9397           0.0000
               year   -> cross_topic_rate_t1           0.4129           0.0000
               year   -> connectivity_t1_log           0.6264           0.0000
               year   ->     n_papers_t1_log           0.5092           0.0000
               year   ->       topic_share_t           0.2601           0.0000
               year   ->     log1p_median_c2           1.1188           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.9301           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5419           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3179           0.0000
```

### Setting 50: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4700.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7835           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8799           0.0000
      modularity_t1   ->     log1p_median_c2           0.4184           0.0000 possible size confound
               year   ->      topic_share_t1           0.9397           0.0000
               year   -> cross_topic_rate_t1           0.4129           0.0000
               year   -> connectivity_t1_log           0.6264           0.0000
               year   ->     n_papers_t1_log           0.5092           0.0000
               year   ->       topic_share_t           0.2601           0.0000
               year   ->     log1p_median_c2           1.1188           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.9301           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5419           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3179           0.0000
```

### Setting 51: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5000.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8051           0.0000
     topic_share_t1   ->     log1p_median_c2           0.1579           0.0000
connectivity_t1_log   ->       topic_share_t           0.1204           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8056           0.0000
      modularity_t1   ->     log1p_median_c2           0.3632           0.0000 possible size confound
               year   ->      topic_share_t1           0.9278           0.0000
               year   -> cross_topic_rate_t1           0.4091           0.0000
               year   -> connectivity_t1_log           0.6226           0.0000
               year   ->     n_papers_t1_log           0.5035           0.0000
               year   ->       topic_share_t           0.2036           0.0000
               year   ->     log1p_median_c2           1.0270           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.9182           0.0000
    n_papers_t1_log   -> connectivity_t1_log           0.0839           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5300           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3102           0.0000
```

### Setting 52: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5000.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8051           0.0000
     topic_share_t1   ->     log1p_median_c2           0.1579           0.0000
connectivity_t1_log   ->       topic_share_t           0.1204           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8056           0.0000
      modularity_t1   ->     log1p_median_c2           0.3632           0.0000 possible size confound
               year   ->      topic_share_t1           0.9278           0.0000
               year   -> cross_topic_rate_t1           0.4091           0.0000
               year   -> connectivity_t1_log           0.6226           0.0000
               year   ->     n_papers_t1_log           0.5035           0.0000
               year   ->       topic_share_t           0.2036           0.0000
               year   ->     log1p_median_c2           1.0270           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.9182           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5300           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3102           0.0000
```

### Setting 53: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5000.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8051           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.8056           0.0000
      modularity_t1   ->     log1p_median_c2           0.3632           0.0000 possible size confound
               year   ->      topic_share_t1           0.9278           0.0000
               year   -> cross_topic_rate_t1           0.4091           0.0000
               year   -> connectivity_t1_log           0.6226           0.0000
               year   ->     n_papers_t1_log           0.5035           0.0000
               year   ->       topic_share_t           0.2036           0.0000
               year   ->     log1p_median_c2           1.0270           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.9182           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5300           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3102           0.0000
```

### Setting 54: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7983           0.0000
connectivity_t1_log   ->       topic_share_t           0.0666           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.6246           0.0000
      modularity_t1   ->     log1p_median_c2           0.2151           0.0000 possible size confound
               year   ->      topic_share_t1           0.8916           0.0000
               year   -> cross_topic_rate_t1           0.3975           0.0000
               year   -> connectivity_t1_log           0.6110           0.0000
               year   ->     n_papers_t1_log           0.4859           0.0000
               year   ->       topic_share_t           0.1525           0.0000
               year   ->     log1p_median_c2           0.7660           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.8820           0.0000
    n_papers_t1_log   -> connectivity_t1_log           0.0723           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5033           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3400           0.0000
```

### Setting 55: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7983           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.6246           0.0000
      modularity_t1   ->     log1p_median_c2           0.2151           0.0000 possible size confound
               year   ->      topic_share_t1           0.8916           0.0000
               year   -> cross_topic_rate_t1           0.3975           0.0000
               year   -> connectivity_t1_log           0.6110           0.0000
               year   ->     n_papers_t1_log           0.4859           0.0000
               year   ->       topic_share_t           0.1525           0.0000
               year   ->     log1p_median_c2           0.7660           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.8820           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5033           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3400           0.0000
```

### Setting 56: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7983           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.6246           0.0000
      modularity_t1   ->     log1p_median_c2           0.2151           0.0000 possible size confound
               year   ->      topic_share_t1           0.8916           0.0000
               year   -> cross_topic_rate_t1           0.3975           0.0000
               year   -> connectivity_t1_log           0.6110           0.0000
               year   ->     n_papers_t1_log           0.4859           0.0000
               year   ->     log1p_median_c2           0.7660           0.0000
    n_papers_t1_log   ->      topic_share_t1           0.8820           0.0000
    n_papers_t1_log   ->       modularity_t1           0.5033           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3400           0.0000
```

### Setting 57: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4400.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.6450           0.0068
connectivity_t1_log   --     log1p_median_c2           0.7927           0.0194
connectivity_t1_log   --       modularity_t1           0.8116           0.0372 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0225           0.5556
connectivity_t1_log   --       topic_share_t           0.0673           0.1234
connectivity_t1_log   --      topic_share_t1           0.0294           0.5370
connectivity_t1_log   --                year           0.2822           0.0848
cross_topic_rate_t1   --       modularity_t1           0.0001           0.2915 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0076           0.9616
cross_topic_rate_t1   --       topic_share_t           0.0626           0.0104
cross_topic_rate_t1   --      topic_share_t1           0.0419           0.7477
cross_topic_rate_t1   --                year           0.1005           0.0628
    log1p_median_c2   --       modularity_t1           0.0202           0.3845 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.0678           0.1150
    log1p_median_c2   --       topic_share_t           0.0254           0.4028
    log1p_median_c2   --      topic_share_t1           0.0487           0.6784
    log1p_median_c2   --                year           0.0022           1.1606
      modularity_t1   --     n_papers_t1_log           0.1301           0.1382 possible size confound
      modularity_t1   --       topic_share_t           0.1634           0.1054 possible size confound
      modularity_t1   --      topic_share_t1           0.0816           0.3643 possible size confound
      modularity_t1   --                year           0.0025           0.9172 possible size confound
    n_papers_t1_log   --       topic_share_t           0.7494           0.0181
    n_papers_t1_log   --      topic_share_t1           0.2648           0.1429
    n_papers_t1_log   --                year           0.0998           0.3867
      topic_share_t   --      topic_share_t1           0.6268           0.0224
      topic_share_t   --                year           0.0130           0.8314
     topic_share_t1   --                year           0.0997           0.1359
```

### Setting 58: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4400.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->     log1p_median_c2           0.6784           0.0487
connectivity_t1_log   ->     log1p_median_c2           0.7927           0.0194
      modularity_t1   ->     log1p_median_c2           0.3845           0.0202 possible size confound
               year   ->     log1p_median_c2           1.1606           0.0022
    n_papers_t1_log   ->     log1p_median_c2           0.1150           0.0678
      topic_share_t   ->     log1p_median_c2           0.4028           0.0254
connectivity_t1_log   -- cross_topic_rate_t1           0.6450           0.0068
connectivity_t1_log   --       modularity_t1           0.8116           0.0372 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0225           0.5556
connectivity_t1_log   --       topic_share_t           0.0673           0.1234
connectivity_t1_log   --      topic_share_t1           0.0294           0.5370
connectivity_t1_log   --                year           0.2822           0.0848
cross_topic_rate_t1   --       modularity_t1           0.0001           0.2915 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0076           0.9616
cross_topic_rate_t1   --      topic_share_t1           0.0419           0.7477
cross_topic_rate_t1   --                year           0.1005           0.0628
      modularity_t1   --     n_papers_t1_log           0.1301           0.1382 possible size confound
      modularity_t1   --       topic_share_t           0.1634           0.1054 possible size confound
      modularity_t1   --      topic_share_t1           0.0816           0.3643 possible size confound
      modularity_t1   --                year           0.0025           0.9172 possible size confound
    n_papers_t1_log   --       topic_share_t           0.7494           0.0181
    n_papers_t1_log   --      topic_share_t1           0.2648           0.1429
    n_papers_t1_log   --                year           0.0998           0.3867
      topic_share_t   --      topic_share_t1           0.6268           0.0224
      topic_share_t   --                year           0.0130           0.8314
     topic_share_t1   --                year           0.0997           0.1359
```

### Setting 59: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4400.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> cross_topic_rate_t1           0.7477           0.0419
     topic_share_t1   ->       modularity_t1           0.3643           0.0816 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.6784           0.0487
connectivity_t1_log   -> cross_topic_rate_t1           0.6450           0.0068
connectivity_t1_log   ->       modularity_t1           0.8116           0.0372 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7927           0.0194
      modularity_t1   -> cross_topic_rate_t1           0.2915           0.0001 possible size confound
      modularity_t1   ->     log1p_median_c2           0.3845           0.0202 possible size confound
               year   ->       modularity_t1           0.9172           0.0025 possible size confound
               year   ->     log1p_median_c2           1.1606           0.0022
    n_papers_t1_log   -> cross_topic_rate_t1           0.9616           0.0076
      topic_share_t   ->     log1p_median_c2           0.4028           0.0254
connectivity_t1_log   --     n_papers_t1_log           0.0225           0.5556
connectivity_t1_log   --      topic_share_t1           0.0294           0.5370
connectivity_t1_log   --                year           0.2822           0.0848
    n_papers_t1_log   --       topic_share_t           0.7494           0.0181
    n_papers_t1_log   --      topic_share_t1           0.2648           0.1429
    n_papers_t1_log   --                year           0.0998           0.3867
      topic_share_t   --      topic_share_t1           0.6268           0.0224
      topic_share_t   --                year           0.0130           0.8314
```

### Setting 60: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 9300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.5910           0.0099
connectivity_t1_log   --     log1p_median_c2           0.7212           0.0170
connectivity_t1_log   --       modularity_t1           0.7832           0.0396 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0048           0.5340
connectivity_t1_log   --       topic_share_t           0.0180           0.2870
connectivity_t1_log   --      topic_share_t1           0.0156           0.6288
connectivity_t1_log   --                year           0.2499           0.1403
cross_topic_rate_t1   --       modularity_t1           0.0001           0.2393 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0289           0.8675
cross_topic_rate_t1   --      topic_share_t1           0.0097           0.6744
cross_topic_rate_t1   --                year           0.1001           0.0797
    log1p_median_c2   --       modularity_t1           0.0001           0.3044 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.1347           0.0001
    log1p_median_c2   --       topic_share_t           0.0035           0.4107
    log1p_median_c2   --      topic_share_t1           0.0243           0.7236
    log1p_median_c2   --                year           0.0021           1.1553
      modularity_t1   --     n_papers_t1_log           0.1799           0.1048 possible size confound
      modularity_t1   --      topic_share_t1           0.0295           0.4447 possible size confound
      modularity_t1   --                year           0.0001           0.9134 possible size confound
    n_papers_t1_log   --       topic_share_t           0.4461           0.0000
    n_papers_t1_log   --      topic_share_t1           0.0251           0.4377
    n_papers_t1_log   --                year           0.0851           0.4732
      topic_share_t   --      topic_share_t1           0.5749           0.0390
      topic_share_t   --                year           0.0224           0.6248
     topic_share_t1   --                year           0.1885           0.0286
```

### Setting 61: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 9300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.5910           0.0099
connectivity_t1_log   --     log1p_median_c2           0.7212           0.0170
connectivity_t1_log   --       modularity_t1           0.7832           0.0396 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0048           0.5340
connectivity_t1_log   --       topic_share_t           0.0180           0.2870
connectivity_t1_log   --      topic_share_t1           0.0156           0.6288
connectivity_t1_log   --                year           0.2499           0.1403
cross_topic_rate_t1   --       modularity_t1           0.0001           0.2393 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0289           0.8675
cross_topic_rate_t1   --      topic_share_t1           0.0097           0.6744
cross_topic_rate_t1   --                year           0.1001           0.0797
    log1p_median_c2   --       modularity_t1           0.0001           0.3044 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.1347           0.0001
    log1p_median_c2   --       topic_share_t           0.0035           0.4107
    log1p_median_c2   --      topic_share_t1           0.0243           0.7236
    log1p_median_c2   --                year           0.0021           1.1553
      modularity_t1   --     n_papers_t1_log           0.1799           0.1048 possible size confound
      modularity_t1   --      topic_share_t1           0.0295           0.4447 possible size confound
      modularity_t1   --                year           0.0001           0.9134 possible size confound
    n_papers_t1_log   --       topic_share_t           0.4461           0.0000
    n_papers_t1_log   --      topic_share_t1           0.0251           0.4377
    n_papers_t1_log   --                year           0.0851           0.4732
      topic_share_t   --      topic_share_t1           0.5749           0.0390
      topic_share_t   --                year           0.0224           0.6248
     topic_share_t1   --                year           0.1885           0.0286
```

### Setting 62: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 9300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> cross_topic_rate_t1           0.6744           0.0097
     topic_share_t1   ->       modularity_t1           0.4447           0.0295 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.7236           0.0243
connectivity_t1_log   -> cross_topic_rate_t1           0.5910           0.0099
connectivity_t1_log   ->       modularity_t1           0.7832           0.0396 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7212           0.0170
      modularity_t1   -> cross_topic_rate_t1           0.2393           0.0001 possible size confound
      modularity_t1   ->     log1p_median_c2           0.3044           0.0001 possible size confound
               year   ->       modularity_t1           0.9134           0.0001 possible size confound
               year   ->     log1p_median_c2           1.1553           0.0021
    n_papers_t1_log   -> cross_topic_rate_t1           0.8675           0.0289
      topic_share_t   ->     log1p_median_c2           0.4107           0.0035
connectivity_t1_log   --     n_papers_t1_log           0.0048           0.5340
connectivity_t1_log   --       topic_share_t           0.0180           0.2870
connectivity_t1_log   --      topic_share_t1           0.0156           0.6288
connectivity_t1_log   --                year           0.2499           0.1403
    n_papers_t1_log   --       topic_share_t           0.4461           0.0000
    n_papers_t1_log   --      topic_share_t1           0.0251           0.4377
    n_papers_t1_log   --                year           0.0851           0.4732
      topic_share_t   --      topic_share_t1           0.5749           0.0390
      topic_share_t   --                year           0.0224           0.6248
```

### Setting 63: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.3534           0.0332
connectivity_t1_log   --     log1p_median_c2           0.6470           0.0162
connectivity_t1_log   --       modularity_t1           0.7301           0.0342 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0006           0.4127
connectivity_t1_log   --       topic_share_t           0.1539           0.0003
connectivity_t1_log   --      topic_share_t1           0.0007           0.3305
connectivity_t1_log   --                year           0.3173           0.1305
cross_topic_rate_t1   --     n_papers_t1_log           0.0268           0.6154
cross_topic_rate_t1   --      topic_share_t1           0.0036           0.5528
cross_topic_rate_t1   --                year           0.1136           0.0220
    log1p_median_c2   --       modularity_t1           0.0001           0.2668 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.1677           0.0001
    log1p_median_c2   --       topic_share_t           0.0014           0.3346
    log1p_median_c2   --      topic_share_t1           0.0170           0.6123
    log1p_median_c2   --                year           0.0007           1.0691
      modularity_t1   --     n_papers_t1_log           0.0000           0.6246 possible size confound
      modularity_t1   --                year           0.0296           0.4114 possible size confound
    n_papers_t1_log   --       topic_share_t           0.3058           0.0002
    n_papers_t1_log   --      topic_share_t1           0.0003           0.5781
    n_papers_t1_log   --                year           0.0456           0.5638
      topic_share_t   --      topic_share_t1           0.6133           0.0478
      topic_share_t   --                year           0.0157           0.6585
     topic_share_t1   --                year           0.1226           0.0427
```

### Setting 64: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.3534           0.0332
connectivity_t1_log   --     log1p_median_c2           0.6470           0.0162
connectivity_t1_log   --       modularity_t1           0.7301           0.0342 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0006           0.4127
connectivity_t1_log   --       topic_share_t           0.1539           0.0003
connectivity_t1_log   --      topic_share_t1           0.0007           0.3305
connectivity_t1_log   --                year           0.3173           0.1305
cross_topic_rate_t1   --     n_papers_t1_log           0.0268           0.6154
cross_topic_rate_t1   --      topic_share_t1           0.0036           0.5528
cross_topic_rate_t1   --                year           0.1136           0.0220
    log1p_median_c2   --       modularity_t1           0.0001           0.2668 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.1677           0.0001
    log1p_median_c2   --       topic_share_t           0.0014           0.3346
    log1p_median_c2   --      topic_share_t1           0.0170           0.6123
    log1p_median_c2   --                year           0.0007           1.0691
      modularity_t1   --     n_papers_t1_log           0.0000           0.6246 possible size confound
      modularity_t1   --                year           0.0296           0.4114 possible size confound
    n_papers_t1_log   --       topic_share_t           0.3058           0.0002
    n_papers_t1_log   --      topic_share_t1           0.0003           0.5781
    n_papers_t1_log   --                year           0.0456           0.5638
      topic_share_t   --      topic_share_t1           0.6133           0.0478
      topic_share_t   --                year           0.0157           0.6585
     topic_share_t1   --                year           0.1226           0.0427
```

### Setting 65: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> cross_topic_rate_t1           0.5528           0.0036
     topic_share_t1   ->     log1p_median_c2           0.6123           0.0170
connectivity_t1_log   -> cross_topic_rate_t1           0.3534           0.0332
connectivity_t1_log   ->       modularity_t1           0.7301           0.0342 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.6470           0.0162
      modularity_t1   ->     log1p_median_c2           0.2668           0.0001 possible size confound
               year   ->       modularity_t1           0.4114           0.0296 possible size confound
               year   ->     log1p_median_c2           1.0691           0.0007
    n_papers_t1_log   -> cross_topic_rate_t1           0.6154           0.0268
    n_papers_t1_log   ->       modularity_t1           0.6246           0.0000 possible size confound
      topic_share_t   ->     log1p_median_c2           0.3346           0.0014
connectivity_t1_log   --     n_papers_t1_log           0.0006           0.4127
connectivity_t1_log   --      topic_share_t1           0.0007           0.3305
connectivity_t1_log   --                year           0.3173           0.1305
    n_papers_t1_log   --       topic_share_t           0.3058           0.0002
    n_papers_t1_log   --      topic_share_t1           0.0003           0.5781
    n_papers_t1_log   --                year           0.0456           0.5638
      topic_share_t   --      topic_share_t1           0.6133           0.0478
      topic_share_t   --                year           0.0157           0.6585
```

### Setting 66: sensitivity_relaxed_tiers / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 7300.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.4771           0.0642 possible size confound
     topic_share_t1   ->       topic_share_t           0.7820           0.0000
     topic_share_t1   ->     log1p_median_c2           0.7726           0.0000
connectivity_t1_log   ->      topic_share_t1           0.1441           0.0006
connectivity_t1_log   -> cross_topic_rate_t1           0.4862           0.0001
connectivity_t1_log   ->       modularity_t1           0.7729           0.0015 possible size confound
connectivity_t1_log   ->       topic_share_t           0.1688           0.0000
connectivity_t1_log   ->     log1p_median_c2           0.6492           0.0000
      modularity_t1   ->     log1p_median_c2           0.2838           0.0000 possible size confound
               year   ->      topic_share_t1           0.5682           0.0000
               year   -> cross_topic_rate_t1           0.7778           0.0000
               year   -> connectivity_t1_log           0.6656           0.0000
               year   ->       modularity_t1           0.9782           0.0000 possible size confound
               year   ->       topic_share_t           0.2882           0.0000
               year   ->     log1p_median_c2           1.0915           0.0000
      topic_share_t   ->     log1p_median_c2           0.4749           0.0814
```

## Adjacency vs. orientation stability across constrained main-model settings

Across the converged constrained main-model fits, `adjacency_rate` counts any edge between a pair; the direction rates show how those adjacent fits orient it. For pairs spanning different temporal tiers, the temporal constraint fixes direction, so orientation is constraint-imposed rather than independently learned. `same_direction_rate` measures consistency among directed fits.

Pairs are ordered so the more frequent direction points from `a` to `b`; ties use alphabetical order. Rates use all eligible fits, including empty graphs. `a_to_b_rate`, `b_to_a_rate`, and `undirected_rate` sum to `adjacency_rate`; conditional rates divide by adjacent fits only. The directional conditional rates use all adjacent fits as the denominator, including undirected fits. In constrained runs, a zero reverse-direction rate can follow directly from the tier mask forbidding backward arrows; it is not independent evidence for that direction. Orientation frequency and consistency of a particular direction are distinct.

Thresholds from the same fitted model are correlated settings, not independent replications.

### continuous: 9 eligible settings

```
              a                   b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
connectivity_t1     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
           year     connectivity_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
           year cross_topic_rate_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
 topic_share_t1     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
           year     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
           year       modularity_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
 topic_share_t1       topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
           year      topic_share_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
  modularity_t1     log1p_median_c2           8        9          0.8889       0.8889       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
           year       topic_share_t           7        9          0.7778       0.7778       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
connectivity_t1       topic_share_t           4        9          0.4444       0.4444       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

### discretized: 9 eligible settings

```
                  a                   b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1       topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     connectivity_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1       topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year cross_topic_rate_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1       topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       modularity_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1       topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year      topic_share_t1           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

### combined: 18 eligible settings

```
                  a                   b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1     log1p_median_c2          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     connectivity_t1          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year cross_topic_rate_t1          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1     log1p_median_c2          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year     log1p_median_c2          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       modularity_t1          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
     topic_share_t1       topic_share_t          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year      topic_share_t1          18       18          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1     log1p_median_c2          17       18          0.9444       0.9444       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
               year       topic_share_t          16       18          0.8889       0.8889       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1       topic_share_t          13       18          0.7222       0.7222       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1     log1p_median_c2           9       18          0.5000       0.5000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1       topic_share_t           9       18          0.5000       0.5000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1       topic_share_t           9       18          0.5000       0.5000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

## Relaxed-tier sensitivity

Exploratory same-tier edges; not bootstrap-stability classified.

```
representation  lambda1  threshold                   a edge                   b  strength_a_to_b  strength_b_to_a
    continuous   0.0200     0.1000      topic_share_t1   ->       modularity_t1           0.4771           0.0642
    continuous   0.0200     0.1000 connectivity_t1_log   ->      topic_share_t1           0.1441           0.0006
    continuous   0.0200     0.1000 connectivity_t1_log   -> cross_topic_rate_t1           0.4862           0.0001
    continuous   0.0200     0.1000 connectivity_t1_log   ->       modularity_t1           0.7729           0.0015
    continuous   0.0200     0.1000       topic_share_t   ->     log1p_median_c2           0.4749           0.0814
```
