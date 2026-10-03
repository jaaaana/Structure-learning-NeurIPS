# Final Team Deliverable -- Step 5 (v5)

Classifies every predictor/exogenous edge seen in the Step 4 topic-level block bootstrap (`bootstrap_stability.py`, 500 replicates) into a tier, using both the continuous+Fisher-Z and discretized+chi-square representations rather than a single adjacency number. `excluded` overrides the numeric tiers regardless of rate, but only for variables entirely absent from the model-ready data (see 'Excluded from interpretation'). `modularity_t1` edges are a different case: they get their real tier from the numbers like everything else, but are additionally flagged `[SIZE CONFOUND]` wherever they appear, since `pc_learning.py`'s `sensitivity_size_control` group shows every `modularity_t1 -> outcome` edge disappears once topic size is controllable -- a reason to be skeptical of the edge's interpretation, not a reason to hide its actual numbers. Thresholds: stable >= 0.7 mean rate (representation gap <= 0.3), candidate >= 0.3 mean rate (same gap requirement), ambiguous = gap > 0.3 regardless of mean, weak = everything else. Classified independently per dataset version -- v4 and v5 can and do disagree on some edges.

These tiers are computed from **adjacency rate alone** -- whether an edge appears at all, in either bootstrap representation -- never from orientation rate. Under this pipeline's temporal-tier background knowledge, every edge that can appear at all is between two different tiers, and `causal-learn` mechanically forces its direction immediately after skeleton discovery, before any independent PC orientation logic runs; see `bootstrap_stability.md`'s orientation-stability caveat and 'Orientation provenance' section for the full derivation.

**`stable`/`candidate`/`ambiguous`/`weak` are descriptive labels for a bootstrap-adjacency-frequency bucket, nothing more** -- they are not p-values, confidence intervals, or any other statistical significance test, and clearing the `stable` bar is not a correctness or causal-truth claim. They also describe **adjacency only**: whether the edge recurs across replicates, never which direction it points (see the paragraph above and the `[T]`/`unconstrained_same_direction` annotations for that, a fully separate question).

## Main graph (frozen setting: continuous / Fisher-Z / alpha=0.05 / constrained)

6 directed edges, 0 undirected, on n=127 rows. Every edge below is annotated with its tier from the bootstrap classification (not just this single run).

Every edge's *direction* here is `[T]` -- forced by the temporal background knowledge, not discovered by PC on its own. Under this model's tier structure, every edge that can exist at all is between two different tiers, and `causal-learn` mechanically orients any such edge immediately after skeleton discovery, before its own v-structure or Meek orientation logic ever runs -- there is no edge in this graph that could have been genuinely `[PC]`-oriented under these constraints (see `bootstrap_stability.md`'s 'Orientation provenance' section for the full derivation). `unconstrained_same_direction` below is the one independent check available: the share of an unconstrained bootstrap's adjacent replicates (same resampled data, no background knowledge at all) where PC's own orientation logic landed on this same direction anyway -- high means the data corroborates the assumption, low means the direction rests on the temporal assumption alone.

```
topic_share_t1 -> topic_share_t   [T, unconstrained_same_direction=0.016]   [stable, mean_rate=1.000]
year -> cross_topic_rate_t1   [T, unconstrained_same_direction=0.182]   [stable, mean_rate=0.777]
cross_topic_rate_t1 -> log1p_median_c2   [T, unconstrained_same_direction=0.174]   [candidate, mean_rate=0.640]
year -> connectivity_t1_log   [T, unconstrained_same_direction=0.498]   [stable, mean_rate=0.967]
year -> topic_share_t   [T, unconstrained_same_direction=0.073]   [ambiguous, mean_rate=0.524]
year -> log1p_median_c2   [T, unconstrained_same_direction=0.151]   [stable, mean_rate=0.935]
```

## Stable-edge graph

Cleared the stability bar in both representations.

```
from                   to                   continuous  discretized  mean    gap    flag
topic_share_t1         topic_share_t        1.0         1.0          1.0     0.0    
year                   connectivity_t1      1.0         0.934        0.967   0.066  
year                   log1p_median_c2      0.97        0.9          0.935   0.07   
year                   cross_topic_rate_t1  0.832       0.722        0.777   0.11   
```

## Candidate edges

Moderate, consistent-direction signal -- tentative, not stable.

```
from                   to                   continuous  discretized  mean    gap    flag
cross_topic_rate_t1    log1p_median_c2      0.496       0.784        0.64    0.288  
modularity_t1          log1p_median_c2      0.37        0.506        0.438   0.136  SIZE_CONFOUND
year                   modularity_t1        0.298       0.566        0.432   0.268  
```
- `modularity_t1 -> log1p_median_c2`: flagged size confound -- pc_learning.py's sensitivity_size_control group shows this edge disappears (replaced by `n_papers_t1_log -> modularity_t1`) once topic size is available to condition on. Its tier above is from the real adjacency rate; this flag is a reason to be skeptical of its interpretation, not a reason to disbelieve the rate itself.
## Ambiguous edges

Large swing between continuous and discretized representations -- likely a representation artifact (linear vs. binned CI test), not interpretable as a finding either way without further work.

```
from                   to                   continuous  discretized  mean    gap    flag
year                   topic_share_t        0.684       0.364        0.524   0.32   
year                   topic_share_t1       0.02        0.62         0.32    0.6    
connectivity_t1        log1p_median_c2      0.022       0.596        0.309   0.574  
connectivity_t1        topic_share_t        0.002       0.328        0.165   0.326  
cross_topic_rate_t1    topic_share_t        0.006       0.316        0.161   0.31   
```

## Excluded from interpretation

Overridden regardless of numeric rate -- see reason per edge.

(none)

## Cross-reference: predictive usefulness (Step 5 / D2.3)

`graph_parents_nested_cv` below selects its additional predictors separately inside each cross-validation fold, using only that fold's training topics, specifically to avoid the held-out fold's topics leaking into predictor selection (see `predictive_usefulness_v5.md` for the full nested-CV detail). It is a different statistic from the stable/candidate tiers above (which use the full-dataset, both-representations bootstrap) -- not the same number restated under a new name.

- `topic_share_t`: baseline R²=0.693, all_t1=0.688, all_t1_no_modularity=0.696, graph_parents_nested_cv=0.693 (see `predictive_usefulness_v5.md` for full CV detail).
- `log1p_median_c2`: baseline R²=-0.067, all_t1=0.263, all_t1_no_modularity=0.140, graph_parents_nested_cv=-0.089 (see `predictive_usefulness_v5.md` for full CV detail).

Note: `sensitivity_outcome:topic_growth`/`:hit_rate_2yr` and `sensitivity_no_year` (in `pc_settings_comparison_v5.md`) are single-run results, not bootstrap-replicated, so they are not tier-classified above -- treat them as context, not stability evidence.

## Interpretation

The only edges stable across both bootstrap representations for v5 are: `topic_share_t1->topic_share_t`, `year->connectivity_t1`, `year->log1p_median_c2`, `year->cross_topic_rate_t1`. These are dominated by mechanical persistence (`topic_share_t1->topic_share_t`) and calendar-time absorption (`year` into `connectivity_t1`/`log1p_median_c2`), not by a genuinely novel structural mechanism. `modularity_t1`'s edges get their tier from their real adjacency rate like any other edge (typically `candidate` or `weak` here, never `stable`), but are flagged `[SIZE CONFOUND]`/`SIZE_CONFOUND` wherever they appear: `pc_learning.py`'s `sensitivity_size_control` group shows every `modularity_t1 -> outcome` edge disappears, replaced by `n_papers_t1_log -> modularity_t1`, once topic size is controllable -- read any `modularity_t1` edge below as a demonstrated size confound regardless of its numeric tier. `connectivity_t1->log1p_median_c2` is flagged ambiguous rather than reported either way, since its adjacency rate depends almost entirely on which CI test (linear vs. binned) is used. The most defensible candidate for a real, non-mechanical structural relationship is `cross_topic_rate_t1->log1p_median_c2`, which survives as stable or candidate depending on version without being refuted by any sensitivity check run so far -- still a candidate, not a proven causal claim, given PC's Markov/faithfulness/i.i.d. assumptions are not fully met by this panel.
