# PC Algorithm Settings Comparison -- Step 3 (v5)

PC run across a controlled grid, per the 2026-08-19 correction. **Main model**: predictors topic_share_t1, cross_topic_rate_t1, connectivity_t1_log, modularity_t1, year (continuous) / topic_share_t1_bin, cross_topic_rate_t1_bin, connectivity_t1_bin, modularity_t1_bin, year_bin (discretized), outcomes topic_share_t, log1p_median_c2 (continuous) / topic_share_t_bin, log1p_median_c2_bin (discretized) -- continuous data + Fisher-Z, discretized data + chi-square, continuous data + KCI (kernel-based, nonlinear-robust), alpha in {0.01, 0.05, 0.10}, with and without the Step 2/3 temporal + exogenous-year constraints. `bridge_concentration_t1` is dropped from the main model entirely (near-degenerate, Step 1 finding). **Sensitivity groups** (alpha=0.05 only): `sensitivity_outcome:<name>` swaps in `topic_growth` or `hit_rate_2yr` as the outcome instead of the main `['topic_share_t', 'log1p_median_c2']`; `sensitivity_no_year` reruns the main predictor/outcome set with the `year` node removed, to check whether year is actually absorbing any of the signal; `sensitivity_size_control` adds `n_papers_t1` (log-transformed, own tier below the regular predictors so it isn't blocked from `modularity_t1`'s conditioning set by forbid_within_tier) to check whether `modularity_t1`'s known size confound (r=0.48-0.51 with n_papers_t1 across v4/v5, stronger than the topic_share_t1 proxy) is driving any of its edges -- compare its edge list below against the main constrained run's.

## Settings grid

```
group                      repr         test      alpha  constr  directed  undirected  temporal_violations 
main                       continuous   fisherz   0.01   True    5         0           0                   
main                       continuous   fisherz   0.01   False   4         1           4                   
main                       continuous   fisherz   0.05   True    6         0           0                   
main                       continuous   fisherz   0.05   False   4         4           1                   
main                       continuous   fisherz   0.1    True    7         0           0                   
main                       continuous   fisherz   0.1    False   4         5           1                   
main                       discretized  chisq     0.01   True    3         0           0                   
main                       discretized  chisq     0.01   False   0         3           0                   
main                       discretized  chisq     0.05   True    5         0           0                   
main                       discretized  chisq     0.05   False   2         3           1                   
main                       discretized  chisq     0.1    True    4         0           0                   
main                       discretized  chisq     0.1    False   4         1           2                   
main                       continuous   kci       0.01   True    6         0           0                   
main                       continuous   kci       0.01   False   6         2           5                   
main                       continuous   kci       0.05   True    6         0           0                   
main                       continuous   kci       0.05   False   7         1           4                   
main                       continuous   kci       0.1    True    7         0           0                   
main                       continuous   kci       0.1    False   8         1           3                   
sensitivity_outcome:topic_growth continuous   fisherz   0.05   True    4         0           0                   
sensitivity_outcome:topic_growth discretized  chisq     0.05   True    3         0           0                   
sensitivity_outcome:topic_growth continuous   fisherz   0.05   False   4         2           0                   
sensitivity_outcome:topic_growth discretized  chisq     0.05   False   4         0           2                   
sensitivity_outcome:hit_rate_2yr continuous   fisherz   0.05   True    4         0           0                   
sensitivity_outcome:hit_rate_2yr discretized  chisq     0.05   True    5         0           0                   
sensitivity_outcome:hit_rate_2yr continuous   fisherz   0.05   False   4         1           1                   
sensitivity_outcome:hit_rate_2yr discretized  chisq     0.05   False   5         1           1                   
sensitivity_no_year        continuous   fisherz   0.05   True    3         0           0                   
sensitivity_no_year        discretized  chisq     0.05   True    3         0           0                   
sensitivity_no_year        continuous   fisherz   0.05   False   4         1           2                   
sensitivity_no_year        discretized  chisq     0.05   False   0         3           0                   
sensitivity_size_control   continuous   fisherz   0.01   True    4         0           0                   
sensitivity_size_control   continuous   fisherz   0.01   False   2         2           2                   
sensitivity_size_control   continuous   fisherz   0.05   True    5         0           0                   
sensitivity_size_control   continuous   fisherz   0.05   False   2         4           0                   
sensitivity_size_control   continuous   fisherz   0.1    True    6         0           0                   
sensitivity_size_control   continuous   fisherz   0.1    False   2         5           0                   
```

## Edge detail per setting

### [main] continuous / fisherz / alpha=0.01 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `year` -> `cross_topic_rate_t1`
- `year` -> `connectivity_t1_log`
- `year` -> `topic_share_t`
- `year` -> `log1p_median_c2`

### [main] continuous / fisherz / alpha=0.01 / unconstrained

Directed:
- `cross_topic_rate_t1` -> `year`
- `connectivity_t1_log` -> `year`
- `topic_share_t` -> `year`
- `log1p_median_c2` -> `year`
Undirected / ambiguous:
- `topic_share_t` -- `topic_share_t1`

### [main] continuous / fisherz / alpha=0.05 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `year` -> `cross_topic_rate_t1`
- `cross_topic_rate_t1` -> `log1p_median_c2`
- `year` -> `connectivity_t1_log`
- `year` -> `topic_share_t`
- `year` -> `log1p_median_c2`

### [main] continuous / fisherz / alpha=0.05 / unconstrained

Directed:
- `modularity_t1` -> `topic_share_t1`
- `topic_share_t` -> `topic_share_t1`  [TEMPORAL VIOLATION]
- `modularity_t1` -> `connectivity_t1_log`
- `year` -> `connectivity_t1_log`
Undirected / ambiguous:
- `cross_topic_rate_t1` -- `year`
- `cross_topic_rate_t1` -- `log1p_median_c2`
- `topic_share_t` -- `year`
- `log1p_median_c2` -- `year`

### [main] continuous / fisherz / alpha=0.1 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `year` -> `cross_topic_rate_t1`
- `cross_topic_rate_t1` -> `log1p_median_c2`
- `year` -> `connectivity_t1_log`
- `modularity_t1` -> `log1p_median_c2`
- `year` -> `topic_share_t`
- `year` -> `log1p_median_c2`

### [main] continuous / fisherz / alpha=0.1 / unconstrained

Directed:
- `modularity_t1` -> `topic_share_t1`
- `topic_share_t` -> `topic_share_t1`  [TEMPORAL VIOLATION]
- `modularity_t1` -> `connectivity_t1_log`
- `year` -> `connectivity_t1_log`
Undirected / ambiguous:
- `cross_topic_rate_t1` -- `year`
- `cross_topic_rate_t1` -- `log1p_median_c2`
- `log1p_median_c2` -- `modularity_t1`
- `topic_share_t` -- `year`
- `log1p_median_c2` -- `year`

### [main] discretized / chisq / alpha=0.01 / constrained

Directed:
- `topic_share_t1_bin` -> `topic_share_t_bin`
- `year_bin` -> `connectivity_t1_bin`
- `year_bin` -> `log1p_median_c2_bin`

### [main] discretized / chisq / alpha=0.01 / unconstrained

Undirected / ambiguous:
- `topic_share_t1_bin` -- `topic_share_t_bin`
- `connectivity_t1_bin` -- `year_bin`
- `log1p_median_c2_bin` -- `year_bin`

### [main] discretized / chisq / alpha=0.05 / constrained

Directed:
- `year_bin` -> `topic_share_t1_bin`
- `topic_share_t1_bin` -> `topic_share_t_bin`
- `cross_topic_rate_t1_bin` -> `log1p_median_c2_bin`
- `year_bin` -> `connectivity_t1_bin`
- `year_bin` -> `log1p_median_c2_bin`

### [main] discretized / chisq / alpha=0.05 / unconstrained

Directed:
- `year_bin` -> `topic_share_t1_bin`
- `topic_share_t_bin` -> `topic_share_t1_bin`  [TEMPORAL VIOLATION]
Undirected / ambiguous:
- `cross_topic_rate_t1_bin` -- `log1p_median_c2_bin`
- `connectivity_t1_bin` -- `year_bin`
- `log1p_median_c2_bin` -- `year_bin`

### [main] discretized / chisq / alpha=0.1 / constrained

Directed:
- `topic_share_t1_bin` -> `topic_share_t_bin`
- `year_bin` -> `cross_topic_rate_t1_bin`
- `year_bin` -> `connectivity_t1_bin`
- `year_bin` -> `log1p_median_c2_bin`

### [main] discretized / chisq / alpha=0.1 / unconstrained

Directed:
- `cross_topic_rate_t1_bin` -> `connectivity_t1_bin`
- `cross_topic_rate_t1_bin` -> `year_bin`
- `year_bin` -> `connectivity_t1_bin`
- `log1p_median_c2_bin` -> `year_bin`
Undirected / ambiguous:
- `topic_share_t1_bin` -- `topic_share_t_bin`

### [main] continuous / kci / alpha=0.01 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `year` -> `cross_topic_rate_t1`
- `year` -> `connectivity_t1_log`
- `connectivity_t1_log` -> `log1p_median_c2`
- `year` -> `modularity_t1`
- `year` -> `log1p_median_c2`

### [main] continuous / kci / alpha=0.01 / unconstrained

Directed:
- `modularity_t1` -> `topic_share_t1`
- `topic_share_t` -> `topic_share_t1`  [TEMPORAL VIOLATION]
- `cross_topic_rate_t1` -> `year`
- `connectivity_t1_log` -> `year`
- `modularity_t1` -> `year`
- `log1p_median_c2` -> `year`
Undirected / ambiguous:
- `cross_topic_rate_t1` -- `log1p_median_c2`
- `connectivity_t1_log` -- `modularity_t1`

### [main] continuous / kci / alpha=0.05 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `year` -> `cross_topic_rate_t1`
- `year` -> `connectivity_t1_log`
- `connectivity_t1_log` -> `log1p_median_c2`
- `year` -> `modularity_t1`
- `year` -> `log1p_median_c2`

### [main] continuous / kci / alpha=0.05 / unconstrained

Directed:
- `topic_share_t1` -> `modularity_t1`
- `cross_topic_rate_t1` -> `year`
- `modularity_t1` -> `connectivity_t1_log`
- `connectivity_t1_log` -> `year`
- `log1p_median_c2` -> `connectivity_t1_log`  [TEMPORAL VIOLATION]
- `year` -> `modularity_t1`
- `log1p_median_c2` -> `year`
Undirected / ambiguous:
- `topic_share_t` -- `topic_share_t1`

### [main] continuous / kci / alpha=0.1 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `year` -> `cross_topic_rate_t1`
- `year` -> `connectivity_t1_log`
- `connectivity_t1_log` -> `log1p_median_c2`
- `year` -> `modularity_t1`
- `year` -> `topic_share_t`
- `year` -> `log1p_median_c2`

### [main] continuous / kci / alpha=0.1 / unconstrained

Directed:
- `topic_share_t1` -> `modularity_t1`
- `cross_topic_rate_t1` -> `year`
- `connectivity_t1_log` -> `modularity_t1`
- `connectivity_t1_log` -> `year`
- `connectivity_t1_log` -> `log1p_median_c2`
- `year` -> `modularity_t1`
- `topic_share_t` -> `year`
- `year` -> `log1p_median_c2`
Undirected / ambiguous:
- `topic_share_t` -- `topic_share_t1`

### [sensitivity_outcome:topic_growth] continuous / fisherz / alpha=0.05 / constrained

Directed:
- `year` -> `topic_share_t1`
- `year` -> `cross_topic_rate_t1`
- `year` -> `connectivity_t1_log`
- `modularity_t1` -> `topic_growth`

### [sensitivity_outcome:topic_growth] discretized / chisq / alpha=0.05 / constrained

Directed:
- `year_bin` -> `topic_share_t1_bin`
- `year_bin` -> `cross_topic_rate_t1_bin`
- `year_bin` -> `connectivity_t1_bin`

### [sensitivity_outcome:topic_growth] continuous / fisherz / alpha=0.05 / unconstrained

Directed:
- `modularity_t1` -> `topic_share_t1`
- `year` -> `topic_share_t1`
- `modularity_t1` -> `connectivity_t1_log`
- `year` -> `connectivity_t1_log`
Undirected / ambiguous:
- `cross_topic_rate_t1` -- `year`
- `modularity_t1` -- `topic_growth`

### [sensitivity_outcome:topic_growth] discretized / chisq / alpha=0.05 / unconstrained

Directed:
- `cross_topic_rate_t1_bin` -> `topic_share_t1_bin`
- `year_bin` -> `topic_share_t1_bin`
- `cross_topic_rate_t1_bin` -> `year_bin`
- `connectivity_t1_bin` -> `year_bin`

### [sensitivity_outcome:hit_rate_2yr] continuous / fisherz / alpha=0.05 / constrained

Directed:
- `year` -> `topic_share_t1`
- `year` -> `cross_topic_rate_t1`
- `year` -> `connectivity_t1_log`
- `connectivity_t1_log` -> `hit_rate_2yr`

### [sensitivity_outcome:hit_rate_2yr] discretized / chisq / alpha=0.05 / constrained

Directed:
- `year_bin` -> `topic_share_t1_bin`
- `year_bin` -> `cross_topic_rate_t1_bin`
- `cross_topic_rate_t1_bin` -> `hit_rate_2yr_bin`
- `year_bin` -> `connectivity_t1_bin`
- `connectivity_t1_bin` -> `hit_rate_2yr_bin`

### [sensitivity_outcome:hit_rate_2yr] continuous / fisherz / alpha=0.05 / unconstrained

Directed:
- `modularity_t1` -> `topic_share_t1`
- `year` -> `topic_share_t1`
- `year` -> `connectivity_t1_log`
- `hit_rate_2yr` -> `connectivity_t1_log`  [TEMPORAL VIOLATION]
Undirected / ambiguous:
- `cross_topic_rate_t1` -- `year`

### [sensitivity_outcome:hit_rate_2yr] discretized / chisq / alpha=0.05 / unconstrained

Directed:
- `cross_topic_rate_t1_bin` -> `topic_share_t1_bin`
- `modularity_t1_bin` -> `topic_share_t1_bin`
- `year_bin` -> `topic_share_t1_bin`
- `year_bin` -> `connectivity_t1_bin`
- `hit_rate_2yr_bin` -> `connectivity_t1_bin`  [TEMPORAL VIOLATION]
Undirected / ambiguous:
- `cross_topic_rate_t1_bin` -- `year_bin`

### [sensitivity_no_year] continuous / fisherz / alpha=0.05 / constrained

Directed:
- `topic_share_t1` -> `topic_share_t`
- `cross_topic_rate_t1` -> `log1p_median_c2`
- `modularity_t1` -> `log1p_median_c2`

### [sensitivity_no_year] discretized / chisq / alpha=0.05 / constrained

Directed:
- `topic_share_t1_bin` -> `topic_share_t_bin`
- `cross_topic_rate_t1_bin` -> `log1p_median_c2_bin`
- `connectivity_t1_bin` -> `log1p_median_c2_bin`

### [sensitivity_no_year] continuous / fisherz / alpha=0.05 / unconstrained

Directed:
- `modularity_t1` -> `topic_share_t1`
- `topic_share_t` -> `topic_share_t1`  [TEMPORAL VIOLATION]
- `connectivity_t1_log` -> `modularity_t1`
- `log1p_median_c2` -> `modularity_t1`  [TEMPORAL VIOLATION]
Undirected / ambiguous:
- `cross_topic_rate_t1` -- `log1p_median_c2`

### [sensitivity_no_year] discretized / chisq / alpha=0.05 / unconstrained

Undirected / ambiguous:
- `topic_share_t1_bin` -- `topic_share_t_bin`
- `cross_topic_rate_t1_bin` -- `log1p_median_c2_bin`
- `connectivity_t1_bin` -- `log1p_median_c2_bin`

### [sensitivity_size_control] continuous / fisherz / alpha=0.01 / constrained

Directed:
- `n_papers_t1_log` -> `topic_share_t1`
- `topic_share_t1` -> `topic_share_t`
- `year` -> `connectivity_t1_log`
- `year` -> `topic_share_t`

### [sensitivity_size_control] continuous / fisherz / alpha=0.01 / unconstrained

Directed:
- `connectivity_t1_log` -> `year`
- `topic_share_t` -> `year`
Undirected / ambiguous:
- `n_papers_t1_log` -- `topic_share_t1`
- `topic_share_t` -- `topic_share_t1`

### [sensitivity_size_control] continuous / fisherz / alpha=0.05 / constrained

Directed:
- `n_papers_t1_log` -> `topic_share_t1`
- `topic_share_t1` -> `topic_share_t`
- `cross_topic_rate_t1` -> `log1p_median_c2`
- `year` -> `connectivity_t1_log`
- `n_papers_t1_log` -> `modularity_t1`

### [sensitivity_size_control] continuous / fisherz / alpha=0.05 / unconstrained

Directed:
- `modularity_t1` -> `connectivity_t1_log`
- `year` -> `connectivity_t1_log`
Undirected / ambiguous:
- `n_papers_t1_log` -- `topic_share_t1`
- `topic_share_t` -- `topic_share_t1`
- `cross_topic_rate_t1` -- `log1p_median_c2`
- `modularity_t1` -- `n_papers_t1_log`

### [sensitivity_size_control] continuous / fisherz / alpha=0.1 / constrained

Directed:
- `n_papers_t1_log` -> `topic_share_t1`
- `topic_share_t1` -> `topic_share_t`
- `cross_topic_rate_t1` -> `log1p_median_c2`
- `year` -> `connectivity_t1_log`
- `n_papers_t1_log` -> `modularity_t1`
- `year` -> `topic_share_t`

### [sensitivity_size_control] continuous / fisherz / alpha=0.1 / unconstrained

Directed:
- `modularity_t1` -> `connectivity_t1_log`
- `year` -> `connectivity_t1_log`
Undirected / ambiguous:
- `n_papers_t1_log` -- `topic_share_t1`
- `topic_share_t` -- `topic_share_t1`
- `cross_topic_rate_t1` -- `log1p_median_c2`
- `modularity_t1` -- `n_papers_t1_log`
- `topic_share_t` -- `year`

## Adjacency vs. orientation stability across constrained main-model settings

Across the 9 constrained **main-model** settings in this grid (continuous+Fisher-Z, discretized+chi-square, continuous+KCI, alpha in {0.01, 0.05, 0.10}): `adjacency_rate` is how often PC places *any* edge (directed or undirected) between the two variables; `orientation_rate_given_adjacent` is, of those adjacent settings, how often PC actually commits to a direction rather than leaving it undirected/ambiguous in the CPDAG. Kept as two separate numbers per the 2026-08-19 correction -- a stable adjacency with unstable orientation is a materially different finding from a fully stable directed edge. Sensitivity settings (different outcome/predictor sets) are excluded from this table. This is a cheap first look, not the Step 4 bootstrap stability analysis -- it only varies representation/test/alpha, not the sample itself.

```
               from                  to  n_settings_adjacent  n_settings_total  adjacency_rate  n_settings_oriented  orientation_rate_given_adjacent
     topic_share_t1       topic_share_t                    9                 9           1.000                    9                              1.0
               year     connectivity_t1                    9                 9           1.000                    9                              1.0
               year     log1p_median_c2                    9                 9           1.000                    9                              1.0
               year cross_topic_rate_t1                    7                 9           0.778                    7                              1.0
               year       topic_share_t                    4                 9           0.444                    4                              1.0
cross_topic_rate_t1     log1p_median_c2                    3                 9           0.333                    3                              1.0
               year       modularity_t1                    3                 9           0.333                    3                              1.0
    connectivity_t1     log1p_median_c2                    3                 9           0.333                    3                              1.0
               year      topic_share_t1                    1                 9           0.111                    1                              1.0
      modularity_t1     log1p_median_c2                    1                 9           0.111                    1                              1.0
```
