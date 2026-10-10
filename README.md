# NeurIPS topic-year causal structure learning

Master's thesis pipeline: PC-algorithm structure learning over a NeurIPS
topic-year panel, asking whether a topic's collaboration-graph structure at
year `t-1` predicts that topic's growth and early citation impact at year
`t`. See `CLAUDE.md` for the full architecture writeup; this file only
covers reproducibility.

## Frozen version

**V5 is the final, frozen dataset** (`data/raw/nips-panel-v5-refreshed.csv`).
Every script's `--version` flag now defaults to `v5`. V4 is kept only as a
superseded comparison point (e.g. in `reports/*_v4` outputs that predate the
V5 refresh) -- do not do new work against it. No further dataset changes
without a concrete, unfixable-otherwise reason (per the 2026-08-19
correction).

## Setup

```bash
pip install -r requirements.txt
```

No `pyproject.toml`; the checked-in `.venv` is intentionally empty.
`requirements.txt` is pinned to the exact versions this pipeline was run
and frozen with (Python 3.10.12).

## Run order

From the repo root, in order -- each step reads the previous step's output:

```bash
python src/data_prep.py              # Step 1: data quality report + continuous/discretized tables
python src/constraints.py            # Step 2: temporal edge constraints (shared by v4/v5, not versioned)
python src/pc/learning.py            # Step 3: PC algorithm settings grid
python src/pc/bootstrap_stability.py # Step 4: topic-block bootstrap stability (500 replicates)
python src/pc/predictive_usefulness.py # Step 5a: baseline vs. graph-selected predictive evaluation
python src/final_graph.py            # Step 5b: final tiered graph + team deliverable
```

GOLEM comparison reports use parallel scripts and report generators:

```bash
python src/golem/learning.py                         # settings grid + report
python src/golem/learning_report.py                  # render settings report from saved fits
python src/golem/bootstrap_stability.py              # 500 topic-block replicates + report
python src/golem/predictive_usefulness.py             # nested five-fold evaluation + report
python src/golem/bootstrap_stability_report.py        # regenerate bootstrap report from saved JSON
python src/golem/predictive_usefulness_report.py      # regenerate predictive report from saved JSON
```

The GOLEM optimizer uses a relative objective tolerance of `1e-6` and a
10,000-iteration limit by default.

`src/refresh_citations.py` only needs to be rerun if the raw citation panel
itself must be regenerated from OpenAlex -- **not needed for the thesis now**
that V5 is frozen. See the caveat below before ever rerunning it.

## Seeds, thresholds, and settings

Kept as explicit, named constants rather than buried magic numbers, so a
rerun is reproducible and every reported number is traceable to one spot in
the code:

| Constant | Value | File | What it controls |
|---|---|---|---|
| `--seed` | `0` | `bootstrap_stability.py` | topic-block resampling for the 500-replicate bootstrap (continuous, discretized, and unconstrained) |
| `NESTED_SEED` | `0` (-> per-fold seeds `0..4`) | `predictive_usefulness.py` | the nested, training-fold-only predictor-selection bootstrap; now also written into `predictive_usefulness{_v}.md` and `predictive_nested_cv{_v}.json`, not just the source |
| `LOUVAIN_SEED` | `42` | `refresh_citations.py` | Louvain community detection inside `graph_metrics`, which determines `modularity_t1` -- the one seed that affects the frozen dataset itself, not just a stability add-on |
| `ALPHAS` | `[0.01, 0.05, 0.10]` | `src/pc/learning.py` | PC algorithm significance grid |
| `GRAPH_PARENT_THRESHOLD` | `0.5` | `predictive_usefulness.py` | per-fold predictor-selection adjacency cutoff (nested CV) |
| `SELECTION_THRESHOLD` | `0.5` | `src/golem/predictive_usefulness.py` | per-fold GOLEM parent-selection frequency cutoff (nested CV) |
| `STABLE_THRESHOLD` / `CANDIDATE_THRESHOLD` / `GAP_THRESHOLD` | `0.7` / `0.3` / `0.3` | `final_graph.py` | bootstrap-adjacency tier classification (descriptive buckets, not significance -- see `final_team_deliverable*.md`) |

These two threshold sets are deliberately different numbers for different
purposes (predictor selection vs. tier classification) -- see
`predictive_usefulness*.md` and `final_team_deliverable*.md` for why they
are not meant to be compared to each other.

## `refresh_citations.py` cache caveat

This script checkpoints OpenAlex citation pulls to
`data/processed/nips-c2-checkpoint.csv` so interrupted/rerun pulls don't
re-fetch rows already retrieved. There is **no `--force-refresh` flag**: for
a genuinely new OpenAlex snapshot (not just resuming an interrupted pull),
the checkpoint file must be deleted manually first, or it will silently
reuse the stale cached rows instead of re-querying the API. Not relevant for
the thesis right now -- citations are frozen at the V5 snapshot and should
not be refreshed again (per the 2026-08-19 correction).
