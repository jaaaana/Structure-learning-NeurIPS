# Data Quality Report -- NeurIPS Topic-Year Panel

Source: `data/raw/nips-panel-v4.csv`

## Open issue requiring confirmation

`median_cites_2yr` / `hit_rate_2yr` show a zero-citation rate of 0% for every year 2013-2020, then jump to 13% (2021), 40% (2022), 46% (2023) -- see the Citation-window check below. This is consistent with an incomplete 2-year citation window for recent rows (either extraction timing or citation-indexing lag), and affects roughly half the panel (76/156 rows are 2021-2023).

## Overview

- Rows: 156
- Unique topics: 29
- Years covered: 2013-2023
- Topics with only 1 row: 3
- Rows with no same-topic row at year-1 in this panel (but with populated `_t1` predictors anyway): 33
  - This means the panel is **filtered** (e.g. a minimum paper/author count per topic-year), not every topic-year combination -- the `_t1` features are computed from the full underlying corpus regardless of whether the prior year cleared the panel's inclusion threshold.

### Rows per year

```
year
2013     4
2014     4
2015     6
2016     8
2017     9
2018    13
2019    16
2020    20
2021    23
2022    25
2023    28
```

## Missing values

None found across any column.

## Distribution summary (core variables)

```
                         count   mean    std    min    50%     max   skew
topic_share_t1           156.0  0.039  0.027  0.004  0.034   0.115  0.716
cross_topic_rate_t1      156.0  0.265  0.064  0.133  0.261   0.483  0.418
connectivity_t1          156.0  3.819  1.388  2.050  3.493  13.761  3.018
modularity_t1            156.0  0.915  0.056  0.615  0.928   0.987 -1.913
bridge_concentration_t1  156.0  0.853  0.347  0.000  1.000   1.000 -2.068
topic_growth             156.0  0.038  0.277 -0.641  0.016   0.752  0.001
median_cites_2yr         156.0  3.093  3.141  0.000  2.000  19.000  1.989
log1p_median_c2          156.0  1.157  0.720  0.000  1.099   2.996 -0.007
hit_rate_2yr             156.0  0.111  0.107  0.000  0.083   0.486  1.230
```

## Correlation analysis (Pearson, core variables)

```
                         topic_share_t1  cross_topic_rate_t1  connectivity_t1  modularity_t1  bridge_concentration_t1  topic_growth  median_cites_2yr  log1p_median_c2  hit_rate_2yr
topic_share_t1                     1.00                -0.13            -0.21           0.43                     0.36         -0.28              0.08             0.15         -0.13
cross_topic_rate_t1               -0.13                 1.00            -0.15           0.09                     0.08         -0.11             -0.12            -0.25         -0.18
connectivity_t1                   -0.21                -0.15             1.00          -0.22                     0.08          0.19             -0.01            -0.01          0.44
modularity_t1                      0.43                 0.09            -0.22           1.00                     0.30         -0.45             -0.14            -0.15         -0.08
bridge_concentration_t1            0.36                 0.08             0.08           0.30                     1.00         -0.29              0.03             0.03          0.00
topic_growth                      -0.28                -0.11             0.19          -0.45                    -0.29          1.00              0.19             0.18          0.24
median_cites_2yr                   0.08                -0.12            -0.01          -0.14                     0.03          0.19              1.00             0.90          0.59
log1p_median_c2                    0.15                -0.25            -0.01          -0.15                     0.03          0.18              0.90             1.00          0.56
hit_rate_2yr                      -0.13                -0.18             0.44          -0.08                     0.00          0.24              0.59             0.56          1.00
```

## Outliers and heavy tails (IQR method)

```
                         n_outliers_iqr  kurtosis    min     max
variable                                                        
topic_share_t1                        0    -0.337  0.004   0.115
cross_topic_rate_t1                   1     0.338  0.133   0.483
connectivity_t1                       6    17.011  2.050  13.761
modularity_t1                         4     6.088  0.615   0.987
bridge_concentration_t1              28     2.331  0.000   1.000
topic_growth                          0    -0.450 -0.641   0.752
median_cites_2yr                      9     5.551  0.000  19.000
log1p_median_c2                       1    -0.520  0.000   2.996
hit_rate_2yr                          4     1.210  0.000   0.486
```

## Redundancy check (|Pearson r| > 0.5)

- `median_cites_2yr` <-> `log1p_median_c2`: r=0.90
- `median_cites_2yr` <-> `hit_rate_2yr`: r=0.59
- `log1p_median_c2` <-> `hit_rate_2yr`: r=0.56

## Small-graph instability check (modularity_t1 / bridge_concentration_t1 by topic-size quartile)

```
               n_papers_mean  modularity_t1_mean  modularity_t1_std  bridge_concentration_t1_mean  bridge_concentration_t1_std
size_quartile                                                                                                                 
Q1                    23.900               0.869              0.067                         0.665                        0.468
Q2                    34.842               0.908              0.038                         0.809                        0.390
Q3                    56.675               0.930              0.035                         0.947                        0.220
Q4                   147.316               0.954              0.038                         0.995                        0.008
```

## Citation-window check (median_cites_2yr / hit_rate_2yr by year)

```
      n_rows  median_cites_2yr_mean  pct_zero_cites  hit_rate_2yr_mean
year                                                                  
2013       4                  2.750           0.000              0.063
2014       4                  3.000           0.000              0.041
2015       6                  3.417           0.000              0.082
2016       8                  4.688           0.000              0.115
2017       9                  6.778           0.000              0.161
2018      13                  6.577           0.000              0.114
2019      16                  4.812           0.000              0.101
2020      20                  4.125           0.000              0.099
2021      23                  1.239           0.130              0.133
2022      25                  1.640           0.400              0.124
2023      28                  0.929           0.464              0.102
```

## Flagged variables

- `bridge_concentration_t1` is near-degenerate: 14% of rows sit at/near 0 and 84% sit at/near 1, leaving very few rows in between. Continuous CI tests (Fisher-Z) assume a roughly continuous spread, so this variable is a poor fit for the continuous PC run -- treat it as effectively binary and rely on the discretized version for it.
- `modularity_t1` has low variance (compressed into [0.61, 0.99]) and correlates with topic size (corr with n_papers = 0.45): bigger topics tend to show higher modularity. Any edge involving modularity_t1 should be checked against topic size as a possible confound, and treated cautiously on small topics where a handful of authors can make the collaboration graph trivially "modular".
- `median_cites_2yr` is right-skewed (skew=1.99); its log-transformed twin `log1p_median_c2` is close to symmetric (skew=-0.01) and is the better choice for continuous Fisher-Z tests.
- `hit_rate_2yr` is a bounded proportion (range [0.00, 0.49]) and right-skewed (skew=1.23), not a raw count -- keep this in mind for the predictive-usefulness models in the evaluation framework later.
- `connectivity_t1` is heavily right-tailed (kurtosis far above every other variable, a handful of very high values) -- a log transform or winsorizing before the continuous Fisher-Z run would reduce the chance that a few extreme topic-years dominate the partial-correlation estimates.
- `median_cites_2yr` / `hit_rate_2yr` show a suspicious jump in zero-citation rate for recent years -- 2013-2020 all sit at 0% zero-rate, then it climbs to 13% (2021), 40% (2022), 46% (2023). This pattern is consistent with the 2-year citation window not being fully reflected in the underlying citation snapshot for the most recent years (either the query predates full window closure, or citation-indexing lag in the source database).
