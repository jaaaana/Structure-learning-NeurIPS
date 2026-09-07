"""Refresh citation windows and rebuild the topic-year panel.

Adapted from the recovered nips_pipeline_v4_clean.ipynb (last run
2026-03-17), with Colab-specific bits removed and paths pointed at this
project. Reuses the already-matched papers in
data/raw/nips-papers_enriched_openalex.csv (no need to re-run paper
matching or topic assignment -- those don't change over time) and only
refreshes what's genuinely time-sensitive: citation counts.

What changed vs. the original pipeline:
- EXCLUDE_YEAR bumped from 2024 to 2025, so 2024 topic-years are now
  included (2024's 2-year window has closed: 2024+1=2025 < 2026).
- Ghost-row title re-matching (the original pipeline's "Fix loop") is
  provided but not run by default -- 92% of papers already have a resolved
  oa_work_id, and it requires many additional API search calls. Enable via
  RUN_GHOST_FIX = True below if you want to chase the remaining ~8%.

Usage:
    python src/refresh_citations.py
Requires an OpenAlex API key, either via the OPENALEX_API_KEY environment
variable or entered at the prompt.
"""
import getpass
import json
import os
import re
import time
import unicodedata
from datetime import date
from difflib import SequenceMatcher
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
import requests
from networkx.algorithms.community import louvain_communities
from networkx.algorithms.community.quality import modularity as nx_modularity
from scipy.cluster.hierarchy import fcluster, linkage
from scipy.spatial.distance import squareform
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
REPORT_DIR = ROOT / "reports"

PAPERS_IN = RAW_DIR / "nips-papers_enriched_openalex.csv"
PAPERS_FIXED = PROCESSED_DIR / "nips-papers-fixed.csv"
C2_CKPT = PROCESSED_DIR / "nips-c2-checkpoint.csv"
C2_OUT = PROCESSED_DIR / "nips-papers-c2.csv"
TOPIC_MAP_OUT = PROCESSED_DIR / "nips-topic-merge-map.json"
PANEL_OUT = RAW_DIR / "nips-panel-v5-refreshed.csv"
VARDESC_OUT = REPORT_DIR / "nips-variable-descriptions.json"

COMPLETE = {"ok", "ok_fallback", "ok_manual_doi", "ok_refetch"}
EXCLUDE_SRC = {4581, 5987, 5346, 14379, 15556, 18507, 20437}
MIN_CELL_SIZE = 20
MIN_YEAR_SPAN = 7
EXCLUDE_YEAR = 2025  # bumped from 2024 -- its 2-year window has now closed
MERGE_THRESHOLD = 0.50
CURRENT_YEAR = date.today().year
SNAPSHOT = str(date.today())

RUN_GHOST_FIX = False  # set True to re-search OpenAlex for the ~8% of
                        # papers with a complete status but no resolved
                        # oa_work_id. Slower, not required for the core
                        # citation refresh.

SELECT_SLIM = "id,display_name,publication_year,doi,cited_by_count,primary_topic,topics,authorships"


def get_api_key() -> str:
    key = os.environ.get("OPENALEX_API_KEY", "").strip()
    if key:
        return key
    key = getpass.getpass("OpenAlex API key: ").strip()
    assert key, "An OpenAlex API key is required."
    return key


def clean_title(x):
    if not isinstance(x, str):
        return x
    import ftfy
    x = ftfy.fix_text(unicodedata.normalize("NFC", x))
    x = re.sub(r"\$.*?\$|\\[a-zA-Z]+|[{}]", " ", x)
    return re.sub(r"\s+", " ", x).strip()


def title_sim(a, b):
    a = re.sub(r"\s+", " ", str(a).strip().lower())
    b = re.sub(r"\s+", " ", str(b).strip().lower())
    return SequenceMatcher(None, a, b).ratio()


def parse_json_list(x):
    if isinstance(x, list):
        return x
    if pd.isna(x) or x in ("", "[]", None):
        return []
    try:
        x = json.loads(x)
    except Exception:
        return []
    return x if isinstance(x, list) else []


def work_to_fields(work: dict) -> dict:
    pt = work.get("primary_topic") or {}
    auths = work.get("authorships") or []
    ids = [a["author"]["id"] for a in auths if a.get("author", {}).get("id")]
    names = [a["author"].get("display_name") for a in auths if a.get("author", {}).get("id")]
    pos = [a.get("author_position") for a in auths if a.get("author", {}).get("id")]
    topics = [{"id": t.get("id"), "name": t.get("display_name"), "score": t.get("score")}
              for t in (work.get("topics") or [])[:5]]
    return {
        "oa_work_id": work.get("id"),
        "oa_display_name": work.get("display_name"),
        "oa_doi": (work.get("doi") or "").replace("https://doi.org/", ""),
        "oa_cited_by_count": work.get("cited_by_count"),
        "oa_primary_topic": pt.get("display_name"),
        "oa_domain": (pt.get("domain") or {}).get("display_name"),
        "oa_field": (pt.get("field") or {}).get("display_name"),
        "oa_subfield": (pt.get("subfield") or {}).get("display_name"),
        "oa_topics_top5_json": json.dumps(topics, ensure_ascii=False),
        "oa_author_ids_json": json.dumps(ids, ensure_ascii=False),
        "oa_author_names_json": json.dumps(names, ensure_ascii=False),
        "oa_author_positions_json": json.dumps(pos, ensure_ascii=False),
    }


def oa_search(session, api_key, title, year, k=5, sim_min=0.85):
    q = '"' + title.replace("\\", "\\\\").replace('"', '\\"') + '"'
    for filt in [f"title.search:{q},publication_year:{year - 1}|{year}|{year + 1}", f"title.search:{q}"]:
        r = session.get("https://api.openalex.org/works",
                         params={"filter": filt, "per_page": k, "select": SELECT_SLIM, "api_key": api_key},
                         timeout=30)
        if r.status_code == 429:
            raise RuntimeError("Rate limited")
        if r.status_code != 200:
            continue
        res = r.json().get("results") or []
        if not res:
            continue
        best = max(res, key=lambda w: title_sim(title, w.get("display_name", "")))
        sim = title_sim(title, best.get("display_name", ""))
        by = best.get("publication_year")
        if sim >= sim_min and (by is None or abs(int(by) - year) <= 2):
            return best, "ok"
    return None, "no_match"


def fix_ghost_rows(papers: pd.DataFrame, session, api_key) -> pd.DataFrame:
    """Re-search OpenAlex by title for rows marked complete but missing oa_work_id."""
    ghost = papers["oa_status"].isin(COMPLETE) & papers["oa_work_id"].isna()
    todo = papers.index[ghost].tolist()
    print(f"Ghost rows to re-search: {len(todo)}")

    for i, idx in enumerate(todo, 1):
        row = papers.loc[idx]
        title = clean_title(row.get("title", ""))
        if not title or len(title) < 5:
            papers.loc[idx, "oa_status"] = "no_match"
            continue
        work, status = oa_search(session, api_key, title, int(row["year"]))
        if work is None:
            papers.loc[idx, "oa_status"] = status
            continue
        vals = {"oa_status": "ok_refetch", "oa_title_sim": title_sim(title, work.get("display_name", "")),
                **work_to_fields(work)}
        for c, v in vals.items():
            if c in papers.columns:
                papers.loc[idx, c] = v
        if i % 50 == 0:
            papers.to_csv(PAPERS_FIXED, index=False)
            print(i, len(todo))
        time.sleep(0.15)

    ghost = papers["oa_status"].isin(COMPLETE) & papers["oa_work_id"].isna()
    papers.loc[ghost, "oa_status"] = "missing_in_openalex"
    papers["snapshot_date"] = SNAPSHOT
    papers.to_csv(PAPERS_FIXED, index=False)
    return papers


def refresh_windowed_citations(papers: pd.DataFrame, session, api_key) -> pd.DataFrame:
    """Fetch counts_by_year per matched paper and compute c2 (2yr window), c3, c2_complete."""
    matched = papers[papers["oa_status"].isin(COMPLETE) & papers["oa_work_id"].notna()
                      & (papers["year"].astype(int) != EXCLUDE_YEAR)].copy()
    matched["_uri"] = matched["oa_work_id"].str.strip()

    ckpt = pd.read_csv(C2_CKPT) if C2_CKPT.exists() else pd.DataFrame(columns=["oa_work_id", "counts_by_year_json"])
    done = set(ckpt["oa_work_id"].dropna())
    todo = [u for u in matched["_uri"] if u not in done]
    print(f"Papers needing counts_by_year fetch: {len(todo)} (already cached: {len(done)})")

    rows = []
    for b, start in enumerate(range(0, len(todo), 50), 1):
        batch = todo[start:start + 50]
        r = session.get("https://api.openalex.org/works",
                         params={"filter": f'ids.openalex:{"|".join(batch)}', "per_page": len(batch),
                                 "select": "id,counts_by_year", "api_key": api_key},
                         timeout=45)
        if r.status_code == 429:
            raise RuntimeError("Rate limited")
        if r.status_code != 200:
            continue
        got = {x["id"]: x.get("counts_by_year") for x in (r.json().get("results") or [])}
        rows.extend({"oa_work_id": u, "counts_by_year_json": json.dumps(got.get(u), ensure_ascii=False)
                     if got.get(u) is not None else None} for u in batch)
        if b % 50 == 0:
            ckpt = pd.concat([ckpt, pd.DataFrame(rows)], ignore_index=True).drop_duplicates("oa_work_id", keep="last")
            ckpt.to_csv(C2_CKPT, index=False)
            rows = []
            print(f"  batch {b}")
        time.sleep(0.1)

    if rows:
        ckpt = pd.concat([ckpt, pd.DataFrame(rows)], ignore_index=True)
    ckpt = ckpt.drop_duplicates("oa_work_id", keep="last")
    ckpt.to_csv(C2_CKPT, index=False)

    def compute_c2_c3(cby_json, pub_year):
        if pd.isna(cby_json):
            return pd.Series([np.nan, np.nan, False], index=["c2", "c3", "c2_complete"])
        try:
            counts = {x["year"]: x["cited_by_count"] for x in json.loads(cby_json) if isinstance(x, dict)}
        except Exception:
            return pd.Series([np.nan, np.nan, False], index=["c2", "c3", "c2_complete"])
        c2 = counts.get(pub_year, 0) + counts.get(pub_year + 1, 0)
        c3 = c2 + counts.get(pub_year + 2, 0) if CURRENT_YEAR > pub_year + 2 else np.nan
        return pd.Series([c2, c3, CURRENT_YEAR > pub_year + 1], index=["c2", "c3", "c2_complete"])

    matched["_cby"] = matched["_uri"].map(ckpt.drop_duplicates("oa_work_id").set_index("oa_work_id")["counts_by_year_json"])
    matched[["c2", "c3", "c2_complete"]] = matched.apply(lambda r: compute_c2_c3(r["_cby"], int(r["year"])), axis=1)

    papers = papers.merge(matched[["src_index", "c2", "c3", "c2_complete"]], on="src_index", how="left")
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    papers.to_csv(C2_OUT, index=False)
    print(f"Papers with a computed c2: {int(papers['c2'].notna().sum())}")
    return papers


def merge_topics(papers: pd.DataFrame) -> dict:
    df = papers[papers["oa_status"].isin(COMPLETE) & papers["oa_work_id"].notna()
                & (papers["year"].astype(int) != EXCLUDE_YEAR) & (~papers["src_index"].isin(EXCLUDE_SRC))
                & papers["oa_primary_topic"].notna()].copy()
    topics = sorted(df["oa_primary_topic"].str.strip().unique())

    tfidf = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5)).fit_transform(topics)
    dist = np.clip(1 - cosine_similarity(tfidf), 0, None)
    np.fill_diagonal(dist, 0)
    labels = fcluster(linkage(squareform(dist, checks=False), method="average"), t=1 - MERGE_THRESHOLD, criterion="distance")

    counts = df["oa_primary_topic"].str.strip().value_counts()
    clusters = {}
    for topic, label in zip(topics, labels):
        clusters.setdefault(label, []).append(topic)

    merge_map = {}
    for members in clusters.values():
        if len(members) < 2:
            continue
        canon = max(members, key=lambda x: counts.get(x, 0))
        merge_map.update({x: canon for x in members if x != canon})

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    TOPIC_MAP_OUT.write_text(json.dumps(merge_map, indent=2), encoding="utf-8")
    print(f"Distinct raw topics: {len(topics)}, merged into: {len(set(topics) - set(merge_map)) }")
    return merge_map


def gini(x):
    x = np.sort(np.asarray(x, float))
    n = len(x)
    return np.nan if n == 0 or x.sum() == 0 else (2 * np.sum(np.arange(1, n + 1) * x) - (n + 1) * x.sum()) / (n * x.sum())


def make_graph(author_lists):
    G = nx.Graph()
    for ids in author_lists:
        ids = [a for a in ids if isinstance(a, str)]
        G.add_nodes_from(ids)
        for i, a in enumerate(ids):
            for b in ids[i + 1:]:
                if G.has_edge(a, b):
                    G[a][b]["weight"] += 1
                else:
                    G.add_edge(a, b, weight=1)
    return G


def graph_metrics(author_lists):
    G = make_graph(author_lists)
    if len(G) < 3 or G.number_of_edges() == 0:
        return len(G), np.nan, np.nan, np.nan
    deg = float(np.mean([d for _, d in G.degree()]))
    comms = louvain_communities(G, weight="weight", seed=42)
    mod = nx_modularity(G, comms, weight="weight")
    bc = sorted(nx.betweenness_centrality(G, weight="weight").values(), reverse=True)
    k = max(1, int(len(bc) * 0.10))
    bc_share = sum(bc[:k]) / sum(bc) if sum(bc) else 0.0
    return len(G), deg, mod, bc_share


def build_panel(papers: pd.DataFrame, merge_map: dict) -> pd.DataFrame:
    df = papers[papers["oa_status"].isin(COMPLETE) & papers["oa_work_id"].notna()
                & (papers["year"].astype(int) != EXCLUDE_YEAR) & (~papers["src_index"].isin(EXCLUDE_SRC))
                & papers["oa_primary_topic"].notna()].copy()
    df["year"] = df["year"].astype(int)
    df["c2"] = pd.to_numeric(df.get("c2"), errors="coerce")
    df["c3"] = pd.to_numeric(df.get("c3"), errors="coerce")
    df["topic"] = df["oa_primary_topic"].str.strip().map(merge_map).fillna(df["oa_primary_topic"].str.strip())
    df["_authors"] = df["oa_author_ids_json"].apply(parse_json_list)
    df["_topics_top5"] = df["oa_topics_top5_json"].apply(parse_json_list)
    df["_team_size"] = df["_authors"].str.len()

    topic_df = df[df["topic"].notna()].copy()
    yearly_total = df.groupby("year").size()
    c2_base = df[df["c2_complete"].fillna(False)] if "c2_complete" in df else df.iloc[0:0]
    yr_p90 = c2_base.groupby("year")["c2"].quantile(0.90) if len(c2_base) else pd.Series(dtype=float)

    at = pd.DataFrame(
        [{"aid": aid, "year": y, "topic": t} for y, t, ids in topic_df[["year", "topic", "_authors"]].itertuples(index=False) for aid in ids if isinstance(aid, str)],
        columns=["aid", "year", "topic"],
    ).drop_duplicates()
    cross = at.groupby(["aid", "year"])["topic"].nunique().ge(2).rename("cross").reset_index()
    at = at.merge(cross, on=["aid", "year"], how="left")

    rows = []
    for (year, topic), cell in topic_df.groupby(["year", "topic"], sort=True):
        cross_r = at[(at["year"] == year) & (at["topic"] == topic)].drop_duplicates("aid")["cross"].mean()
        n_nodes, mean_deg, mod, bc_share = graph_metrics(cell["_authors"])
        cell_c = cell[cell["c2_complete"].fillna(False)] if "c2_complete" in cell else cell.iloc[0:0]
        c2v = cell_c["c2"].dropna().to_numpy()
        c3v = cell_c["c3"].dropna().to_numpy()
        p90 = yr_p90.get(year, np.nan)
        rows.append({
            "topic": topic, "year": year,
            "n_papers": len(cell), "n_authors": n_nodes,
            "topic_share": len(cell) / yearly_total.get(year, 1),
            "cross_topic_rate": float(cross_r) if pd.notna(cross_r) else np.nan,
            "connectivity": mean_deg, "modularity": mod, "bridge_concentration": bc_share,
            "median_cites_2yr": float(np.median(c2v)) if len(c2v) else np.nan,
            "hit_rate_2yr": float((c2v >= p90).mean()) if len(c2v) and pd.notna(p90) else np.nan,
            "avg_team_size": float(cell["_team_size"].mean()),
            "median_cites_3yr": float(np.median(c3v)) if len(c3v) else np.nan,
            "citation_gini": gini(c2v) if len(c2v) >= 3 else np.nan,
        })

    panel = pd.DataFrame(rows).sort_values(["topic", "year"]).reset_index(drop=True)
    panel["topic_growth"] = np.log(panel["topic_share"] + 1e-4) - np.log(panel.groupby("topic")["topic_share"].shift(1) + 1e-4)
    panel["log1p_median_c2"] = np.log1p(panel["median_cites_2yr"])

    # n_papers/n_authors lagged the same way as the other _t1 predictors (from
    # the full pre-filter panel, before the MIN_CELL_SIZE/MIN_YEAR_SPAN cut
    # below) so n_papers_t1 reflects the true t-1 cell size, not just whichever
    # predecessor cells happened to survive the current-year filter. Added per
    # the 2026-08-19 correction: network predictors are from t-1,
    # so the minimum-graph-size condition must be checked on that graph, not
    # on n_papers at t.
    lag_cols = ["topic_share", "cross_topic_rate", "connectivity", "modularity", "bridge_concentration",
                "n_papers", "n_authors"]
    lag = panel[["topic", "year"] + lag_cols].rename(columns={c: f"{c}_t1" for c in lag_cols})
    lag["year"] += 1
    panel = panel.merge(lag, on=["topic", "year"], how="inner")

    keep_topics = panel.groupby("topic")["year"].nunique().ge(MIN_YEAR_SPAN)
    panel = panel[panel["topic"].isin(keep_topics[keep_topics].index) & panel["n_papers"].ge(MIN_CELL_SIZE)].copy()

    out_cols = [
        "topic", "year", "n_papers", "n_authors", "n_papers_t1", "n_authors_t1",
        "topic_share_t1", "cross_topic_rate_t1", "connectivity_t1", "modularity_t1", "bridge_concentration_t1",
        "topic_growth", "median_cites_2yr", "log1p_median_c2", "hit_rate_2yr",
        "topic_share", "cross_topic_rate", "connectivity", "modularity", "bridge_concentration",
        "avg_team_size", "median_cites_3yr", "citation_gini",
    ]
    out = panel[[c for c in out_cols if c in panel.columns]].sort_values(["topic", "year"]).reset_index(drop=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    out.to_csv(PANEL_OUT, index=False)

    core = ["topic_share_t1", "cross_topic_rate_t1", "connectivity_t1", "modularity_t1", "bridge_concentration_t1",
            "topic_growth", "median_cites_2yr", "hit_rate_2yr"]
    print(f"Panel shape: {out.shape}, complete core rows: {int(out[core].notna().all(axis=1).sum())}")
    return out


def main():
    api_key = get_api_key()
    session = requests.Session()

    print(f"{SNAPSHOT} | exclude_year={EXCLUDE_YEAR} | min_cell={MIN_CELL_SIZE} | min_years={MIN_YEAR_SPAN}")

    papers = pd.read_csv(PAPERS_FIXED if PAPERS_FIXED.exists() else PAPERS_IN)

    if RUN_GHOST_FIX:
        papers = fix_ghost_rows(papers, session, api_key)

    papers = refresh_windowed_citations(papers, session, api_key)
    merge_map = merge_topics(papers)
    panel = build_panel(papers, merge_map)

    print(f"\nWrote refreshed panel -> {PANEL_OUT}")
    print("Compare against data/raw/nips-panel-v4.csv before adopting it as the new Step 1 input.")


if __name__ == "__main__":
    main()
