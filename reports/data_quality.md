# Data Quality Report -- NeurIPS Topic-Year Panel (v4)

Source: `data/raw/nips-panel-v4.csv`

## Citation-window finding (resolved)

`median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate in recent years (see the Citation-window check below). This was initially suspected to be right-censoring from a stale data pull, but the recovered panel-construction pipeline (`nips_pipeline_v4_clean.ipynb`, last run 2026-03-17) shows this concern is already handled: `median_cites_2yr` only uses papers whose 2-year citation window has fully elapsed (`c2_complete = current_year > pub_year + 1`), computed from OpenAlex's real per-year citation breakdown (`counts_by_year`), not a raw lifetime snapshot. Since the pipeline ran in 2026, every year through 2023 clears that bar -- the pattern is real, complete data.

The likely remaining explanation is OpenAlex's own citation-indexing lag for recent literature -- independently confirmed by a teammate who built the citation-enrichment step: *'OpenAlex gives significantly smaller values... it seems difficult to get citations up to year t.'* This is a substantive limitation worth discussing in the thesis, but **not** grounds to truncate or exclude recent-year rows -- there's no reason to treat those rows as less valid than earlier years.

**Corroborating evidence**: `median_cites_3yr` (a 3-year citation window, computed the same way but with one more year for citations to be indexed) shows a much milder version of the same pattern -- zero-citation rate by year, 2yr window -> 3yr window: 2021: 13% -> 0%; 2022: 40% -> 4%; 2023: 46% -> 25%. Giving citations one more year to be indexed sharply reduces the effect, which is exactly what an indexing-lag explanation predicts and a genuine decline in citation impact would not produce.

## Overview

- Rows: 156
- Unique topics: 29
- Years covered: 2013-2023
- Topics with only 1 row: 3
- Rows with no same-topic row at year-1 in this panel (but with populated `_t1` predictors anyway): 33
  - This means the panel is **filtered** (e.g. a minimum paper/author count per topic-year), not every topic-year combination -- the `_t1` features are computed from the full underlying corpus regardless of whether the prior year cleared the panel's inclusion threshold.

## Topic taxonomy

v4 has 29 unique topics after merging.

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
topic_share              156.0  0.040  0.027  0.006  0.035   0.115  0.706
```

## Correlation analysis (Pearson, core variables)

```
                         topic_share_t1  cross_topic_rate_t1  connectivity_t1  modularity_t1  bridge_concentration_t1  topic_growth  median_cites_2yr  log1p_median_c2  hit_rate_2yr  topic_share
topic_share_t1                     1.00                -0.13            -0.21           0.43                     0.36         -0.28              0.08             0.15         -0.13         0.92
cross_topic_rate_t1               -0.13                 1.00            -0.15           0.09                     0.08         -0.11             -0.12            -0.25         -0.18        -0.18
connectivity_t1                   -0.21                -0.15             1.00          -0.22                     0.08          0.19             -0.01            -0.01          0.44        -0.16
modularity_t1                      0.43                 0.09            -0.22           1.00                     0.30         -0.45             -0.14            -0.15         -0.08         0.31
bridge_concentration_t1            0.36                 0.08             0.08           0.30                     1.00         -0.29              0.03             0.03          0.00         0.33
topic_growth                      -0.28                -0.11             0.19          -0.45                    -0.29          1.00              0.19             0.18          0.24         0.05
median_cites_2yr                   0.08                -0.12            -0.01          -0.14                     0.03          0.19              1.00             0.90          0.59         0.19
log1p_median_c2                    0.15                -0.25            -0.01          -0.15                     0.03          0.18              0.90             1.00          0.56         0.26
hit_rate_2yr                      -0.13                -0.18             0.44          -0.08                     0.00          0.24              0.59             0.56          1.00        -0.03
topic_share                        0.92                -0.18            -0.16           0.31                     0.33          0.05              0.19             0.26         -0.03         1.00
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
topic_share                           0    -0.312  0.006   0.115
```

## Redundancy check (|Pearson r| > 0.5)

- `topic_share_t1` <-> `topic_share`: r=0.92
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
      n_rows  median_cites_2yr_mean  pct_zero_cites_2yr  hit_rate_2yr_mean  median_cites_3yr_mean  pct_zero_cites_3yr  n_valid_3yr
year                                                                                                                              
2013       4                  2.750               0.000              0.063                  6.500                0.00            4
2014       4                  3.000               0.000              0.041                  6.250                0.00            4
2015       6                  3.417               0.000              0.082                  7.750                0.00            6
2016       8                  4.688               0.000              0.115                 11.375                0.00            8
2017       9                  6.778               0.000              0.161                 16.389                0.00            9
2018      13                  6.577               0.000              0.114                 15.846                0.00           13
2019      16                  4.812               0.000              0.101                 11.438                0.00           16
2020      20                  4.125               0.000              0.099                  7.500                0.00           20
2021      23                  1.239               0.130              0.133                  3.587                0.00           23
2022      25                  1.640               0.400              0.124                  3.780                0.04           25
2023      28                  0.929               0.464              0.102                  1.964                0.25           28
```

## Flagged variables

- `bridge_concentration_t1` is near-degenerate: 14% of rows sit at/near 0 and 84% sit at/near 1, leaving very few rows in between. Continuous CI tests (Fisher-Z) assume a roughly continuous spread, so this variable is a poor fit for the continuous PC run -- treat it as effectively binary and rely on the discretized version for it. Per the recovered pipeline (`nips_pipeline_v4_clean.ipynb`), this is the share of total betweenness centrality held by the top 10% of authors in the topic's co-authorship graph -- on small author counts, a handful of authors mechanically dominate betweenness, which explains the degeneracy directly rather than just describing it.
- `modularity_t1` has low variance (compressed into [0.61, 0.99]) and correlates with topic size (corr with n_papers = 0.45): bigger topics tend to show higher modularity. Any edge involving modularity_t1 should be checked against topic size as a possible confound, and treated cautiously on small topics where a handful of authors can make the collaboration graph trivially "modular".
- `median_cites_2yr` is right-skewed (skew=1.99); its log-transformed twin `log1p_median_c2` is close to symmetric (skew=-0.01) and is the better choice for continuous Fisher-Z tests.
- `hit_rate_2yr` is a bounded proportion (range [0.00, 0.49]) and right-skewed (skew=1.23), not a raw count -- keep this in mind for the predictive-usefulness models in the evaluation framework later.
- Rows are (topic, year) pairs, and the same topic contributes multiple rows across years. Standard CI tests used by PC assume i.i.d. samples, which repeated observations of the same topic technically violate. This isn't fixed at the data-prep stage; the bootstrap/subsampling stability analysis in Step 4 is the empirical check against it. A within-topic-demeaned version is also worth adding as a Step 4 sensitivity setting, since pooling topics conflates between-topic differences with the within-topic t-1->t dynamic the model is actually meant to capture.
- `connectivity_t1` is heavily right-tailed (kurtosis far above every other variable, a handful of very high values) -- a log transform or winsorizing before the continuous Fisher-Z run would reduce the chance that a few extreme topic-years dominate the partial-correlation estimates.
- `median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate in recent years -- see the 'Citation-window finding' section above for the full explanation (OpenAlex citation-indexing lag, not a stale-extraction artifact) and the Citation-window check table below for the exact per-year numbers.

## t-1 minimum-graph-size filter (2026-08-19 correction)

Network predictors (`topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1`, `modularity_t1`, `bridge_concentration_t1`) are measured on the topic's **t-1** collaboration graph, not the t graph -- so the minimum-graph-size condition has to be checked against `n_papers_t1`, not `n_papers`. Both continuous and discretized output tables below have this filter already applied (rows with `n_papers_t1 < 20`, or no recoverable t-1 size at all, are dropped): **33 row(s) dropped**, 123 remain for the main model. The raw panel and every other section of this report still describe the full, unfiltered data -- only the two model-ready output tables are filtered.

## Recommendation for the first PC model

Per the 2026-08-19 correction, the **main model** outcome is `topic_share_t` (not `topic_growth` -- topic_growth is computed as log(topic_share_t) - log(topic_share_t1), so its dependence on topic_share_t1 is partly mechanical) plus `log1p_median_c2`; `topic_growth` and `hit_rate_2yr` are sensitivity-only outcomes. `bridge_concentration_t1` is dropped from the main model entirely (both continuous and discretized) for now -- near-degenerate, see flags above -- and `year` is included as an exogenous context variable with no edges allowed pointing into it (see constraints.py).

- Use the **continuous** table (`data/processed/topic_year_continuous.csv`) with Fisher-Z for the primary run: predictors `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1` (log-transformed), `modularity_t1`, plus `year`; outcomes `topic_share_t`, `log1p_median_c2`.
- Use the **discretized** table (`data/processed/topic_year_discretized.csv`) with chi-square/G-test as the sensitivity comparison. `bridge_concentration_t1_bin` is still produced in this table (for the separate bridge_concentration sensitivity setting) even though it's excluded from the main discretized model too.
- Carry `modularity_t1` in both versions, but flag any edge touching it during interpretation (Step 5 / thesis D4) as possibly confounded with topic size.
- `n_papers`/`n_authors` (t) are not part of the causal model but are kept as context columns for small-topic sanity checks; `n_papers_t1`/`n_authors_t1` are kept the same way, and are also what the minimum-graph-size filter above is computed from.
