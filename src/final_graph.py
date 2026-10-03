import argparse
import json
from pathlib import Path

from constraints import (
    EXOGENOUS,
    MAIN_OUTCOMES,
    MAIN_PREDICTORS,
    TIER_1,
    TIER_1_LOG_VARIANT,
    _base_name,
)
from data_prep import DATASETS
from final_graph_report import render_report
from pc_learning import CONNECTIVITY_LOG_VARIANT, _canon_pair, edge_recurrence, orientation_provenance

ROOT = Path(__file__).resolve().parent.parent

STABLE_THRESHOLD = 0.7
CANDIDATE_THRESHOLD = 0.3
GAP_THRESHOLD = 0.3

SIZE_CONFOUND_SOURCES = {"modularity_t1"}
EXCLUDED_VARS = {"bridge_concentration_t1"}

_OUTCOME_NAMES = set(TIER_1) | {TIER_1_LOG_VARIANT}


def _suffix(version: str) -> str:
    return "" if version == "v4" else f"_{version}"


def _bootstrap_runs_path(version: str) -> Path:
    return ROOT / "reports" / "pc_runs" / f"bootstrap_runs{_suffix(version)}.json"


def _pc_runs_path(version: str) -> Path:
    return ROOT / "reports" / "pc_runs" / f"pc_runs{_suffix(version)}.json"


def _predictive_nested_cv_path(version: str) -> Path:
    return ROOT / "reports" / "pc_runs" / f"predictive_nested_cv{_suffix(version)}.json"


def _report_out(version: str) -> Path:
    return ROOT / "reports" / f"final_team_deliverable{_suffix(version)}.md"


def _json_out(version: str) -> Path:
    return ROOT / "reports" / f"final_graph{_suffix(version)}.json"


def is_excluded(frm: str, to: str) -> bool:
    return frm in EXCLUDED_VARS or to in EXCLUDED_VARS


def is_size_confound(frm: str, to: str) -> bool:
    return frm in SIZE_CONFOUND_SOURCES and to in _OUTCOME_NAMES


def classify_rate(mean_rate: float, gap: float) -> str:
    if gap > GAP_THRESHOLD:
        return "ambiguous"
    if mean_rate >= STABLE_THRESHOLD:
        return "stable"
    if mean_rate >= CANDIDATE_THRESHOLD:
        return "candidate"
    return "weak"


def build_classification(version: str) -> list:
    data = json.loads(_bootstrap_runs_path(version).read_text(encoding="utf-8"))
    cont_freq = edge_recurrence(data["continuous"]).set_index(["from", "to"])["adjacency_rate"]
    disc_freq = edge_recurrence(data["discretized"]).set_index(["from", "to"])["adjacency_rate"]

    pairs = set(cont_freq.index) | set(disc_freq.index)
    rows = []
    for frm, to in pairs:
        cont_rate = float(cont_freq.get((frm, to), 0.0))
        disc_rate = float(disc_freq.get((frm, to), 0.0))
        mean_rate = (cont_rate + disc_rate) / 2
        gap = abs(cont_rate - disc_rate)
        tier = "excluded" if is_excluded(frm, to) else classify_rate(mean_rate, gap)
        rows.append({
            "from": frm, "to": to,
            "continuous_rate": round(cont_rate, 3), "discretized_rate": round(disc_rate, 3),
            "mean_rate": round(mean_rate, 3), "gap": round(gap, 3),
            "tier": tier,
            "size_confound_flag": is_size_confound(frm, to),
        })
    rows.sort(key=lambda r: r["mean_rate"], reverse=True)
    return rows


def load_main_graph(version: str) -> dict:
    runs = json.loads(_pc_runs_path(version).read_text(encoding="utf-8"))
    for r in runs:
        if (r.get("group") == "main" and r["representation"] == "continuous"
                and r["indep_test"] == "fisherz" and r["alpha"] == 0.05 and r["constrained"]):
            return r
    raise ValueError(f"Frozen main setting not found in {_pc_runs_path(version)}")


def orientation_provenance_lookup(version: str) -> dict:
    data = json.loads(_bootstrap_runs_path(version).read_text(encoding="utf-8"))
    unc_results = data.get("continuous_unconstrained", [])
    cross = orientation_provenance(unc_results)["cross_tier"]
    if len(cross) == 0:
        return {}
    return cross.set_index(["from", "to"])["same_direction_rate"].to_dict()


def annotate_main_graph(main_graph: dict, classification: list, orientation_lookup: dict) -> list:
    by_pair = {(r["from"], r["to"]): r for r in classification}
    annotated = []
    for src, dst in main_graph["directed_edges"]:
        pair = _canon_pair(_base_name(src), _base_name(dst))
        row = by_pair.get(pair)
        annotated.append({
            "src": src, "dst": dst,
            "tier": row["tier"] if row else "unclassified (not seen in bootstrap)",
            "mean_rate": row["mean_rate"] if row else None,
            "same_direction_rate": orientation_lookup.get(pair),
            "size_confound_flag": is_size_confound(pair[0], pair[1]),
        })
    return annotated


def predictive_usefulness_summary(version: str) -> dict:
    path = _predictive_nested_cv_path(version)
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found -- run `python src/predictive_usefulness.py "
            f"--version {version}` first."
        )
    return json.loads(path.read_text(encoding="utf-8"))


def export_json(version: str, classification: list, main_graph: dict, annotated_main: list) -> dict:
    data = {
        "version": version,
        "thresholds": {"stable": STABLE_THRESHOLD, "candidate": CANDIDATE_THRESHOLD, "gap": GAP_THRESHOLD},
        "main_graph": {
            "setting": {"representation": "continuous", "indep_test": "fisherz", "alpha": 0.05, "constrained": True},
            "edges": annotated_main,
        },
        "tiers": {
            tier: [{k: r[k] for k in ("from", "to", "continuous_rate", "discretized_rate", "mean_rate", "gap",
                                       "size_confound_flag")}
                   for r in classification if r["tier"] == tier]
            for tier in ["stable", "candidate", "ambiguous", "excluded", "weak"]
        },
    }
    out = _json_out(version)
    out.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data


def main(version: str = "v5"):
    classification = build_classification(version)
    main_graph = load_main_graph(version)
    orientation_lookup = orientation_provenance_lookup(version)
    annotated_main = annotate_main_graph(main_graph, classification, orientation_lookup)
    pred_usefulness = predictive_usefulness_summary(version)

    report = render_report(version, classification, main_graph, annotated_main, pred_usefulness,
                            STABLE_THRESHOLD, CANDIDATE_THRESHOLD, GAP_THRESHOLD,
                            SIZE_CONFOUND_SOURCES, _suffix(version))
    report_out = _report_out(version)
    report_out.write_text(report, encoding="utf-8")

    json_data = export_json(version, classification, main_graph, annotated_main)
    json_out = _json_out(version)

    counts = {t: len(json_data["tiers"][t]) for t in json_data["tiers"]}
    print(f"[{version}] tiers: {counts}")
    print(f"Wrote {report_out}")
    print(f"Wrote {json_out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", choices=list(DATASETS.keys()), default="v5")
    args = parser.parse_args()
    main(args.version)
