# GOLEM Settings Comparison (v5)

**66 graph settings from 30 fitted models:** 16 converged, 14 reached the iteration limit, 0 failed numerically.

Continuous fits use equal-noise-variance GOLEM on centered, standardized
PC inputs. Discretized fits are a **Gaussian surrogate on centered full one-hot
groups**, with unweighted group lasso replacing L1; this is an extension, not a
categorical probability model. No rows or years are removed. Connectivity and
size use the same log transformations as PC.

## Settings grid

Sensitivity outcomes and no-year runs freeze sparsity=0.02 and threshold=0.10. Size-control uses the continuous grid. No hyperparameter is selected by agreement with PC.

```
 id                            group representation  constrained  lambda1  threshold       status  iterations  directed  undirected  violations_before  violations_after
  0                             main     continuous         True   0.0100     0.0500    converged        4000        11           0                  0                 0
  1                             main     continuous         True   0.0100     0.1000    converged        4000        11           0                  0                 0
  2                             main     continuous         True   0.0100     0.2000    converged        4000        10           0                  0                 0
  3                             main     continuous         True   0.0200     0.0500 nonconverged       10000        11           0                  0                 0
  4                             main     continuous         True   0.0200     0.1000 nonconverged       10000        11           0                  0                 0
  5                             main     continuous         True   0.0200     0.2000 nonconverged       10000         9           0                  0                 0
  6                             main     continuous         True   0.0500     0.0500 nonconverged       10000        10           0                  0                 0
  7                             main     continuous         True   0.0500     0.1000 nonconverged       10000        10           0                  0                 0
  8                             main     continuous         True   0.0500     0.2000 nonconverged       10000         8           0                  0                 0
  9                             main     continuous        False   0.0100     0.0500 nonconverged       10000         9          10                  5                 1
 10                             main     continuous        False   0.0100     0.1000 nonconverged       10000        13           3                  3                 1
 11                             main     continuous        False   0.0100     0.2000 nonconverged       10000        13           3                  3                 1
 12                             main     continuous        False   0.0200     0.0500 nonconverged       10000         0          19                  5                 0
 13                             main     continuous        False   0.0200     0.1000 nonconverged       10000        13           3                  3                 1
 14                             main     continuous        False   0.0200     0.2000 nonconverged       10000        15           0                  2                 2
 15                             main     continuous        False   0.0500     0.0500 nonconverged       10000        11           6                  6                 1
 16                             main     continuous        False   0.0500     0.1000 nonconverged       10000        12           3                  4                 2
 17                             main     continuous        False   0.0500     0.2000 nonconverged       10000        12           0                  1                 1
 18                             main    discretized         True   0.0100     0.0500    converged        5800        14           0                  0                 0
 19                             main    discretized         True   0.0100     0.1000    converged        5800        14           0                  0                 0
 20                             main    discretized         True   0.0100     0.2000    converged        5800        14           0                  0                 0
 21                             main    discretized         True   0.0200     0.0500    converged        5000        14           0                  0                 0
 22                             main    discretized         True   0.0200     0.1000    converged        5000        14           0                  0                 0
 23                             main    discretized         True   0.0200     0.2000    converged        5000        14           0                  0                 0
 24                             main    discretized         True   0.0500     0.0500    converged        3900        14           0                  0                 0
 25                             main    discretized         True   0.0500     0.1000    converged        3900        14           0                  0                 0
 26                             main    discretized         True   0.0500     0.2000    converged        3900        14           0                  0                 0
 27                             main    discretized        False   0.0100     0.0500 nonconverged       10000         0          21                  3                 0
 28                             main    discretized        False   0.0100     0.1000 nonconverged       10000        21           0                  2                 2
 29                             main    discretized        False   0.0100     0.2000 nonconverged       10000        21           0                  2                 2
 30                             main    discretized        False   0.0200     0.0500    converged        8700         0          21                  3                 0
 31                             main    discretized        False   0.0200     0.1000    converged        8700         0          21                  3                 0
 32                             main    discretized        False   0.0200     0.2000    converged        8700        21           0                  2                 2
 33                             main    discretized        False   0.0500     0.0500    converged        5000         0          21                 10                 0
 34                             main    discretized        False   0.0500     0.1000    converged        5000         0          21                 10                 0
 35                             main    discretized        False   0.0500     0.2000    converged        5000         0          20                 10                 0
 36 sensitivity_outcome:topic_growth     continuous         True   0.0200     0.1000    converged        2300         7           0                  0                 0
 37 sensitivity_outcome:topic_growth     continuous        False   0.0200     0.1000 nonconverged       10000        10           0                  0                 0
 38 sensitivity_outcome:topic_growth    discretized         True   0.0200     0.1000    converged        4000         9           0                  0                 0
 39 sensitivity_outcome:topic_growth    discretized        False   0.0200     0.1000    converged        5500         0          15                  2                 0
 40 sensitivity_outcome:hit_rate_2yr     continuous         True   0.0200     0.1000    converged        3000         9           0                  0                 0
 41 sensitivity_outcome:hit_rate_2yr     continuous        False   0.0200     0.1000 nonconverged       10000        11           1                  2                 1
 42 sensitivity_outcome:hit_rate_2yr    discretized         True   0.0200     0.1000    converged        4000         9           0                  0                 0
 43 sensitivity_outcome:hit_rate_2yr    discretized        False   0.0200     0.1000    converged        8400         0          15                  5                 0
 44              sensitivity_no_year     continuous         True   0.0200     0.1000 nonconverged       10000         3           0                  0                 0
 45              sensitivity_no_year     continuous        False   0.0200     0.1000 nonconverged       10000         4           6                  4                 0
 46              sensitivity_no_year    discretized         True   0.0200     0.1000    converged        5200         8           0                  0                 0
 47              sensitivity_no_year    discretized        False   0.0200     0.1000    converged        8100         0          15                  4                 0
 48         sensitivity_size_control     continuous         True   0.0100     0.0500    converged        5200        15           0                  0                 0
 49         sensitivity_size_control     continuous         True   0.0100     0.1000    converged        5200        14           0                  0                 0
 50         sensitivity_size_control     continuous         True   0.0100     0.2000    converged        5200        12           0                  0                 0
 51         sensitivity_size_control     continuous         True   0.0200     0.0500 nonconverged       10000        15           0                  0                 0
 52         sensitivity_size_control     continuous         True   0.0200     0.1000 nonconverged       10000        14           0                  0                 0
 53         sensitivity_size_control     continuous         True   0.0200     0.2000 nonconverged       10000        12           0                  0                 0
 54         sensitivity_size_control     continuous         True   0.0500     0.0500 nonconverged       10000        14           0                  0                 0
 55         sensitivity_size_control     continuous         True   0.0500     0.1000 nonconverged       10000        12           0                  0                 0
 56         sensitivity_size_control     continuous         True   0.0500     0.2000 nonconverged       10000        11           0                  0                 0
 57         sensitivity_size_control     continuous        False   0.0100     0.0500    converged        4900         0          27                  8                 0
 58         sensitivity_size_control     continuous        False   0.0100     0.1000    converged        4900         6          20                  5                 0
 59         sensitivity_size_control     continuous        False   0.0100     0.2000    converged        4900        12           8                  2                 0
 60         sensitivity_size_control     continuous        False   0.0200     0.0500 nonconverged       10000         0          25                  7                 0
 61         sensitivity_size_control     continuous        False   0.0200     0.1000 nonconverged       10000         0          25                  6                 0
 62         sensitivity_size_control     continuous        False   0.0200     0.2000 nonconverged       10000        12           9                  3                 0
 63         sensitivity_size_control     continuous        False   0.0500     0.0500 nonconverged       10000         0          23                  5                 0
 64         sensitivity_size_control     continuous        False   0.0500     0.1000 nonconverged       10000         0          23                  5                 0
 65         sensitivity_size_control     continuous        False   0.0500     0.2000 nonconverged       10000        11           8                  2                 0
```

## Edge detail per setting

### Setting 0: main / continuous / lambda1=0.01 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.526459910943394, 'likelihood': 5.467397713303013, 'sparsity': 5.906219764038047, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8064           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.4339           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1437           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8031           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.3478           0.0000 possible size confound
               year   ->      topic_share_t1           0.4597           0.0000                       
               year   -> cross_topic_rate_t1           0.4361           0.0000                       
               year   -> connectivity_t1_log           0.6706           0.0000                       
               year   ->       modularity_t1           0.2367           0.0000 possible size confound
               year   ->       topic_share_t           0.2309           0.0000                       
               year   ->     log1p_median_c2           1.3110           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 1: main / continuous / lambda1=0.01 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.526459910943394, 'likelihood': 5.467397713303013, 'sparsity': 5.906219764038047, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8064           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.4339           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1437           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8031           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.3478           0.0000 possible size confound
               year   ->      topic_share_t1           0.4597           0.0000                       
               year   -> cross_topic_rate_t1           0.4361           0.0000                       
               year   -> connectivity_t1_log           0.6706           0.0000                       
               year   ->       modularity_t1           0.2367           0.0000 possible size confound
               year   ->       topic_share_t           0.2309           0.0000                       
               year   ->     log1p_median_c2           1.3110           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 2: main / continuous / lambda1=0.01 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.526459910943394, 'likelihood': 5.467397713303013, 'sparsity': 5.906219764038047, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8064           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.4339           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8031           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.3478           0.0000 possible size confound
               year   ->      topic_share_t1           0.4597           0.0000                       
               year   -> cross_topic_rate_t1           0.4361           0.0000                       
               year   -> connectivity_t1_log           0.6706           0.0000                       
               year   ->       modularity_t1           0.2367           0.0000 possible size confound
               year   ->       topic_share_t           0.2309           0.0000                       
               year   ->     log1p_median_c2           1.3110           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 3: main / continuous / lambda1=0.02 / threshold=0.05 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.583505029304953, 'likelihood': 5.473159175916959, 'sparsity': 5.517292669399705, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8045           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.3847           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1139           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.7265           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.2869           0.0000 possible size confound
               year   ->      topic_share_t1           0.4528           0.0000                       
               year   -> cross_topic_rate_t1           0.4293           0.0000                       
               year   -> connectivity_t1_log           0.6637           0.0000                       
               year   ->       modularity_t1           0.2299           0.0000 possible size confound
               year   ->       topic_share_t           0.1973           0.0000                       
               year   ->     log1p_median_c2           1.2111           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 4: main / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.583505029304953, 'likelihood': 5.473159175916959, 'sparsity': 5.517292669399705, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8045           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.3847           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1139           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.7265           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.2869           0.0000 possible size confound
               year   ->      topic_share_t1           0.4528           0.0000                       
               year   -> cross_topic_rate_t1           0.4293           0.0000                       
               year   -> connectivity_t1_log           0.6637           0.0000                       
               year   ->       modularity_t1           0.2299           0.0000 possible size confound
               year   ->       topic_share_t           0.1973           0.0000                       
               year   ->     log1p_median_c2           1.2111           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 5: main / continuous / lambda1=0.02 / threshold=0.2 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.583505029304953, 'likelihood': 5.473159175916959, 'sparsity': 5.517292669399705, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8045           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.3847           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.7265           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.2869           0.0000 possible size confound
               year   ->      topic_share_t1           0.4528           0.0000                       
               year   -> cross_topic_rate_t1           0.4293           0.0000                       
               year   -> connectivity_t1_log           0.6637           0.0000                       
               year   ->       modularity_t1           0.2299           0.0000 possible size confound
               year   ->     log1p_median_c2           1.2111           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 6: main / continuous / lambda1=0.05 / threshold=0.05 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.733088513545739, 'likelihood': 5.5105898265316045, 'sparsity': 4.449973740282688, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7964           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.2343           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.4926           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.1009           0.0000 possible size confound
               year   ->      topic_share_t1           0.4320           0.0000                       
               year   -> cross_topic_rate_t1           0.4085           0.0000                       
               year   -> connectivity_t1_log           0.6429           0.0000                       
               year   ->       modularity_t1           0.2090           0.0000 possible size confound
               year   ->       topic_share_t           0.1368           0.0000                       
               year   ->     log1p_median_c2           0.9059           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 7: main / continuous / lambda1=0.05 / threshold=0.1 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.733088513545739, 'likelihood': 5.5105898265316045, 'sparsity': 4.449973740282688, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7964           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.2343           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.4926           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.1009           0.0000 possible size confound
               year   ->      topic_share_t1           0.4320           0.0000                       
               year   -> cross_topic_rate_t1           0.4085           0.0000                       
               year   -> connectivity_t1_log           0.6429           0.0000                       
               year   ->       modularity_t1           0.2090           0.0000 possible size confound
               year   ->       topic_share_t           0.1368           0.0000                       
               year   ->     log1p_median_c2           0.9059           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 8: main / continuous / lambda1=0.05 / threshold=0.2 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.733088513545739, 'likelihood': 5.5105898265316045, 'sparsity': 4.449973740282688, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7964           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.2343           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.4926           0.0000                       
               year   ->      topic_share_t1           0.4320           0.0000                       
               year   -> cross_topic_rate_t1           0.4085           0.0000                       
               year   -> connectivity_t1_log           0.6429           0.0000                       
               year   ->       modularity_t1           0.2090           0.0000 possible size confound
               year   ->     log1p_median_c2           0.9059           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 9: main / continuous / lambda1=0.01 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.846057316370644, 'likelihood': 4.680758000540324, 'sparsity': 11.266993457958261, 'dag': 0.010525876250147448}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->     log1p_median_c2           0.8126           0.0335                       
connectivity_t1_log   -> cross_topic_rate_t1           0.5252           0.0003                       
connectivity_t1_log   ->     log1p_median_c2           0.7944           0.0002                       
      modularity_t1   -> cross_topic_rate_t1           0.1000           0.0007 possible size confound
      modularity_t1   ->     log1p_median_c2           0.3875           0.0491 possible size confound
               year   -> cross_topic_rate_t1           0.8060           0.0188                       
               year   ->     log1p_median_c2           1.2733           0.0087                       
      topic_share_t   -> cross_topic_rate_t1           0.0705           0.0299                       
      topic_share_t   ->     log1p_median_c2           0.4165           0.0005                       
connectivity_t1_log   --       modularity_t1           0.7938           0.0002 possible size confound
connectivity_t1_log   --       topic_share_t           0.0001           0.5779                       
connectivity_t1_log   --      topic_share_t1           0.0690           0.4564                       
connectivity_t1_log   --                year           0.0493           0.7424                       
      modularity_t1   --       topic_share_t           0.0526           0.0089 possible size confound
      modularity_t1   --      topic_share_t1           0.0730           0.5156 possible size confound
      modularity_t1   --                year           0.0101           0.9947 possible size confound
      topic_share_t   --      topic_share_t1           0.8040           0.0515                       
      topic_share_t   --                year           0.0872           0.2875                       
     topic_share_t1   --                year           0.2089           0.0586                       
```

Cyclic components: `[['connectivity_t1_log', 'modularity_t1', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'modularity_t1'], ['topic_share_t1', 'year'], ['topic_share_t1', 'topic_share_t'], ['connectivity_t1_log', 'topic_share_t1'], ['connectivity_t1_log', 'modularity_t1'], ['modularity_t1', 'topic_share_t1'], ['modularity_t1', 'topic_share_t'], ['year', 'topic_share_t1'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'year']]`.

### Setting 10: main / continuous / lambda1=0.01 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.846057316370644, 'likelihood': 4.680758000540324, 'sparsity': 11.266993457958261, 'dag': 0.010525876250147448}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4564           0.0690                       
     topic_share_t1   ->       modularity_t1           0.5156           0.0730 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.8126           0.0335                       
connectivity_t1_log   -> cross_topic_rate_t1           0.5252           0.0003                       
connectivity_t1_log   ->       modularity_t1           0.7938           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7944           0.0002                       
      modularity_t1   ->     log1p_median_c2           0.3875           0.0491 possible size confound
               year   -> cross_topic_rate_t1           0.8060           0.0188                       
               year   -> connectivity_t1_log           0.7424           0.0493                       
               year   ->       modularity_t1           0.9947           0.0101 possible size confound
               year   ->     log1p_median_c2           1.2733           0.0087                       
      topic_share_t   -> connectivity_t1_log           0.5779           0.0001                       
      topic_share_t   ->     log1p_median_c2           0.4165           0.0005                       
      topic_share_t   --      topic_share_t1           0.8040           0.0515                       
      topic_share_t   --                year           0.0872           0.2875                       
     topic_share_t1   --                year           0.2089           0.0586                       
```

Cyclic components: `[['topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'year'], ['year', 'topic_share_t'], ['topic_share_t', 'topic_share_t1']]`.

### Setting 11: main / continuous / lambda1=0.01 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.846057316370644, 'likelihood': 4.680758000540324, 'sparsity': 11.266993457958261, 'dag': 0.010525876250147448}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4564           0.0690                       
     topic_share_t1   ->       modularity_t1           0.5156           0.0730 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.8126           0.0335                       
connectivity_t1_log   -> cross_topic_rate_t1           0.5252           0.0003                       
connectivity_t1_log   ->       modularity_t1           0.7938           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7944           0.0002                       
      modularity_t1   ->     log1p_median_c2           0.3875           0.0491 possible size confound
               year   -> cross_topic_rate_t1           0.8060           0.0188                       
               year   -> connectivity_t1_log           0.7424           0.0493                       
               year   ->       modularity_t1           0.9947           0.0101 possible size confound
               year   ->     log1p_median_c2           1.2733           0.0087                       
      topic_share_t   -> connectivity_t1_log           0.5779           0.0001                       
      topic_share_t   ->     log1p_median_c2           0.4165           0.0005                       
      topic_share_t   --      topic_share_t1           0.8040           0.0515                       
      topic_share_t   --                year           0.0872           0.2875                       
     topic_share_t1   --                year           0.2089           0.0586                       
```

Cyclic components: `[['topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'year'], ['year', 'topic_share_t'], ['topic_share_t', 'topic_share_t1']]`.

### Setting 12: main / continuous / lambda1=0.02 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.95488886556411, 'likelihood': 4.698376753014124, 'sparsity': 10.496119952676917, 'dag': 0.009317942699289539}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.4101           0.0039                       
connectivity_t1_log   --     log1p_median_c2           0.7309           0.0001                       
connectivity_t1_log   --       modularity_t1           0.8028           0.0002 possible size confound
connectivity_t1_log   --       topic_share_t           0.0001           0.5412                       
connectivity_t1_log   --      topic_share_t1           0.0653           0.4237                       
connectivity_t1_log   --                year           0.0494           0.7353                       
cross_topic_rate_t1   --     log1p_median_c2           0.0001           0.0649                       
cross_topic_rate_t1   --      topic_share_t1           0.0691           0.0003                       
cross_topic_rate_t1   --                year           0.0284           0.6462                       
    log1p_median_c2   --       modularity_t1           0.0342           0.3276 possible size confound
    log1p_median_c2   --       topic_share_t           0.0005           0.3863                       
    log1p_median_c2   --      topic_share_t1           0.0329           0.7436                       
    log1p_median_c2   --                year           0.0100           1.1920                       
      modularity_t1   --       topic_share_t           0.0512           0.0003 possible size confound
      modularity_t1   --      topic_share_t1           0.0651           0.5201 possible size confound
      modularity_t1   --                year           0.0092           1.0180 possible size confound
      topic_share_t   --      topic_share_t1           0.7890           0.0530                       
      topic_share_t   --                year           0.0831           0.2960                       
     topic_share_t1   --                year           0.1980           0.0509                       
```

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'modularity_t1'], ['topic_share_t1', 'year'], ['topic_share_t1', 'topic_share_t'], ['topic_share_t1', 'log1p_median_c2'], ['cross_topic_rate_t1', 'topic_share_t1'], ['connectivity_t1_log', 'topic_share_t1'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'log1p_median_c2'], ['modularity_t1', 'topic_share_t1'], ['modularity_t1', 'topic_share_t'], ['modularity_t1', 'log1p_median_c2'], ['year', 'topic_share_t1'], ['year', 'cross_topic_rate_t1'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'topic_share_t'], ['year', 'log1p_median_c2'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'year'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'cross_topic_rate_t1']]`.

### Setting 13: main / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.95488886556411, 'likelihood': 4.698376753014124, 'sparsity': 10.496119952676917, 'dag': 0.009317942699289539}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4237           0.0653                       
     topic_share_t1   ->       modularity_t1           0.5201           0.0651 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.7436           0.0329                       
connectivity_t1_log   -> cross_topic_rate_t1           0.4101           0.0039                       
connectivity_t1_log   ->       modularity_t1           0.8028           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7309           0.0001                       
      modularity_t1   ->     log1p_median_c2           0.3276           0.0342 possible size confound
               year   -> cross_topic_rate_t1           0.6462           0.0284                       
               year   -> connectivity_t1_log           0.7353           0.0494                       
               year   ->       modularity_t1           1.0180           0.0092 possible size confound
               year   ->     log1p_median_c2           1.1920           0.0100                       
      topic_share_t   -> connectivity_t1_log           0.5412           0.0001                       
      topic_share_t   ->     log1p_median_c2           0.3863           0.0005                       
      topic_share_t   --      topic_share_t1           0.7890           0.0530                       
      topic_share_t   --                year           0.0831           0.2960                       
     topic_share_t1   --                year           0.1980           0.0509                       
```

Cyclic components: `[['topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'year'], ['year', 'topic_share_t'], ['topic_share_t', 'topic_share_t1']]`.

### Setting 14: main / continuous / lambda1=0.02 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.95488886556411, 'likelihood': 4.698376753014124, 'sparsity': 10.496119952676917, 'dag': 0.009317942699289539}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> connectivity_t1_log           0.4237           0.0653                       
     topic_share_t1   ->       modularity_t1           0.5201           0.0651 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.7436           0.0329                       
connectivity_t1_log   -> cross_topic_rate_t1           0.4101           0.0039                       
connectivity_t1_log   ->       modularity_t1           0.8028           0.0002 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7309           0.0001                       
      modularity_t1   ->     log1p_median_c2           0.3276           0.0342 possible size confound
               year   -> cross_topic_rate_t1           0.6462           0.0284                       
               year   -> connectivity_t1_log           0.7353           0.0494                       
               year   ->       modularity_t1           1.0180           0.0092 possible size confound
               year   ->       topic_share_t           0.2960           0.0831                       
               year   ->     log1p_median_c2           1.1920           0.0100                       
      topic_share_t   ->      topic_share_t1           0.7890           0.0530                       
      topic_share_t   -> connectivity_t1_log           0.5412           0.0001                       
      topic_share_t   ->     log1p_median_c2           0.3863           0.0005                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 15: main / continuous / lambda1=0.05 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.236371816949729, 'likelihood': 4.804133018028432, 'sparsity': 8.054811491344815, 'dag': 0.005899644870811294}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

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

Cyclic components: `[['connectivity_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'year'], ['topic_share_t1', 'topic_share_t'], ['connectivity_t1_log', 'year'], ['year', 'connectivity_t1_log'], ['year', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'year']]`.

### Setting 16: main / continuous / lambda1=0.05 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.236371816949729, 'likelihood': 4.804133018028432, 'sparsity': 8.054811491344815, 'dag': 0.005899644870811294}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

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

Cyclic components: `[['topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'year'], ['year', 'topic_share_t'], ['topic_share_t', 'topic_share_t1']]`.

### Setting 17: main / continuous / lambda1=0.05 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.236371816949729, 'likelihood': 4.804133018028432, 'sparsity': 8.054811491344815, 'dag': 0.005899644870811294}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_share_t`, `log1p_median_c2`.

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

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 18: main / discretized / lambda1=0.01 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5800.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.062744268357372, 'likelihood': 14.010841251963736, 'sparsity': 5.190301639363542, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0962           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3124           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4813           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7335           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.5293           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9501           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.3663           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7167           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1380           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.1045           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7197           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8363           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.6124           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.5088           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 19: main / discretized / lambda1=0.01 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5800.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.062744268357372, 'likelihood': 14.010841251963736, 'sparsity': 5.190301639363542, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0962           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3124           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4813           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7335           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.5293           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9501           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.3663           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7167           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1380           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.1045           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7197           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8363           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.6124           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.5088           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 20: main / discretized / lambda1=0.01 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5800.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.062744268357372, 'likelihood': 14.010841251963736, 'sparsity': 5.190301639363542, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0962           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3124           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4813           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7335           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.5293           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9501           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.3663           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7167           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1380           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.1045           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7197           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8363           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.6124           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.5088           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 21: main / discretized / lambda1=0.02 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.11413334827581, 'likelihood': 14.01236596324546, 'sparsity': 5.088369251517571, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0853           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3019           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4565           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7235           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.4980           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9278           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.3460           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7070           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1243           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0906           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7033           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8239           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.5750           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.4780           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 22: main / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.11413334827581, 'likelihood': 14.01236596324546, 'sparsity': 5.088369251517571, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0853           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3019           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4565           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7235           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.4980           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9278           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.3460           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7070           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1243           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0906           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7033           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8239           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.5750           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.4780           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 23: main / discretized / lambda1=0.02 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.11413334827581, 'likelihood': 14.01236596324546, 'sparsity': 5.088369251517571, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0853           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.3019           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4565           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7235           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.4980           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.9278           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.3460           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.7070           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1243           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0906           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7033           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8239           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.5750           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.4780           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 24: main / discretized / lambda1=0.05 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3900.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.262367863267254, 'likelihood': 14.022503401096296, 'sparsity': 4.797289243419172, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0652           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.2687           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4064           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.6935           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.4094           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.8722           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.2843           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.6760           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.0835           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0488           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.6578           0.0000                       
               year_bin   ->       modularity_t1_bin           0.7869           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.4730           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.3947           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 25: main / discretized / lambda1=0.05 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3900.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.262367863267254, 'likelihood': 14.022503401096296, 'sparsity': 4.797289243419172, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0652           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.2687           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4064           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.6935           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.4094           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.8722           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.2843           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.6760           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.0835           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0488           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.6578           0.0000                       
               year_bin   ->       modularity_t1_bin           0.7869           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.4730           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.3947           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 26: main / discretized / lambda1=0.05 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3900.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 14.262367863267254, 'likelihood': 14.022503401096296, 'sparsity': 4.797289243419172, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->       topic_share_t_bin           2.0652           0.0000                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           0.2687           0.0000                       
cross_topic_rate_t1_bin   ->       topic_share_t_bin           0.4064           0.0000                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.6935           0.0000                       
    connectivity_t1_bin   ->       topic_share_t_bin           0.4094           0.0000                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           0.8722           0.0000                       
      modularity_t1_bin   ->       topic_share_t_bin           0.2843           0.0000 possible size confound
      modularity_t1_bin   ->     log1p_median_c2_bin           0.6760           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.0835           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0488           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.6578           0.0000                       
               year_bin   ->       modularity_t1_bin           0.7869           0.0000 possible size confound
               year_bin   ->       topic_share_t_bin           0.4730           0.0000                       
               year_bin   ->     log1p_median_c2_bin           1.3947           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 27: main / discretized / lambda1=0.01 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.443277903970204, 'likelihood': 10.711559396138965, 'sparsity': 26.068429343606994, 'dag': 0.09420684287903391}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0062           3.8780                       
    connectivity_t1_bin   --     log1p_median_c2_bin           3.3122           0.0071                       
    connectivity_t1_bin   --       modularity_t1_bin           1.0102           0.0138 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0064           9.0449                       
    connectivity_t1_bin   --       topic_share_t_bin           8.0206           0.0074                       
    connectivity_t1_bin   --                year_bin           0.0068           2.7168                       
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.7287           0.0115                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           0.4351           0.0331 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           7.1149           0.0135                       
cross_topic_rate_t1_bin   --       topic_share_t_bin           1.6102           0.0071                       
cross_topic_rate_t1_bin   --                year_bin           0.0145           8.4694                       
    log1p_median_c2_bin   --       modularity_t1_bin           3.6973           0.0403 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0071           1.6218                       
    log1p_median_c2_bin   --       topic_share_t_bin           0.0091           6.8261                       
    log1p_median_c2_bin   --                year_bin           0.0181           1.5632                       
      modularity_t1_bin   --      topic_share_t1_bin           0.0174           1.3407 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.0121           1.6537 possible size confound
      modularity_t1_bin   --                year_bin           0.0591           1.4362 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           4.2912           0.0055                       
     topic_share_t1_bin   --                year_bin           0.0072           3.6249                       
      topic_share_t_bin   --                year_bin           0.0095           0.7648                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'connectivity_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'topic_share_t_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t1_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t_bin'], ['cross_topic_rate_t1_bin', 'log1p_median_c2_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'topic_share_t_bin'], ['connectivity_t1_bin', 'log1p_median_c2_bin'], ['modularity_t1_bin', 'year_bin'], ['year_bin', 'topic_share_t1_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['year_bin', 'topic_share_t_bin'], ['year_bin', 'log1p_median_c2_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin']]`.

### Setting 28: main / discretized / lambda1=0.01 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.443277903970204, 'likelihood': 10.711559396138965, 'sparsity': 26.068429343606994, 'dag': 0.09420684287903391}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->     connectivity_t1_bin           9.0449           0.0064                       
     topic_share_t1_bin   ->       modularity_t1_bin           1.3407           0.0174 possible size confound
     topic_share_t1_bin   ->       topic_share_t_bin           4.2912           0.0055                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           1.6218           0.0071                       
cross_topic_rate_t1_bin   ->      topic_share_t1_bin           7.1149           0.0135                       
cross_topic_rate_t1_bin   ->     connectivity_t1_bin           3.8780           0.0062                       
cross_topic_rate_t1_bin   ->       modularity_t1_bin           0.4351           0.0331 possible size confound
cross_topic_rate_t1_bin   ->       topic_share_t_bin           1.6102           0.0071                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7287           0.0115                       
    connectivity_t1_bin   ->       modularity_t1_bin           1.0102           0.0138 possible size confound
    connectivity_t1_bin   ->       topic_share_t_bin           8.0206           0.0074                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           3.3122           0.0071                       
               year_bin   ->      topic_share_t1_bin           3.6249           0.0072                       
               year_bin   -> cross_topic_rate_t1_bin           8.4694           0.0145                       
               year_bin   ->     connectivity_t1_bin           2.7168           0.0068                       
               year_bin   ->       modularity_t1_bin           1.4362           0.0591 possible size confound
               year_bin   ->       topic_share_t_bin           0.7648           0.0095                       
               year_bin   ->     log1p_median_c2_bin           1.5632           0.0181                       
      topic_share_t_bin   ->       modularity_t1_bin           1.6537           0.0121 possible size confound
      topic_share_t_bin   ->     log1p_median_c2_bin           6.8261           0.0091                       
    log1p_median_c2_bin   ->       modularity_t1_bin           3.6973           0.0403 possible size confound
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 29: main / discretized / lambda1=0.01 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.443277903970204, 'likelihood': 10.711559396138965, 'sparsity': 26.068429343606994, 'dag': 0.09420684287903391}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->     connectivity_t1_bin           9.0449           0.0064                       
     topic_share_t1_bin   ->       modularity_t1_bin           1.3407           0.0174 possible size confound
     topic_share_t1_bin   ->       topic_share_t_bin           4.2912           0.0055                       
     topic_share_t1_bin   ->     log1p_median_c2_bin           1.6218           0.0071                       
cross_topic_rate_t1_bin   ->      topic_share_t1_bin           7.1149           0.0135                       
cross_topic_rate_t1_bin   ->     connectivity_t1_bin           3.8780           0.0062                       
cross_topic_rate_t1_bin   ->       modularity_t1_bin           0.4351           0.0331 possible size confound
cross_topic_rate_t1_bin   ->       topic_share_t_bin           1.6102           0.0071                       
cross_topic_rate_t1_bin   ->     log1p_median_c2_bin           0.7287           0.0115                       
    connectivity_t1_bin   ->       modularity_t1_bin           1.0102           0.0138 possible size confound
    connectivity_t1_bin   ->       topic_share_t_bin           8.0206           0.0074                       
    connectivity_t1_bin   ->     log1p_median_c2_bin           3.3122           0.0071                       
               year_bin   ->      topic_share_t1_bin           3.6249           0.0072                       
               year_bin   -> cross_topic_rate_t1_bin           8.4694           0.0145                       
               year_bin   ->     connectivity_t1_bin           2.7168           0.0068                       
               year_bin   ->       modularity_t1_bin           1.4362           0.0591 possible size confound
               year_bin   ->       topic_share_t_bin           0.7648           0.0095                       
               year_bin   ->     log1p_median_c2_bin           1.5632           0.0181                       
      topic_share_t_bin   ->       modularity_t1_bin           1.6537           0.0121 possible size confound
      topic_share_t_bin   ->     log1p_median_c2_bin           6.8261           0.0091                       
    log1p_median_c2_bin   ->       modularity_t1_bin           3.6973           0.0403 possible size confound
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 30: main / discretized / lambda1=0.02 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8700.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.685335640836493, 'likelihood': 10.760180683934149, 'sparsity': 22.807599987768732, 'dag': 0.09380059142939423}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

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

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'connectivity_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'topic_share_t_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t1_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t_bin'], ['cross_topic_rate_t1_bin', 'log1p_median_c2_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'topic_share_t_bin'], ['connectivity_t1_bin', 'log1p_median_c2_bin'], ['modularity_t1_bin', 'cross_topic_rate_t1_bin'], ['modularity_t1_bin', 'year_bin'], ['year_bin', 'topic_share_t1_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['year_bin', 'topic_share_t_bin'], ['year_bin', 'log1p_median_c2_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin']]`.

### Setting 31: main / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8700.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.685335640836493, 'likelihood': 10.760180683934149, 'sparsity': 22.807599987768732, 'dag': 0.09380059142939423}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

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

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'connectivity_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'topic_share_t_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t1_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t_bin'], ['cross_topic_rate_t1_bin', 'log1p_median_c2_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'topic_share_t_bin'], ['connectivity_t1_bin', 'log1p_median_c2_bin'], ['modularity_t1_bin', 'year_bin'], ['year_bin', 'topic_share_t1_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['year_bin', 'topic_share_t_bin'], ['year_bin', 'log1p_median_c2_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin']]`.

### Setting 32: main / discretized / lambda1=0.02 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8700.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.685335640836493, 'likelihood': 10.760180683934149, 'sparsity': 22.807599987768732, 'dag': 0.09380059142939423}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

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

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 33: main / discretized / lambda1=0.05 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 12.315366169519674, 'likelihood': 10.959677229886289, 'sparsity': 17.712781570860347, 'dag': 0.09400997221807383}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0110           6.4226                       
    connectivity_t1_bin   --     log1p_median_c2_bin           0.0162           1.0340                       
    connectivity_t1_bin   --       modularity_t1_bin           3.7377           0.0165 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0404           0.1769                       
    connectivity_t1_bin   --       topic_share_t_bin           0.0805           0.5154                       
    connectivity_t1_bin   --                year_bin           0.0102           2.8178                       
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0118           2.1210                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           1.4495           0.0175 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0236           0.7906                       
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0408           0.3821                       
cross_topic_rate_t1_bin   --                year_bin           0.0112           6.6009                       
    log1p_median_c2_bin   --       modularity_t1_bin           0.8913           0.0488 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0156           4.3920                       
    log1p_median_c2_bin   --       topic_share_t_bin           0.0189           1.7510                       
    log1p_median_c2_bin   --                year_bin           5.5222           0.0302                       
      modularity_t1_bin   --      topic_share_t1_bin           0.1393           0.7791 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.3000           0.4991 possible size confound
      modularity_t1_bin   --                year_bin           0.0248           1.0731 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           0.0455           5.7993                       
     topic_share_t1_bin   --                year_bin           1.6041           0.0156                       
      topic_share_t_bin   --                year_bin           0.5078           0.0241                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t1_bin', 'connectivity_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'year_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'topic_share_t_bin'], ['modularity_t1_bin', 'topic_share_t1_bin'], ['modularity_t1_bin', 'topic_share_t_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'topic_share_t1_bin'], ['topic_share_t_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t_bin', 'connectivity_t1_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'year_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'cross_topic_rate_t1_bin'], ['log1p_median_c2_bin', 'connectivity_t1_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin'], ['log1p_median_c2_bin', 'year_bin']]`.

### Setting 34: main / discretized / lambda1=0.05 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 12.315366169519674, 'likelihood': 10.959677229886289, 'sparsity': 17.712781570860347, 'dag': 0.09400997221807383}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0110           6.4226                       
    connectivity_t1_bin   --     log1p_median_c2_bin           0.0162           1.0340                       
    connectivity_t1_bin   --       modularity_t1_bin           3.7377           0.0165 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0404           0.1769                       
    connectivity_t1_bin   --       topic_share_t_bin           0.0805           0.5154                       
    connectivity_t1_bin   --                year_bin           0.0102           2.8178                       
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0118           2.1210                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           1.4495           0.0175 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0236           0.7906                       
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0408           0.3821                       
cross_topic_rate_t1_bin   --                year_bin           0.0112           6.6009                       
    log1p_median_c2_bin   --       modularity_t1_bin           0.8913           0.0488 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0156           4.3920                       
    log1p_median_c2_bin   --       topic_share_t_bin           0.0189           1.7510                       
    log1p_median_c2_bin   --                year_bin           5.5222           0.0302                       
      modularity_t1_bin   --      topic_share_t1_bin           0.1393           0.7791 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.3000           0.4991 possible size confound
      modularity_t1_bin   --                year_bin           0.0248           1.0731 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           0.0455           5.7993                       
     topic_share_t1_bin   --                year_bin           1.6041           0.0156                       
      topic_share_t_bin   --                year_bin           0.5078           0.0241                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t1_bin', 'connectivity_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'year_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['modularity_t1_bin', 'topic_share_t1_bin'], ['modularity_t1_bin', 'topic_share_t_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'topic_share_t1_bin'], ['topic_share_t_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t_bin', 'connectivity_t1_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'year_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'cross_topic_rate_t1_bin'], ['log1p_median_c2_bin', 'connectivity_t1_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin'], ['log1p_median_c2_bin', 'year_bin']]`.

### Setting 35: main / discretized / lambda1=0.05 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 12.315366169519674, 'likelihood': 10.959677229886289, 'sparsity': 17.712781570860347, 'dag': 0.09400997221807383}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0110           6.4226                       
    connectivity_t1_bin   --     log1p_median_c2_bin           0.0162           1.0340                       
    connectivity_t1_bin   --       modularity_t1_bin           3.7377           0.0165 possible size confound
    connectivity_t1_bin   --       topic_share_t_bin           0.0805           0.5154                       
    connectivity_t1_bin   --                year_bin           0.0102           2.8178                       
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0118           2.1210                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           1.4495           0.0175 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0236           0.7906                       
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0408           0.3821                       
cross_topic_rate_t1_bin   --                year_bin           0.0112           6.6009                       
    log1p_median_c2_bin   --       modularity_t1_bin           0.8913           0.0488 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0156           4.3920                       
    log1p_median_c2_bin   --       topic_share_t_bin           0.0189           1.7510                       
    log1p_median_c2_bin   --                year_bin           5.5222           0.0302                       
      modularity_t1_bin   --      topic_share_t1_bin           0.1393           0.7791 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.3000           0.4991 possible size confound
      modularity_t1_bin   --                year_bin           0.0248           1.0731 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           0.0455           5.7993                       
     topic_share_t1_bin   --                year_bin           1.6041           0.0156                       
      topic_share_t_bin   --                year_bin           0.5078           0.0241                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'year_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['modularity_t1_bin', 'topic_share_t_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'topic_share_t1_bin'], ['topic_share_t_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t_bin', 'connectivity_t1_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'year_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'cross_topic_rate_t1_bin'], ['log1p_median_c2_bin', 'connectivity_t1_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin'], ['log1p_median_c2_bin', 'year_bin']]`.

### Setting 36: sensitivity_outcome:topic_growth / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 2300.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.85658041743545, 'likelihood': 4.803177034627585, 'sparsity': 2.6701691403932215, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_growth`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->        topic_growth           0.1919           0.0000                       
connectivity_t1_log   ->        topic_growth           0.2482           0.0000                       
               year   ->      topic_share_t1           0.4500           0.0000                       
               year   -> cross_topic_rate_t1           0.4264           0.0000                       
               year   -> connectivity_t1_log           0.6608           0.0000                       
               year   ->       modularity_t1           0.2270           0.0000 possible size confound
               year   ->        topic_growth           0.4199           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 37: sensitivity_outcome:topic_growth / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.461810209350346, 'likelihood': 4.334251712149534, 'sparsity': 5.831833525308413, 'dag': 0.002184365338928629}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `topic_growth`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5274           0.0085 possible size confound
     topic_share_t1   ->        topic_growth           0.1788           0.0202                       
connectivity_t1_log   -> cross_topic_rate_t1           0.4506           0.0187                       
connectivity_t1_log   ->       modularity_t1           0.8130           0.0183 possible size confound
connectivity_t1_log   ->        topic_growth           0.2489           0.0040                       
               year   ->      topic_share_t1           0.4237           0.0628                       
               year   -> cross_topic_rate_t1           0.7233           0.0175                       
               year   -> connectivity_t1_log           0.6173           0.0491                       
               year   ->       modularity_t1           1.0461           0.0028 possible size confound
               year   ->        topic_growth           0.3961           0.0158                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 38: sensitivity_outcome:topic_growth / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.497907226522916, 'likelihood': 11.434747074077531, 'sparsity': 3.158007622269168, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_growth_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->        topic_growth_bin           0.8318           0.0000                       
cross_topic_rate_t1_bin   ->        topic_growth_bin           0.4898           0.0000                       
    connectivity_t1_bin   ->        topic_growth_bin           0.5008           0.0000                       
      modularity_t1_bin   ->        topic_growth_bin           0.5210           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1220           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0880           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7052           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8217           0.0000 possible size confound
               year_bin   ->        topic_growth_bin           0.9425           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 39: sensitivity_outcome:topic_growth / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 5500.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 9.850632174384812, 'likelihood': 9.094988296954046, 'sparsity': 16.623263623100215, 'dag': 0.08463572099375227}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `topic_growth_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           5.9268           0.0230                       
    connectivity_t1_bin   --       modularity_t1_bin           0.0222           6.2158 possible size confound
    connectivity_t1_bin   --        topic_growth_bin           0.6741           0.0670                       
    connectivity_t1_bin   --      topic_share_t1_bin           2.6092           0.0204                       
    connectivity_t1_bin   --                year_bin           0.0198           3.1939                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           0.0244           2.6119 possible size confound
cross_topic_rate_t1_bin   --        topic_growth_bin           1.2799           0.0434                       
cross_topic_rate_t1_bin   --      topic_share_t1_bin           6.2388           0.0197                       
cross_topic_rate_t1_bin   --                year_bin           0.0290           1.8056                       
      modularity_t1_bin   --        topic_growth_bin           0.4842           0.1219 possible size confound
      modularity_t1_bin   --      topic_share_t1_bin           1.6188           0.0299 possible size confound
      modularity_t1_bin   --                year_bin           0.0218           7.4094 possible size confound
       topic_growth_bin   --      topic_share_t1_bin           0.0860           2.2312                       
       topic_growth_bin   --                year_bin           0.1986           0.8843                       
     topic_share_t1_bin   --                year_bin           0.0426           1.8688                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'modularity_t1_bin', 'topic_growth_bin', 'topic_share_t1_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'topic_growth_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t1_bin'], ['cross_topic_rate_t1_bin', 'topic_growth_bin'], ['connectivity_t1_bin', 'topic_share_t1_bin'], ['connectivity_t1_bin', 'cross_topic_rate_t1_bin'], ['connectivity_t1_bin', 'topic_growth_bin'], ['modularity_t1_bin', 'topic_share_t1_bin'], ['modularity_t1_bin', 'cross_topic_rate_t1_bin'], ['modularity_t1_bin', 'connectivity_t1_bin'], ['modularity_t1_bin', 'topic_growth_bin'], ['year_bin', 'topic_share_t1_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['year_bin', 'topic_growth_bin'], ['topic_growth_bin', 'modularity_t1_bin'], ['topic_growth_bin', 'year_bin']]`.

### Setting 40: sensitivity_outcome:hit_rate_2yr / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 3000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.716011445457354, 'likelihood': 4.636000101165956, 'sparsity': 4.000567214569897, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `hit_rate_2yr`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->        hit_rate_2yr           0.4091           0.0000                       
cross_topic_rate_t1   ->        hit_rate_2yr           0.1030           0.0000                       
connectivity_t1_log   ->        hit_rate_2yr           0.8125           0.0000                       
      modularity_t1   ->        hit_rate_2yr           0.2432           0.0000 possible size confound
               year   ->      topic_share_t1           0.4509           0.0000                       
               year   -> cross_topic_rate_t1           0.4273           0.0000                       
               year   -> connectivity_t1_log           0.6618           0.0000                       
               year   ->       modularity_t1           0.2279           0.0000 possible size confound
               year   ->        hit_rate_2yr           0.6651           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 41: sensitivity_outcome:hit_rate_2yr / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.282799943365373, 'likelihood': 4.116717755976666, 'sparsity': 7.419004414939383, 'dag': 0.0035404198179840307}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `hit_rate_2yr`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.4996           0.0253 possible size confound
     topic_share_t1   ->        hit_rate_2yr           0.4683           0.0116                       
connectivity_t1_log   -> cross_topic_rate_t1           0.3460           0.0090                       
connectivity_t1_log   ->       modularity_t1           0.7587           0.0132 possible size confound
connectivity_t1_log   ->        hit_rate_2yr           0.9608           0.0055                       
      modularity_t1   ->        hit_rate_2yr           0.3450           0.0500 possible size confound
               year   -> cross_topic_rate_t1           0.6450           0.0249                       
               year   -> connectivity_t1_log           0.6416           0.0510                       
               year   ->       modularity_t1           0.9906           0.0046 possible size confound
               year   ->        hit_rate_2yr           0.8648           0.0010                       
       hit_rate_2yr   -> cross_topic_rate_t1           0.1212           0.0003                       
     topic_share_t1   --                year           0.1285           0.2999                       
```

Cyclic components: `[['topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'year'], ['year', 'topic_share_t1']]`.

### Setting 42: sensitivity_outcome:hit_rate_2yr / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 4000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.41161015438521, 'likelihood': 11.343317696081463, 'sparsity': 3.414622915187296, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `hit_rate_2yr_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->        hit_rate_2yr_bin           0.6657           0.0000                       
cross_topic_rate_t1_bin   ->        hit_rate_2yr_bin           0.7544           0.0000                       
    connectivity_t1_bin   ->        hit_rate_2yr_bin           1.1847           0.0000                       
      modularity_t1_bin   ->        hit_rate_2yr_bin           0.3853           0.0000 possible size confound
               year_bin   ->      topic_share_t1_bin           1.1223           0.0000                       
               year_bin   -> cross_topic_rate_t1_bin           1.0883           0.0000                       
               year_bin   ->     connectivity_t1_bin           1.7055           0.0000                       
               year_bin   ->       modularity_t1_bin           0.8219           0.0000 possible size confound
               year_bin   ->        hit_rate_2yr_bin           0.7660           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 43: sensitivity_outcome:hit_rate_2yr / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8400.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 9.838156509403746, 'likelihood': 9.074941339459418, 'sparsity': 17.03847691834588, 'dag': 0.08448912631548211}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `year_bin`, `hit_rate_2yr_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           0.0242           2.6440                       
    connectivity_t1_bin   --        hit_rate_2yr_bin           0.0356           1.3597                       
    connectivity_t1_bin   --       modularity_t1_bin           0.0215           6.6658 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           4.6475           0.0264                       
    connectivity_t1_bin   --                year_bin           0.0647           1.8782                       
cross_topic_rate_t1_bin   --        hit_rate_2yr_bin           0.0250           6.1289                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           5.5744           0.0242 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           1.4496           0.0400                       
cross_topic_rate_t1_bin   --                year_bin           0.0251           2.6079                       
       hit_rate_2yr_bin   --       modularity_t1_bin           2.4759           0.0265 possible size confound
       hit_rate_2yr_bin   --      topic_share_t1_bin           0.6963           0.0713                       
       hit_rate_2yr_bin   --                year_bin           0.0245           5.9583                       
      modularity_t1_bin   --      topic_share_t1_bin           2.2970           0.0267 possible size confound
      modularity_t1_bin   --                year_bin           0.0399           1.2069 possible size confound
     topic_share_t1_bin   --                year_bin           0.1434           2.0190                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'hit_rate_2yr_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'year_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'year_bin'], ['cross_topic_rate_t1_bin', 'topic_share_t1_bin'], ['cross_topic_rate_t1_bin', 'connectivity_t1_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'topic_share_t1_bin'], ['modularity_t1_bin', 'topic_share_t1_bin'], ['modularity_t1_bin', 'connectivity_t1_bin'], ['year_bin', 'topic_share_t1_bin'], ['year_bin', 'cross_topic_rate_t1_bin'], ['year_bin', 'connectivity_t1_bin'], ['year_bin', 'modularity_t1_bin'], ['year_bin', 'hit_rate_2yr_bin'], ['hit_rate_2yr_bin', 'topic_share_t1_bin'], ['hit_rate_2yr_bin', 'cross_topic_rate_t1_bin'], ['hit_rate_2yr_bin', 'connectivity_t1_bin'], ['hit_rate_2yr_bin', 'modularity_t1_bin']]`.

### Setting 44: sensitivity_no_year / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.876161612360404, 'likelihood': 4.844597174359463, 'sparsity': 1.5782219000470166, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge               b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->   topic_share_t           0.8815           0.0000                       
cross_topic_rate_t1   -> log1p_median_c2           0.2983           0.0000                       
      modularity_t1   -> log1p_median_c2           0.2128           0.0000 possible size confound
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 45: sensitivity_no_year / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 4.574184723837057, 'likelihood': 4.429716282335372, 'sparsity': 5.50802325855563, 'dag': 0.006861595266114406}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       modularity_t1           0.5548           0.0084 possible size confound
     topic_share_t1   ->       topic_share_t           0.8426           0.0248                       
     topic_share_t1   ->     log1p_median_c2           0.7976           0.0005                       
      modularity_t1   -> connectivity_t1_log           0.1584           0.0449 possible size confound
cross_topic_rate_t1   --     log1p_median_c2           0.0431           0.2841                       
cross_topic_rate_t1   --       modularity_t1           0.0423           0.2054 possible size confound
cross_topic_rate_t1   --       topic_share_t           0.1689           0.2078                       
    log1p_median_c2   --       modularity_t1           0.2739           0.0065 possible size confound
    log1p_median_c2   --       topic_share_t           0.0399           0.9714                       
      modularity_t1   --       topic_share_t           0.1116           0.3347 possible size confound
```

Cyclic components: `[['cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'topic_share_t']]`. Converted orientations: `[['cross_topic_rate_t1', 'topic_share_t'], ['modularity_t1', 'cross_topic_rate_t1'], ['modularity_t1', 'topic_share_t'], ['topic_share_t', 'cross_topic_rate_t1'], ['topic_share_t', 'modularity_t1'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'cross_topic_rate_t1'], ['log1p_median_c2', 'modularity_t1']]`.

### Setting 46: sensitivity_no_year / discretized / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5200.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 11.389317846737903, 'likelihood': 11.335421870335045, 'sparsity': 2.6947988201428563, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1_bin   ->   topic_share_t_bin           2.1395           0.0000                       
     topic_share_t1_bin   -> log1p_median_c2_bin           0.5190           0.0000                       
cross_topic_rate_t1_bin   ->   topic_share_t_bin           0.5079           0.0000                       
cross_topic_rate_t1_bin   -> log1p_median_c2_bin           1.1461           0.0000                       
    connectivity_t1_bin   ->   topic_share_t_bin           0.3584           0.0000                       
    connectivity_t1_bin   -> log1p_median_c2_bin           1.2060           0.0000                       
      modularity_t1_bin   ->   topic_share_t_bin           0.3448           0.0000 possible size confound
      modularity_t1_bin   -> log1p_median_c2_bin           0.8616           0.0000 possible size confound
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 47: sensitivity_no_year / discretized / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 8100.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 9.71013159371301, 'likelihood': 8.975461516515, 'sparsity': 15.674935509770842, 'dag': 0.08423427340051859}`.

Nodes (including isolates): `topic_share_t1_bin`, `cross_topic_rate_t1_bin`, `connectivity_t1_bin`, `modularity_t1_bin`, `topic_share_t_bin`, `log1p_median_c2_bin`.

```
                      a edge                       b  strength_a_to_b  strength_b_to_a                   flag
    connectivity_t1_bin   -- cross_topic_rate_t1_bin           1.1636           0.0372                       
    connectivity_t1_bin   --     log1p_median_c2_bin           2.6076           0.0254                       
    connectivity_t1_bin   --       modularity_t1_bin           0.6029           0.0959 possible size confound
    connectivity_t1_bin   --      topic_share_t1_bin           0.0225           6.7036                       
    connectivity_t1_bin   --       topic_share_t_bin           6.4025           0.0219                       
cross_topic_rate_t1_bin   --     log1p_median_c2_bin           0.0262           5.8087                       
cross_topic_rate_t1_bin   --       modularity_t1_bin           3.4765           0.0494 possible size confound
cross_topic_rate_t1_bin   --      topic_share_t1_bin           0.0582           0.7889                       
cross_topic_rate_t1_bin   --       topic_share_t_bin           0.0263           2.4022                       
    log1p_median_c2_bin   --       modularity_t1_bin           1.6614           0.0389 possible size confound
    log1p_median_c2_bin   --      topic_share_t1_bin           0.0327           1.2102                       
    log1p_median_c2_bin   --       topic_share_t_bin           0.0239           5.4128                       
      modularity_t1_bin   --      topic_share_t1_bin           0.1720           0.5668 possible size confound
      modularity_t1_bin   --       topic_share_t_bin           0.0554           0.7453 possible size confound
     topic_share_t1_bin   --       topic_share_t_bin           3.4257           0.0216                       
```

Cyclic components: `[['connectivity_t1_bin', 'cross_topic_rate_t1_bin', 'log1p_median_c2_bin', 'modularity_t1_bin', 'topic_share_t1_bin', 'topic_share_t_bin']]`. Converted orientations: `[['topic_share_t1_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t1_bin', 'connectivity_t1_bin'], ['topic_share_t1_bin', 'modularity_t1_bin'], ['topic_share_t1_bin', 'topic_share_t_bin'], ['topic_share_t1_bin', 'log1p_median_c2_bin'], ['cross_topic_rate_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'cross_topic_rate_t1_bin'], ['connectivity_t1_bin', 'modularity_t1_bin'], ['connectivity_t1_bin', 'topic_share_t_bin'], ['connectivity_t1_bin', 'log1p_median_c2_bin'], ['modularity_t1_bin', 'topic_share_t1_bin'], ['topic_share_t_bin', 'cross_topic_rate_t1_bin'], ['topic_share_t_bin', 'modularity_t1_bin'], ['topic_share_t_bin', 'log1p_median_c2_bin'], ['log1p_median_c2_bin', 'cross_topic_rate_t1_bin'], ['log1p_median_c2_bin', 'modularity_t1_bin']]`.

### Setting 48: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.05 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5200.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.1936749033810905, 'likelihood': 6.110560709157254, 'sparsity': 8.311419422383608, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7861           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.1946           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1494           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8799           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.4184           0.0000 possible size confound
               year   ->      topic_share_t1           0.9397           0.0000                       
               year   -> cross_topic_rate_t1           0.4129           0.0000                       
               year   -> connectivity_t1_log           0.6264           0.0000                       
               year   ->     n_papers_t1_log           0.5092           0.0000                       
               year   ->       topic_share_t           0.2576           0.0000                       
               year   ->     log1p_median_c2           1.1188           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.9301           0.0000                       
    n_papers_t1_log   -> connectivity_t1_log           0.0878           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5419           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3179           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 49: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.1 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5200.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.1936749033810905, 'likelihood': 6.110560709157254, 'sparsity': 8.311419422383608, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7861           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.1946           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1494           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8799           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.4184           0.0000 possible size confound
               year   ->      topic_share_t1           0.9397           0.0000                       
               year   -> cross_topic_rate_t1           0.4129           0.0000                       
               year   -> connectivity_t1_log           0.6264           0.0000                       
               year   ->     n_papers_t1_log           0.5092           0.0000                       
               year   ->       topic_share_t           0.2576           0.0000                       
               year   ->     log1p_median_c2           1.1188           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.9301           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5419           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3179           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 50: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.2 / constrained=True

Status: **converged**. Rows: 127. Iterations: 5200.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.1936749033810905, 'likelihood': 6.110560709157254, 'sparsity': 8.311419422383608, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7861           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8799           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.4184           0.0000 possible size confound
               year   ->      topic_share_t1           0.9397           0.0000                       
               year   -> cross_topic_rate_t1           0.4129           0.0000                       
               year   -> connectivity_t1_log           0.6264           0.0000                       
               year   ->     n_papers_t1_log           0.5092           0.0000                       
               year   ->       topic_share_t           0.2576           0.0000                       
               year   ->     log1p_median_c2           1.1188           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.9301           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5419           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3179           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 51: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.05 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.274355643016878, 'likelihood': 6.117305710029538, 'sparsity': 7.852496649366973, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8047           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.1578           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1211           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8056           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.3632           0.0000 possible size confound
               year   ->      topic_share_t1           0.9278           0.0000                       
               year   -> cross_topic_rate_t1           0.4091           0.0000                       
               year   -> connectivity_t1_log           0.6226           0.0000                       
               year   ->     n_papers_t1_log           0.5035           0.0000                       
               year   ->       topic_share_t           0.2047           0.0000                       
               year   ->     log1p_median_c2           1.0270           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.9182           0.0000                       
    n_papers_t1_log   -> connectivity_t1_log           0.0839           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5300           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3102           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 52: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.1 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.274355643016878, 'likelihood': 6.117305710029538, 'sparsity': 7.852496649366973, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8047           0.0000                       
     topic_share_t1   ->     log1p_median_c2           0.1578           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.1211           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8056           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.3632           0.0000 possible size confound
               year   ->      topic_share_t1           0.9278           0.0000                       
               year   -> cross_topic_rate_t1           0.4091           0.0000                       
               year   -> connectivity_t1_log           0.6226           0.0000                       
               year   ->     n_papers_t1_log           0.5035           0.0000                       
               year   ->       topic_share_t           0.2047           0.0000                       
               year   ->     log1p_median_c2           1.0270           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.9182           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5300           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3102           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 53: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.2 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.274355643016878, 'likelihood': 6.117305710029538, 'sparsity': 7.852496649366973, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.8047           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.8056           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.3632           0.0000 possible size confound
               year   ->      topic_share_t1           0.9278           0.0000                       
               year   -> cross_topic_rate_t1           0.4091           0.0000                       
               year   -> connectivity_t1_log           0.6226           0.0000                       
               year   ->     n_papers_t1_log           0.5035           0.0000                       
               year   ->       topic_share_t           0.2047           0.0000                       
               year   ->     log1p_median_c2           1.0270           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.9182           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5300           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3102           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 54: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.05 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.494699055544211, 'likelihood': 6.152241169444458, 'sparsity': 6.849157721995061, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7984           0.0000                       
connectivity_t1_log   ->       topic_share_t           0.0665           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.6249           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.2151           0.0000 possible size confound
               year   ->      topic_share_t1           0.8916           0.0000                       
               year   -> cross_topic_rate_t1           0.3975           0.0000                       
               year   -> connectivity_t1_log           0.6110           0.0000                       
               year   ->     n_papers_t1_log           0.4859           0.0000                       
               year   ->       topic_share_t           0.1524           0.0000                       
               year   ->     log1p_median_c2           0.7661           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.8820           0.0000                       
    n_papers_t1_log   -> connectivity_t1_log           0.0723           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5033           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3402           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 55: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.1 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.494699055544211, 'likelihood': 6.152241169444458, 'sparsity': 6.849157721995061, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7984           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.6249           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.2151           0.0000 possible size confound
               year   ->      topic_share_t1           0.8916           0.0000                       
               year   -> cross_topic_rate_t1           0.3975           0.0000                       
               year   -> connectivity_t1_log           0.6110           0.0000                       
               year   ->     n_papers_t1_log           0.4859           0.0000                       
               year   ->       topic_share_t           0.1524           0.0000                       
               year   ->     log1p_median_c2           0.7661           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.8820           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5033           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3402           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 56: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.2 / constrained=True

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 6.494699055544211, 'likelihood': 6.152241169444458, 'sparsity': 6.849157721995061, 'dag': 0.0}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->       topic_share_t           0.7984           0.0000                       
connectivity_t1_log   ->     log1p_median_c2           0.6249           0.0000                       
      modularity_t1   ->     log1p_median_c2           0.2151           0.0000 possible size confound
               year   ->      topic_share_t1           0.8916           0.0000                       
               year   -> cross_topic_rate_t1           0.3975           0.0000                       
               year   -> connectivity_t1_log           0.6110           0.0000                       
               year   ->     n_papers_t1_log           0.4859           0.0000                       
               year   ->     log1p_median_c2           0.7661           0.0000                       
    n_papers_t1_log   ->      topic_share_t1           0.8820           0.0000                       
    n_papers_t1_log   ->       modularity_t1           0.5033           0.0000 possible size confound
    n_papers_t1_log   ->     log1p_median_c2           0.3402           0.0000                       
```

Cyclic components: `[]`. Converted orientations: `[]`.

### Setting 57: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.05 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4900.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.4339235727312065, 'likelihood': 5.164086095535109, 'sparsity': 14.51709769237432, 'dag': 0.02493330005447092}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.6452           0.0068                       
connectivity_t1_log   --     log1p_median_c2           0.7928           0.0194                       
connectivity_t1_log   --       modularity_t1           0.8114           0.0372 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0224           0.5558                       
connectivity_t1_log   --       topic_share_t           0.0669           0.1239                       
connectivity_t1_log   --      topic_share_t1           0.0294           0.5376                       
connectivity_t1_log   --                year           0.2822           0.0848                       
cross_topic_rate_t1   --       modularity_t1           0.0001           0.2916 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0077           0.9617                       
cross_topic_rate_t1   --       topic_share_t           0.0625           0.0104                       
cross_topic_rate_t1   --      topic_share_t1           0.0418           0.7477                       
cross_topic_rate_t1   --                year           0.1006           0.0630                       
    log1p_median_c2   --       modularity_t1           0.0202           0.3844 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.0683           0.1129                       
    log1p_median_c2   --       topic_share_t           0.0256           0.4021                       
    log1p_median_c2   --      topic_share_t1           0.0486           0.6794                       
    log1p_median_c2   --                year           0.0022           1.1625                       
      modularity_t1   --     n_papers_t1_log           0.1303           0.1382 possible size confound
      modularity_t1   --       topic_share_t           0.1632           0.1052 possible size confound
      modularity_t1   --      topic_share_t1           0.0814           0.3645 possible size confound
      modularity_t1   --                year           0.0025           0.9169 possible size confound
    n_papers_t1_log   --       topic_share_t           0.7485           0.0181                       
    n_papers_t1_log   --      topic_share_t1           0.2635           0.1435                       
    n_papers_t1_log   --                year           0.0999           0.3866                       
      topic_share_t   --      topic_share_t1           0.6271           0.0222                       
      topic_share_t   --                year           0.0130           0.8304                       
     topic_share_t1   --                year           0.1000           0.1350                       
```

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'cross_topic_rate_t1'], ['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'modularity_t1'], ['topic_share_t1', 'year'], ['topic_share_t1', 'n_papers_t1_log'], ['topic_share_t1', 'log1p_median_c2'], ['cross_topic_rate_t1', 'year'], ['cross_topic_rate_t1', 'topic_share_t'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'year'], ['connectivity_t1_log', 'topic_share_t'], ['connectivity_t1_log', 'log1p_median_c2'], ['modularity_t1', 'topic_share_t1'], ['modularity_t1', 'cross_topic_rate_t1'], ['modularity_t1', 'n_papers_t1_log'], ['modularity_t1', 'topic_share_t'], ['modularity_t1', 'log1p_median_c2'], ['year', 'topic_share_t1'], ['year', 'cross_topic_rate_t1'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['year', 'log1p_median_c2'], ['n_papers_t1_log', 'topic_share_t1'], ['n_papers_t1_log', 'cross_topic_rate_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'modularity_t1'], ['n_papers_t1_log', 'year'], ['n_papers_t1_log', 'topic_share_t'], ['n_papers_t1_log', 'log1p_median_c2'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'modularity_t1'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'n_papers_t1_log']]`.

### Setting 58: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.1 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4900.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.4339235727312065, 'likelihood': 5.164086095535109, 'sparsity': 14.51709769237432, 'dag': 0.02493330005447092}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   ->     log1p_median_c2           0.6794           0.0486                       
connectivity_t1_log   ->     log1p_median_c2           0.7928           0.0194                       
      modularity_t1   ->     log1p_median_c2           0.3844           0.0202 possible size confound
               year   ->     log1p_median_c2           1.1625           0.0022                       
    n_papers_t1_log   ->     log1p_median_c2           0.1129           0.0683                       
      topic_share_t   ->     log1p_median_c2           0.4021           0.0256                       
connectivity_t1_log   -- cross_topic_rate_t1           0.6452           0.0068                       
connectivity_t1_log   --       modularity_t1           0.8114           0.0372 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0224           0.5558                       
connectivity_t1_log   --       topic_share_t           0.0669           0.1239                       
connectivity_t1_log   --      topic_share_t1           0.0294           0.5376                       
connectivity_t1_log   --                year           0.2822           0.0848                       
cross_topic_rate_t1   --       modularity_t1           0.0001           0.2916 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0077           0.9617                       
cross_topic_rate_t1   --      topic_share_t1           0.0418           0.7477                       
cross_topic_rate_t1   --                year           0.1006           0.0630                       
      modularity_t1   --     n_papers_t1_log           0.1303           0.1382 possible size confound
      modularity_t1   --       topic_share_t           0.1632           0.1052 possible size confound
      modularity_t1   --      topic_share_t1           0.0814           0.3645 possible size confound
      modularity_t1   --                year           0.0025           0.9169 possible size confound
    n_papers_t1_log   --       topic_share_t           0.7485           0.0181                       
    n_papers_t1_log   --      topic_share_t1           0.2635           0.1435                       
    n_papers_t1_log   --                year           0.0999           0.3866                       
      topic_share_t   --      topic_share_t1           0.6271           0.0222                       
      topic_share_t   --                year           0.0130           0.8304                       
     topic_share_t1   --                year           0.1000           0.1350                       
```

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'modularity_t1', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'cross_topic_rate_t1'], ['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'modularity_t1'], ['topic_share_t1', 'n_papers_t1_log'], ['cross_topic_rate_t1', 'year'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'year'], ['modularity_t1', 'cross_topic_rate_t1'], ['modularity_t1', 'n_papers_t1_log'], ['modularity_t1', 'topic_share_t'], ['year', 'topic_share_t1'], ['year', 'modularity_t1'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['n_papers_t1_log', 'topic_share_t1'], ['n_papers_t1_log', 'cross_topic_rate_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'modularity_t1'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'modularity_t1']]`.

### Setting 59: sensitivity_size_control / continuous / lambda1=0.01 / threshold=0.2 / constrained=False

Status: **converged**. Rows: 127. Iterations: 4900.

Optimizer: `{'lambda1': 0.01, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.4339235727312065, 'likelihood': 5.164086095535109, 'sparsity': 14.51709769237432, 'dag': 0.02493330005447092}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> cross_topic_rate_t1           0.7477           0.0418                       
     topic_share_t1   ->       modularity_t1           0.3645           0.0814 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.6794           0.0486                       
connectivity_t1_log   -> cross_topic_rate_t1           0.6452           0.0068                       
connectivity_t1_log   ->       modularity_t1           0.8114           0.0372 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7928           0.0194                       
      modularity_t1   -> cross_topic_rate_t1           0.2916           0.0001 possible size confound
      modularity_t1   ->     log1p_median_c2           0.3844           0.0202 possible size confound
               year   ->       modularity_t1           0.9169           0.0025 possible size confound
               year   ->     log1p_median_c2           1.1625           0.0022                       
    n_papers_t1_log   -> cross_topic_rate_t1           0.9617           0.0077                       
      topic_share_t   ->     log1p_median_c2           0.4021           0.0256                       
connectivity_t1_log   --     n_papers_t1_log           0.0224           0.5558                       
connectivity_t1_log   --      topic_share_t1           0.0294           0.5376                       
connectivity_t1_log   --                year           0.2822           0.0848                       
    n_papers_t1_log   --       topic_share_t           0.7485           0.0181                       
    n_papers_t1_log   --      topic_share_t1           0.2635           0.1435                       
    n_papers_t1_log   --                year           0.0999           0.3866                       
      topic_share_t   --      topic_share_t1           0.6271           0.0222                       
      topic_share_t   --                year           0.0130           0.8304                       
```

Cyclic components: `[['connectivity_t1_log', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'connectivity_t1_log'], ['connectivity_t1_log', 'year'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['n_papers_t1_log', 'topic_share_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1']]`.

### Setting 60: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.571654186885919, 'likelihood': 5.173167090548626, 'sparsity': 13.451406471908705, 'dag': 0.025891793379823724}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.5909           0.0099                       
connectivity_t1_log   --     log1p_median_c2           0.7209           0.0170                       
connectivity_t1_log   --       modularity_t1           0.7833           0.0396 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0047           0.5339                       
connectivity_t1_log   --       topic_share_t           0.0177           0.2873                       
connectivity_t1_log   --      topic_share_t1           0.0154           0.6287                       
connectivity_t1_log   --                year           0.2499           0.1403                       
cross_topic_rate_t1   --       modularity_t1           0.0002           0.2394 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0289           0.8676                       
cross_topic_rate_t1   --      topic_share_t1           0.0097           0.6742                       
cross_topic_rate_t1   --                year           0.1003           0.0796                       
    log1p_median_c2   --       modularity_t1           0.0001           0.3047 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.1348           0.0001                       
    log1p_median_c2   --       topic_share_t           0.0036           0.4104                       
    log1p_median_c2   --      topic_share_t1           0.0242           0.7240                       
    log1p_median_c2   --                year           0.0020           1.1553                       
      modularity_t1   --     n_papers_t1_log           0.1797           0.1048 possible size confound
      modularity_t1   --      topic_share_t1           0.0296           0.4448 possible size confound
      modularity_t1   --                year           0.0003           0.9134 possible size confound
    n_papers_t1_log   --       topic_share_t           0.4461           0.0003                       
    n_papers_t1_log   --      topic_share_t1           0.0252           0.4376                       
    n_papers_t1_log   --                year           0.0851           0.4732                       
      topic_share_t   --      topic_share_t1           0.5749           0.0391                       
      topic_share_t   --                year           0.0224           0.6248                       
     topic_share_t1   --                year           0.1885           0.0286                       
```

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'cross_topic_rate_t1'], ['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'modularity_t1'], ['topic_share_t1', 'year'], ['topic_share_t1', 'n_papers_t1_log'], ['topic_share_t1', 'log1p_median_c2'], ['cross_topic_rate_t1', 'year'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'year'], ['connectivity_t1_log', 'log1p_median_c2'], ['modularity_t1', 'cross_topic_rate_t1'], ['modularity_t1', 'n_papers_t1_log'], ['modularity_t1', 'log1p_median_c2'], ['year', 'cross_topic_rate_t1'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['year', 'log1p_median_c2'], ['n_papers_t1_log', 'cross_topic_rate_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'modularity_t1'], ['n_papers_t1_log', 'year'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'n_papers_t1_log']]`.

### Setting 61: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.571654186885919, 'likelihood': 5.173167090548626, 'sparsity': 13.451406471908705, 'dag': 0.025891793379823724}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
connectivity_t1_log   -- cross_topic_rate_t1           0.5909           0.0099                       
connectivity_t1_log   --     log1p_median_c2           0.7209           0.0170                       
connectivity_t1_log   --       modularity_t1           0.7833           0.0396 possible size confound
connectivity_t1_log   --     n_papers_t1_log           0.0047           0.5339                       
connectivity_t1_log   --       topic_share_t           0.0177           0.2873                       
connectivity_t1_log   --      topic_share_t1           0.0154           0.6287                       
connectivity_t1_log   --                year           0.2499           0.1403                       
cross_topic_rate_t1   --       modularity_t1           0.0002           0.2394 possible size confound
cross_topic_rate_t1   --     n_papers_t1_log           0.0289           0.8676                       
cross_topic_rate_t1   --      topic_share_t1           0.0097           0.6742                       
cross_topic_rate_t1   --                year           0.1003           0.0796                       
    log1p_median_c2   --       modularity_t1           0.0001           0.3047 possible size confound
    log1p_median_c2   --     n_papers_t1_log           0.1348           0.0001                       
    log1p_median_c2   --       topic_share_t           0.0036           0.4104                       
    log1p_median_c2   --      topic_share_t1           0.0242           0.7240                       
    log1p_median_c2   --                year           0.0020           1.1553                       
      modularity_t1   --     n_papers_t1_log           0.1797           0.1048 possible size confound
      modularity_t1   --      topic_share_t1           0.0296           0.4448 possible size confound
      modularity_t1   --                year           0.0003           0.9134 possible size confound
    n_papers_t1_log   --       topic_share_t           0.4461           0.0003                       
    n_papers_t1_log   --      topic_share_t1           0.0252           0.4376                       
    n_papers_t1_log   --                year           0.0851           0.4732                       
      topic_share_t   --      topic_share_t1           0.5749           0.0391                       
      topic_share_t   --                year           0.0224           0.6248                       
     topic_share_t1   --                year           0.1885           0.0286                       
```

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'cross_topic_rate_t1'], ['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'modularity_t1'], ['topic_share_t1', 'year'], ['topic_share_t1', 'n_papers_t1_log'], ['topic_share_t1', 'log1p_median_c2'], ['cross_topic_rate_t1', 'year'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'year'], ['connectivity_t1_log', 'log1p_median_c2'], ['modularity_t1', 'cross_topic_rate_t1'], ['modularity_t1', 'n_papers_t1_log'], ['modularity_t1', 'log1p_median_c2'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['year', 'log1p_median_c2'], ['n_papers_t1_log', 'cross_topic_rate_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'modularity_t1'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'n_papers_t1_log']]`.

### Setting 62: sensitivity_size_control / continuous / lambda1=0.02 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.02, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.571654186885919, 'likelihood': 5.173167090548626, 'sparsity': 13.451406471908705, 'dag': 0.025891793379823724}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

Exploratory graph only; excluded from recurrence and comparisons.

```
                  a edge                   b  strength_a_to_b  strength_b_to_a                   flag
     topic_share_t1   -> cross_topic_rate_t1           0.6742           0.0097                       
     topic_share_t1   ->       modularity_t1           0.4448           0.0296 possible size confound
     topic_share_t1   ->     log1p_median_c2           0.7240           0.0242                       
connectivity_t1_log   -> cross_topic_rate_t1           0.5909           0.0099                       
connectivity_t1_log   ->       modularity_t1           0.7833           0.0396 possible size confound
connectivity_t1_log   ->     log1p_median_c2           0.7209           0.0170                       
      modularity_t1   -> cross_topic_rate_t1           0.2394           0.0002 possible size confound
      modularity_t1   ->     log1p_median_c2           0.3047           0.0001 possible size confound
               year   ->       modularity_t1           0.9134           0.0003 possible size confound
               year   ->     log1p_median_c2           1.1553           0.0020                       
    n_papers_t1_log   -> cross_topic_rate_t1           0.8676           0.0289                       
      topic_share_t   ->     log1p_median_c2           0.4104           0.0036                       
connectivity_t1_log   --     n_papers_t1_log           0.0047           0.5339                       
connectivity_t1_log   --       topic_share_t           0.0177           0.2873                       
connectivity_t1_log   --      topic_share_t1           0.0154           0.6287                       
connectivity_t1_log   --                year           0.2499           0.1403                       
    n_papers_t1_log   --       topic_share_t           0.4461           0.0003                       
    n_papers_t1_log   --      topic_share_t1           0.0252           0.4376                       
    n_papers_t1_log   --                year           0.0851           0.4732                       
      topic_share_t   --      topic_share_t1           0.5749           0.0391                       
      topic_share_t   --                year           0.0224           0.6248                       
```

Cyclic components: `[['connectivity_t1_log', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'n_papers_t1_log'], ['connectivity_t1_log', 'year'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'connectivity_t1_log']]`.

### Setting 63: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.05 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.9155702491484305, 'likelihood': 5.264145930994893, 'sparsity': 11.180368527978116, 'dag': 0.01848117835092644}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

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

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'cross_topic_rate_t1'], ['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'year'], ['topic_share_t1', 'n_papers_t1_log'], ['topic_share_t1', 'log1p_median_c2'], ['cross_topic_rate_t1', 'year'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'year'], ['connectivity_t1_log', 'topic_share_t'], ['connectivity_t1_log', 'log1p_median_c2'], ['modularity_t1', 'log1p_median_c2'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['year', 'log1p_median_c2'], ['n_papers_t1_log', 'cross_topic_rate_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'modularity_t1'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'n_papers_t1_log']]`.

### Setting 64: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.1 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.9155702491484305, 'likelihood': 5.264145930994893, 'sparsity': 11.180368527978116, 'dag': 0.01848117835092644}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

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

Cyclic components: `[['connectivity_t1_log', 'cross_topic_rate_t1', 'log1p_median_c2', 'modularity_t1', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'cross_topic_rate_t1'], ['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'year'], ['topic_share_t1', 'n_papers_t1_log'], ['topic_share_t1', 'log1p_median_c2'], ['cross_topic_rate_t1', 'year'], ['connectivity_t1_log', 'cross_topic_rate_t1'], ['connectivity_t1_log', 'modularity_t1'], ['connectivity_t1_log', 'year'], ['connectivity_t1_log', 'topic_share_t'], ['connectivity_t1_log', 'log1p_median_c2'], ['modularity_t1', 'log1p_median_c2'], ['year', 'connectivity_t1_log'], ['year', 'modularity_t1'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['year', 'log1p_median_c2'], ['n_papers_t1_log', 'cross_topic_rate_t1'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'modularity_t1'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1'], ['topic_share_t', 'log1p_median_c2'], ['log1p_median_c2', 'n_papers_t1_log']]`.

### Setting 65: sensitivity_size_control / continuous / lambda1=0.05 / threshold=0.2 / constrained=False

Status: **nonconverged**. Rows: 127. Iterations: 10000.

Optimizer: `{'lambda1': 0.05, 'lambda_dag': 5.0, 'learning_rate': 0.001, 'max_iter': 10000, 'tolerance': 1e-07, 'check_every': 100, 'patience': 5, 'seed': 0}`. Objective components: `{'total': 5.9155702491484305, 'likelihood': 5.264145930994893, 'sparsity': 11.180368527978116, 'dag': 0.01848117835092644}`.

Nodes (including isolates): `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1_log`, `modularity_t1`, `year`, `n_papers_t1_log`, `topic_share_t`, `log1p_median_c2`.

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

Cyclic components: `[['connectivity_t1_log', 'n_papers_t1_log', 'topic_share_t', 'topic_share_t1', 'year']]`. Converted orientations: `[['topic_share_t1', 'connectivity_t1_log'], ['topic_share_t1', 'n_papers_t1_log'], ['connectivity_t1_log', 'year'], ['year', 'n_papers_t1_log'], ['year', 'topic_share_t'], ['n_papers_t1_log', 'connectivity_t1_log'], ['n_papers_t1_log', 'topic_share_t'], ['topic_share_t', 'topic_share_t1']]`.

## Constrained main-model recurrence

Pairs use alphabetical base-variable order. Rates use all eligible fits, including empty graphs. `a_to_b_rate`, `b_to_a_rate`, and `undirected_rate` sum to `adjacency_rate`; conditional rates divide by adjacent fits only. Orientation frequency and consistency of a particular direction are distinct.

Thresholds from the same fitted model are correlated settings, not independent replications.

### continuous: 3 eligible settings

```
                  a               b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1 log1p_median_c2           3        3          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1            year           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
cross_topic_rate_t1            year           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2   modularity_t1           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2  topic_share_t1           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2            year           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      modularity_t1            year           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t  topic_share_t1           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t            year           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
     topic_share_t1            year           3        3          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    connectivity_t1   topic_share_t           2        3          0.6667       0.6667       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

### discretized: 9 eligible settings

```
                  a               b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1 log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1   topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1            year           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
cross_topic_rate_t1 log1p_median_c2           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1   topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1            year           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2   modularity_t1           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2  topic_share_t1           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2            year           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      modularity_t1   topic_share_t           9        9          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1            year           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t  topic_share_t1           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t            year           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
     topic_share_t1            year           9        9          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
```

### combined: 12 eligible settings

```
                  a               b  n_adjacent  n_total  adjacency_rate  a_to_b_rate  b_to_a_rate  undirected_rate  orientation_rate_given_adjacent  a_to_b_given_adjacent  b_to_a_given_adjacent  undirected_given_adjacent
    connectivity_t1 log1p_median_c2          12       12          1.0000       1.0000       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
    connectivity_t1            year          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
cross_topic_rate_t1            year          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2   modularity_t1          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2  topic_share_t1          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    log1p_median_c2            year          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      modularity_t1            year          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t  topic_share_t1          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
      topic_share_t            year          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
     topic_share_t1            year          12       12          1.0000       0.0000       1.0000           0.0000                           1.0000                 0.0000                 1.0000                     0.0000
    connectivity_t1   topic_share_t          11       12          0.9167       0.9167       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1 log1p_median_c2           9       12          0.7500       0.7500       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
cross_topic_rate_t1   topic_share_t           9       12          0.7500       0.7500       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
      modularity_t1   topic_share_t           9       12          0.7500       0.7500       0.0000           0.0000                           1.0000                 1.0000                 0.0000                     0.0000
```

## Comparison with PC

reports\pc_runs\pc_runs_v5.json

Match representation, model group, constraint mode, row count, and normalized node set. Legacy PC files omit input hashes and node lists; nodes are reconstructed from their group, so exact historical input identity cannot be independently verified. Other PC endpoint types count toward adjacency only. Two empty skeletons have Jaccard=1.

```
 golem_setting pc_test  pc_alpha  shared_adjacencies  golem_only  pc_only  jaccard  direction_agreement  direction_reversals  shared_pc_undirected  shared_golem_undirected
             0 fisherz    0.0100                   5           6        0   0.4545                    5                    0                     0                        0
             0 fisherz    0.0500                   5           6        1   0.4167                    5                    0                     0                        0
             0 fisherz    0.1000                   6           5        1   0.5000                    6                    0                     0                        0
             0     kci    0.0100                   6           5        0   0.5455                    6                    0                     0                        0
             0     kci    0.0500                   6           5        0   0.5455                    6                    0                     0                        0
             0     kci    0.1000                   7           4        0   0.6364                    7                    0                     0                        0
             1 fisherz    0.0100                   5           6        0   0.4545                    5                    0                     0                        0
             1 fisherz    0.0500                   5           6        1   0.4167                    5                    0                     0                        0
             1 fisherz    0.1000                   6           5        1   0.5000                    6                    0                     0                        0
             1     kci    0.0100                   6           5        0   0.5455                    6                    0                     0                        0
             1     kci    0.0500                   6           5        0   0.5455                    6                    0                     0                        0
             1     kci    0.1000                   7           4        0   0.6364                    7                    0                     0                        0
             2 fisherz    0.0100                   5           5        0   0.5000                    5                    0                     0                        0
             2 fisherz    0.0500                   5           5        1   0.4545                    5                    0                     0                        0
             2 fisherz    0.1000                   6           4        1   0.5455                    6                    0                     0                        0
             2     kci    0.0100                   6           4        0   0.6000                    6                    0                     0                        0
             2     kci    0.0500                   6           4        0   0.6000                    6                    0                     0                        0
             2     kci    0.1000                   7           3        0   0.7000                    7                    0                     0                        0
            18   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            18   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            18   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            19   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            19   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            19   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            20   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            20   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            20   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            21   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            21   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            21   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            22   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            22   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            22   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            23   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            23   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            23   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            24   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            24   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            24   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            25   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            25   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            25   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            26   chisq    0.0100                   3          11        0   0.2143                    3                    0                     0                        0
            26   chisq    0.0500                   5           9        0   0.3571                    5                    0                     0                        0
            26   chisq    0.1000                   4          10        0   0.2857                    4                    0                     0                        0
            30   chisq    0.0100                   3          18        0   0.1429                    0                    0                     3                        3
            30   chisq    0.0500                   5          16        0   0.2381                    0                    0                     3                        5
            30   chisq    0.1000                   5          16        0   0.2381                    0                    0                     1                        5
            31   chisq    0.0100                   3          18        0   0.1429                    0                    0                     3                        3
            31   chisq    0.0500                   5          16        0   0.2381                    0                    0                     3                        5
            31   chisq    0.1000                   5          16        0   0.2381                    0                    0                     1                        5
            32   chisq    0.0100                   3          18        0   0.1429                    0                    0                     3                        0
            32   chisq    0.0500                   5          16        0   0.2381                    1                    1                     3                        0
            32   chisq    0.1000                   5          16        0   0.2381                    2                    2                     1                        0
            33   chisq    0.0100                   3          18        0   0.1429                    0                    0                     3                        3
            33   chisq    0.0500                   5          16        0   0.2381                    0                    0                     3                        5
            33   chisq    0.1000                   5          16        0   0.2381                    0                    0                     1                        5
            34   chisq    0.0100                   3          18        0   0.1429                    0                    0                     3                        3
            34   chisq    0.0500                   5          16        0   0.2381                    0                    0                     3                        5
            34   chisq    0.1000                   5          16        0   0.2381                    0                    0                     1                        5
            35   chisq    0.0100                   3          17        0   0.1500                    0                    0                     3                        3
            35   chisq    0.0500                   5          15        0   0.2500                    0                    0                     3                        5
            35   chisq    0.1000                   5          15        0   0.2500                    0                    0                     1                        5
            36 fisherz    0.0500                   3           4        1   0.3750                    3                    0                     0                        0
            38   chisq    0.0500                   3           6        0   0.3333                    3                    0                     0                        0
            39   chisq    0.0500                   4          11        0   0.2667                    0                    0                     0                        4
            40 fisherz    0.0500                   4           5        0   0.4444                    4                    0                     0                        0
            42   chisq    0.0500                   5           4        0   0.5556                    5                    0                     0                        0
            43   chisq    0.0500                   6           9        0   0.4000                    0                    0                     1                        6
            46   chisq    0.0500                   3           5        0   0.3750                    3                    0                     0                        0
            47   chisq    0.0500                   3          12        0   0.2000                    0                    0                     3                        3
            48 fisherz    0.0100                   4          11        0   0.2667                    4                    0                     0                        0
            48 fisherz    0.0500                   4          11        1   0.2500                    4                    0                     0                        0
            48 fisherz    0.1000                   5          10        1   0.3125                    5                    0                     0                        0
            49 fisherz    0.0100                   4          10        0   0.2857                    4                    0                     0                        0
            49 fisherz    0.0500                   4          10        1   0.2667                    4                    0                     0                        0
            49 fisherz    0.1000                   5           9        1   0.3333                    5                    0                     0                        0
            50 fisherz    0.0100                   4           8        0   0.3333                    4                    0                     0                        0
            50 fisherz    0.0500                   4           8        1   0.3077                    4                    0                     0                        0
            50 fisherz    0.1000                   5           7        1   0.3846                    5                    0                     0                        0
            57 fisherz    0.0100                   4          23        0   0.1481                    0                    0                     2                        4
            57 fisherz    0.0500                   5          22        1   0.1786                    0                    0                     3                        5
            57 fisherz    0.1000                   6          21        1   0.2143                    0                    0                     4                        6
            58 fisherz    0.0100                   4          22        0   0.1538                    0                    0                     2                        4
            58 fisherz    0.0500                   5          21        1   0.1852                    0                    0                     3                        5
            58 fisherz    0.1000                   6          20        1   0.2222                    0                    0                     4                        6
            59 fisherz    0.0100                   4          16        0   0.2000                    0                    0                     2                        4
            59 fisherz    0.0500                   4          16        2   0.1818                    0                    1                     2                        3
            59 fisherz    0.1000                   5          15        2   0.2273                    0                    1                     3                        4
```
