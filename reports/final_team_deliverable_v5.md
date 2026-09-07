# Final Team Deliverable -- Step 5 (v5)

Classifies every predictor/exogenous edge seen in the Step 4 topic-level block bootstrap (`bootstrap_stability.py`, 500 replicates) into a tier, using both the continuous+Fisher-Z and discretized+chi-square representations rather than a single adjacency number. `excluded` overrides the numeric tiers regardless of rate -- see the 'Excluded from interpretation' section. Thresholds: stable >= 0.7 mean rate (representation gap <= 0.3), candidate >= 0.3 mean rate (same gap requirement), ambiguous = gap > 0.3 regardless of mean, weak = everything else. Classified independently per dataset version -- v4 and v5 can and do disagree on some edges.

## Main graph (frozen setting: continuous / Fisher-Z / alpha=0.05 / constrained)

6 directed edges, 0 undirected, on n=127 rows. Every edge below is annotated with its tier from the bootstrap classification (not just this single run).

```
topic_share_t1 -> topic_share_t   [stable, mean_rate=1.000]
year -> cross_topic_rate_t1   [stable, mean_rate=0.777]
cross_topic_rate_t1 -> log1p_median_c2   [candidate, mean_rate=0.640]
year -> connectivity_t1_log   [stable, mean_rate=0.967]
year -> topic_share_t   [ambiguous, mean_rate=0.524]
year -> log1p_median_c2   [stable, mean_rate=0.935]
```

## Stable-edge graph

Cleared the stability bar in both representations.

```
from                   to                   continuous  discretized  mean    gap   
topic_share_t1         topic_share_t        1.0         1.0          1.0     0.0   
year                   connectivity_t1      1.0         0.934        0.967   0.066 
year                   log1p_median_c2      0.97        0.9          0.935   0.07  
year                   cross_topic_rate_t1  0.832       0.722        0.777   0.11  
```

## Candidate edges

Moderate, consistent-direction signal -- tentative, not stable.

```
from                   to                   continuous  discretized  mean    gap   
cross_topic_rate_t1    log1p_median_c2      0.496       0.784        0.64    0.288 
year                   modularity_t1        0.298       0.566        0.432   0.268 
```

## Ambiguous edges

Large swing between continuous and discretized representations -- likely a representation artifact (linear vs. binned CI test), not interpretable as a finding either way without further work.

```
from                   to                   continuous  discretized  mean    gap   
year                   topic_share_t        0.684       0.364        0.524   0.32  
year                   topic_share_t1       0.02        0.62         0.32    0.6   
connectivity_t1        log1p_median_c2      0.022       0.596        0.309   0.574 
connectivity_t1        topic_share_t        0.002       0.328        0.165   0.326 
cross_topic_rate_t1    topic_share_t        0.006       0.316        0.161   0.31  
```

## Excluded from interpretation

Overridden regardless of numeric rate -- see reason per edge.

```
from                   to                   continuous  discretized  mean    gap   
modularity_t1          log1p_median_c2      0.37        0.506        0.438   0.136 
modularity_t1          topic_share_t        0.056       0.078        0.067   0.022 
```
- `modularity_t1 -> log1p_median_c2`: size confound -- pc_learning.py's sensitivity_size_control group shows this edge disappears (replaced by `n_papers_t1_log -> modularity_t1`) once topic size is available to condition on.
- `modularity_t1 -> topic_share_t`: size confound -- pc_learning.py's sensitivity_size_control group shows this edge disappears (replaced by `n_papers_t1_log -> modularity_t1`) once topic size is available to condition on.
- `bridge_concentration_t1` is near-degenerate (mass at 0/1) and was already excluded from the main model at Step 1 -- listed here for completeness, not because it appeared in the bootstrap.

## Cross-reference: predictive usefulness (Step 5 / D2.3)

- `topic_share_t`: baseline R²=0.688, all_t1=0.688, all_t1_no_modularity=0.696, graph_parents=0.693 (see `predictive_usefulness_v5.md` for full CV detail).
- `log1p_median_c2`: baseline R²=-0.210, all_t1=0.263, all_t1_no_modularity=0.140, graph_parents=-0.036 (see `predictive_usefulness_v5.md` for full CV detail).

Note: `sensitivity_outcome:topic_growth`/`:hit_rate_2yr` and `sensitivity_no_year` (in `pc_settings_comparison_v5.md`) are single-run results, not bootstrap-replicated, so they are not tier-classified above -- treat them as context, not stability evidence.

## Interpretation

The only edges stable across both bootstrap representations for v5 are: `topic_share_t1->topic_share_t`, `year->connectivity_t1`, `year->log1p_median_c2`, `year->cross_topic_rate_t1`. These are dominated by mechanical persistence (`topic_share_t1->topic_share_t`) and calendar-time absorption (`year` into `connectivity_t1`/`log1p_median_c2`), not by a genuinely novel structural mechanism. `modularity_t1`'s edges, despite moderate raw adjacency rates, are excluded outright as a demonstrated size confound. `connectivity_t1->log1p_median_c2` is flagged ambiguous rather than reported either way, since its adjacency rate depends almost entirely on which CI test (linear vs. binned) is used. The most defensible candidate for a real, non-mechanical structural relationship is `cross_topic_rate_t1->log1p_median_c2`, which survives as stable or candidate depending on version without being refuted by any sensitivity check run so far -- still a candidate, not a proven causal claim, given PC's Markov/faithfulness/i.i.d. assumptions are not fully met by this panel.
