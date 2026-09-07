# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

Master's thesis project: causal structure learning (PC algorithm) over a
NeurIPS topic-year panel. The question being asked is whether a topic's
collaboration-graph structure at year `t-1` predicts that topic's growth and
early citation impact at year `t`. The pipeline runs in numbered steps, each
a script under `src/`, each writing its output to `reports/` or
`data/processed/`.

There is no `requirements.txt`/`pyproject.toml` in the repo (the checked-in
`.venv` is empty). Dependencies are only discoverable from imports:
`pandas`, `numpy`, `scipy`, `scikit-learn`, `networkx`, `requests`, `ftfy`,
and `causal-learn` (imported as `causallearn`). Install these manually before
running anything.

## Commands

Every step script takes `--version {v4,v5}` (default `v4`) and must be run
from the repo root (paths resolve via `ROOT = Path(__file__).resolve().parent.parent`).
Run steps in order — later steps import from earlier ones and read their
output files:

```bash
python src/data_prep.py --version v5       # Step 1: data quality report + continuous/discretized tables
python src/constraints.py                  # Step 2: temporal edge constraints (not versioned, shared by v4/v5)
python src/pc_learning.py --version v5     # Step 3: PC algorithm grid, imports constraints.py + data_prep.py
```

Refreshing the raw citation panel (upstream of Step 1, only needed to
regenerate `data/raw/nips-panel-v5-refreshed.csv` from scratch) requires an
OpenAlex API key via the `OPENALEX_API_KEY` env var (or an interactive
prompt) and makes live API calls:

```bash
python src/refresh_citations.py
```

There is no test suite, linter, or build step in this repo.

## Architecture

**Versioning convention**: `v4` and `v5` are two parallel runs of the same
pipeline over different input panels (`data/raw/nips-panel-v4.csv` vs.
`data/raw/nips-panel-v5-refreshed.csv`, v5 extends coverage to 2024 and has
refreshed citation counts). Every script keys its inputs/outputs off this
version string (see `DATASETS` in `data_prep.py`) so that running one version
never touches the other's files. When adding a new pipeline step, follow the
same pattern rather than branching internally on version-specific logic.

**Pipeline (in dependency order)**:

1. `src/refresh_citations.py` — rebuilds the raw panel from
   `data/raw/nips-papers_enriched_openalex.csv`: re-pulls per-year citation
   breakdowns from OpenAlex (checkpointed to `data/processed/nips-c2-checkpoint.csv`
   so reruns don't re-fetch), re-clusters raw OpenAlex topic labels into a
   canonical topic taxonomy via TF-IDF + hierarchical clustering
   (`merge_topics`, output map in `data/processed/nips-topic-merge-map.json`),
   computes author co-authorship graph metrics per topic-year
   (`graph_metrics`: connectivity, modularity via Louvain, betweenness
   concentration), and lags every structural predictor by one year to
   produce the `_t1` columns. This is an adaptation of the recovered
   original pipeline notebook `nips_pipeline_v4_clean.ipynb`.
2. `src/data_prep.py` (Step 1) — loads the raw panel, writes a data-quality
   report (`reports/data_quality[_v5].md`), applies the t-1 minimum-graph-size
   filter (`MIN_T1_SIZE`, checked against `n_papers_t1` not `n_papers`, since
   the `_t1` predictors are measured on the t-1 graph), and emits two
   model-ready tables: a continuous version
   (`data/processed/topic_year_continuous[_v5].csv`) and a tertile-discretized
   version (`data/processed/topic_year_discretized[_v5].csv`).
3. `src/constraints.py` (Step 2) — defines the temporal tier structure shared
   by every PC run: `EXOGENOUS` (`year`, nothing may point into it), `TIER_0`
   (t-1 structural predictors), `TIER_1` (t outcomes). Exports a
   `build_background_knowledge(node_names)` function that builds a
   `causallearn` `BackgroundKnowledge` object from *whatever subset* of
   variables a given PC run uses — it strips `_bin`/`_log` suffixes via
   `_base_name()` before tier lookup, so the same function works unmodified
   across continuous/discretized/log-transformed variants. Also defines the
   main-vs-sensitivity variable split (`MAIN_PREDICTORS`/`MAIN_OUTCOMES` vs.
   `SENSITIVITY_PREDICTORS_ONLY`/`SENSITIVITY_OUTCOMES_ONLY`) that Step 3
   consumes. Writes `reports/edge_constraints.{md,json}`.
4. `src/pc_learning.py` (Step 3) — runs `causallearn`'s PC algorithm across a
   grid: {continuous+Fisher-Z, discretized+chi-square, continuous+KCI} x
   {alpha in 0.01/0.05/0.10} x {constrained (Step 2 background knowledge) /
   unconstrained}, plus lighter sensitivity groups (alternate outcomes,
   with/without `year`). Unconstrained runs are checked against the temporal
   rule after the fact (`count_temporal_violations`) rather than being
   constrained during search — that's the point of running them
   unconstrained. Writes the full settings comparison
   (`reports/pc_settings_comparison[_v5].md`) plus raw results JSON
   (`reports/pc_runs/pc_runs[_v5].json`).

**Main model** (current, per the 2026-08-19 correction — see
below): predictors `topic_share_t1`, `cross_topic_rate_t1`, `connectivity_t1`
(log-transformed for the continuous run), `modularity_t1`, plus exogenous
`year`; outcomes `topic_share_t`, `log1p_median_c2`. `bridge_concentration_t1`
is dropped from the main model (near-degenerate — see Step 1's flagged
variables). `topic_growth` and `hit_rate_2yr` are sensitivity-only outcomes,
not main-model outcomes, because `topic_growth` is mechanically derived from
`topic_share_t1` (`log(topic_share_t) - log(topic_share_t1)`).

**Tier semantics** (`constraints.py`): `causallearn`'s `BackgroundKnowledge`
forbids an edge `n1 -> n2` whenever `n1`'s tier number is higher than `n2`'s.
This repo uses tier 0 = exogenous (`year`), tier 1 = t-1 predictors, tier 2 =
t outcomes — giving exactly "no t -> t-1" and "nothing -> year" with no extra
forbidden-pattern rules. When adding a new variable, decide its tier by
whether it's measured at t-1, at t, or is context/exogenous, then add it to
the corresponding list in `constraints.py` — everything downstream
(`data_prep.py`'s `PREDICTORS_T1`/`OUTCOMES`, `pc_learning.py`'s node-name
lists) needs to agree on the same variable name.

**Notebooks** (`nips_pipeline_v4_clean.ipynb`, `nips_analysis_v4_clean.ipynb`)
are the recovered original (pre-refactor) pipeline and analysis, kept for
reference/provenance — new pipeline work happens in `src/`, not the
notebooks.

## Data quality findings that constrain future work

These are established findings from `reports/data_quality*.md`, not just
implementation details — code changes that contradict them need a reason:

- Citation zero-rates rising in recent years is OpenAlex indexing lag, not a
  data bug — confirmed via a 3-year-window comparison and a live API
  spot-check. Do not truncate or exclude recent-year rows because of this.
- `bridge_concentration_t1` is near-degenerate (mass piled at 0/1) — treat as
  effectively binary, unsuited to continuous Fisher-Z.
- `modularity_t1` correlates with topic size — flag any edge touching it as a
  possible size confound.
- Rows are `(topic, year)` panel data, not i.i.d. — PC's CI tests assume
  i.i.d. samples; this is a known limitation addressed empirically by
  bootstrap/subsampling stability analysis (Step 4, not yet in this repo) and
  not fixed at the data-prep stage.
