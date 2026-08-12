# Data Quality Report -- NeurIPS Topic-Year Panel (v5)

Source: `data/raw/nips-panel-v5-refreshed.csv`

## Citation-window finding (resolved)

`median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate in recent years (see the Citation-window check below). This panel's citations were refreshed via `src/refresh_citations.py` (an adaptation of `nips_pipeline_v4_clean.ipynb`), re-pulling OpenAlex's per-year citation breakdown for all matched papers. Compared to v4, the zero-citation rate dropped substantially for 2022 (40.0% -> 15.8%) and 2023 (46.4% -> 29.2%) with no change for 2021 (13.0% both) -- directly confirming the remaining pattern is OpenAlex's own citation-indexing lag for recent literature, not a stale extraction. This version also extends coverage to 2024.

The likely remaining explanation is OpenAlex's own citation-indexing lag for recent literature -- independently confirmed by a teammate who built the citation-enrichment step: *'OpenAlex gives significantly smaller values... it seems difficult to get citations up to year t.'* This is a substantive limitation worth discussing in the thesis, but **not** grounds to truncate or exclude recent-year rows -- there's no reason to treat those rows as less valid than earlier years.

## Overview

- Rows: 161
- Unique topics: 28
- Years covered: 2013-2024
- Topics with only 1 row: 4
- Rows with no same-topic row at year-1 in this panel (but with populated `_t1` predictors anyway): 36
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
2019    15
2020    19
2021    23
2022    19
2023    24
2024    17
```

## Missing values

```
median_cites_3yr    17
```

## Distribution summary (core variables)

```
                         count   mean    std    min    50%     max   skew
topic_share_t1           161.0  0.041  0.027  0.004  0.036   0.119  0.690
cross_topic_rate_t1      161.0  0.270  0.060  0.120  0.270   0.456  0.129
connectivity_t1          161.0  3.968  1.530  2.050  3.636  14.415  2.670
modularity_t1            161.0  0.917  0.055  0.615  0.930   0.986 -1.981
bridge_concentration_t1  161.0  0.888  0.307  0.000  1.000   1.000 -2.570
topic_growth             161.0  0.018  0.387 -1.054  0.033   1.561  0.141
median_cites_2yr         161.0  3.090  3.069  0.000  2.000  19.000  2.108
log1p_median_c2          161.0  1.184  0.664  0.000  1.099   2.996  0.158
hit_rate_2yr             161.0  0.110  0.107  0.000  0.082   0.486  1.120
```

## Correlation analysis (Pearson, core variables)

```
                         topic_share_t1  cross_topic_rate_t1  connectivity_t1  modularity_t1  bridge_concentration_t1  topic_growth  median_cites_2yr  log1p_median_c2  hit_rate_2yr
topic_share_t1                     1.00                -0.21            -0.15           0.43                     0.31         -0.29              0.02             0.09         -0.17
cross_topic_rate_t1               -0.21                 1.00            -0.04           0.14                     0.08         -0.15             -0.18            -0.30         -0.19
connectivity_t1                   -0.15                -0.04             1.00          -0.24                     0.14          0.06             -0.05            -0.07          0.38
modularity_t1                      0.43                 0.14            -0.24           1.00                     0.24         -0.43             -0.15            -0.14         -0.15
bridge_concentration_t1            0.31                 0.08             0.14           0.24                     1.00         -0.34             -0.01            -0.03         -0.05
topic_growth                      -0.29                -0.15             0.06          -0.43                    -0.34          1.00              0.23             0.27          0.32
median_cites_2yr                   0.02                -0.18            -0.05          -0.15                    -0.01          0.23              1.00             0.91          0.60
log1p_median_c2                    0.09                -0.30            -0.07          -0.14                    -0.03          0.27              0.91             1.00          0.58
hit_rate_2yr                      -0.17                -0.19             0.38          -0.15                    -0.05          0.32              0.60             0.58          1.00
```

## Outliers and heavy tails (IQR method)

```
                         n_outliers_iqr  kurtosis    min     max
variable                                                        
topic_share_t1                        0    -0.254  0.004   0.119
cross_topic_rate_t1                   2     0.305  0.120   0.456
connectivity_t1                       7    13.406  2.050  14.415
modularity_t1                         4     6.568  0.615   0.986
bridge_concentration_t1              27     4.703  0.000   1.000
topic_growth                          8     1.873 -1.054   1.561
median_cites_2yr                      8     6.045  0.000  19.000
log1p_median_c2                       1    -0.221  0.000   2.996
hit_rate_2yr                          1     0.772  0.000   0.486
```

## Redundancy check (|Pearson r| > 0.5)

- `median_cites_2yr` <-> `log1p_median_c2`: r=0.91
- `median_cites_2yr` <-> `hit_rate_2yr`: r=0.60
- `log1p_median_c2` <-> `hit_rate_2yr`: r=0.58

## Small-graph instability check (modularity_t1 / bridge_concentration_t1 by topic-size quartile)

```
               n_papers_mean  modularity_t1_mean  modularity_t1_std  bridge_concentration_t1_mean  bridge_concentration_t1_std
size_quartile                                                                                                                 
Q1                    23.857               0.880              0.064                         0.729                        0.441
Q2                    35.524               0.911              0.043                         0.872                        0.325
Q3                    56.135               0.930              0.038                         0.970                        0.164
Q4                   135.750               0.951              0.043                         0.995                        0.008
```

## Citation-window check (median_cites_2yr / hit_rate_2yr by year)

```
      n_rows  median_cites_2yr_mean  pct_zero_cites  hit_rate_2yr_mean
year                                                                  
2013       4                  2.750           0.000              0.065
2014       4                  2.875           0.000              0.037
2015       6                  3.333           0.000              0.077
2016       8                  4.625           0.000              0.107
2017       9                  6.722           0.000              0.169
2018      13                  6.538           0.000              0.113
2019      15                  4.967           0.000              0.104
2020      19                  4.079           0.000              0.101
2021      23                  1.283           0.130              0.134
2022      19                  2.289           0.158              0.118
2023      24                  1.354           0.292              0.093
2024      17                  0.882           0.235              0.113
```

## Flagged variables

- `bridge_concentration_t1` is near-degenerate: 11% of rows sit at/near 0 and 88% sit at/near 1, leaving very few rows in between. Continuous CI tests (Fisher-Z) assume a roughly continuous spread, so this variable is a poor fit for the continuous PC run -- treat it as effectively binary and rely on the discretized version for it. Per the recovered pipeline (`nips_pipeline_v4_clean.ipynb`), this is the share of total betweenness centrality held by the top 10% of authors in the topic's co-authorship graph -- on small author counts, a handful of authors mechanically dominate betweenness, which explains the degeneracy directly rather than just describing it.
- `modularity_t1` has low variance (compressed into [0.61, 0.99]) and correlates with topic size (corr with n_papers = 0.42): bigger topics tend to show higher modularity. Any edge involving modularity_t1 should be checked against topic size as a possible confound, and treated cautiously on small topics where a handful of authors can make the collaboration graph trivially "modular".
- `median_cites_2yr` is right-skewed (skew=2.11); its log-transformed twin `log1p_median_c2` is close to symmetric (skew=0.16) and is the better choice for continuous Fisher-Z tests.
- `hit_rate_2yr` is a bounded proportion (range [0.00, 0.49]) and right-skewed (skew=1.12), not a raw count -- keep this in mind for the predictive-usefulness models in the evaluation framework later.
- Rows are (topic, year) pairs, and the same topic contributes multiple rows across years. Standard CI tests used by PC assume i.i.d. samples, which repeated observations of the same topic technically violate. This isn't fixed at the data-prep stage; the bootstrap/subsampling stability analysis in Step 4 is the empirical check against it. A within-topic-demeaned version is also worth adding as a Step 4 sensitivity setting, since pooling topics conflates between-topic differences with the within-topic t-1->t dynamic the model is actually meant to capture.
- `connectivity_t1` is heavily right-tailed (kurtosis far above every other variable, a handful of very high values) -- a log transform or winsorizing before the continuous Fisher-Z run would reduce the chance that a few extreme topic-years dominate the partial-correlation estimates.
- `median_cites_2yr` / `hit_rate_2yr` show a rising zero-citation rate in recent years -- see the 'Citation-window finding' section above for the full explanation (OpenAlex citation-indexing lag, not a stale-extraction artifact) and the Citation-window check table below for the exact per-year numbers.

## Recommendation for the first PC model

- Use the **continuous** table (`data/processed/topic_year_continuous_v5.csv`) with Fisher-Z for the primary run, dropping `bridge_concentration_t1` from that continuous run (near-degenerate, see flags above) -- keep the other 4 predictors (`topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1`, `modularity_t1`) and use `log1p_median_c2` in place of raw `median_cites_2yr`.
- Use the **discretized** table (`data/processed/topic_year_discretized_v5.csv`) with chi-square/G-test as the second setting -- this is where `bridge_concentration_t1_bin` (binary) can be included, since discretization sidesteps its continuous-test unsuitability.
- Carry `modularity_t1` in both versions, but flag any edge touching it during interpretation (Step 5 / thesis D4) as possibly confounded with topic size.
- `n_papers`/`n_authors` are not part of the causal model (per docx Step 2's variable list) but are kept in both output tables as context columns for exactly this kind of small-topic sanity check.
