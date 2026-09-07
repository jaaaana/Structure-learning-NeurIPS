import json
from pathlib import Path

from causallearn.graph.GraphNode import GraphNode
from causallearn.utils.PCUtils.BackgroundKnowledge import BackgroundKnowledge

from constraints_report import render_report

ROOT = Path(__file__).resolve().parent.parent
REPORT_OUT = ROOT / "reports" / "edge_constraints.md"
JSON_OUT = ROOT / "reports" / "edge_constraints.json"

TIER_0 = [
    "topic_share_t1",
    "cross_topic_rate_t1",
    "connectivity_t1",
    "modularity_t1",
    "bridge_concentration_t1",
]

TIER_1 = ["topic_growth", "median_cites_2yr", "hit_rate_2yr", "topic_share_t"]
TIER_1_LOG_VARIANT = "log1p_median_c2"

EXOGENOUS = ["year"]

MAIN_PREDICTORS = ["topic_share_t1", "cross_topic_rate_t1", "connectivity_t1", "modularity_t1"]
MAIN_OUTCOMES = ["topic_share_t", TIER_1_LOG_VARIANT]
SENSITIVITY_PREDICTORS_ONLY = ["bridge_concentration_t1"]
SENSITIVITY_OUTCOMES_ONLY = ["topic_growth", "hit_rate_2yr"]

SIZE_VARS = ["n_papers_t1"]


def allowed_edges() -> list:
    predictor_to_outcome = [(p, o) for p in TIER_0 for o in TIER_1]
    exogenous_to_rest = [(e, v) for e in EXOGENOUS for v in TIER_0 + TIER_1]
    return predictor_to_outcome + exogenous_to_rest


def forbidden_edges() -> list:
    temporal = [(o, p) for o in TIER_1 for p in TIER_0]
    into_exogenous = [(v, e) for v in TIER_0 + TIER_1 for e in EXOGENOUS]
    return temporal + into_exogenous


def sensitivity_edges() -> dict:
    outcome_outcome = [(a, b) for a in TIER_1 for b in TIER_1 if a != b]
    predictor_predictor = [(a, b) for a in TIER_0 for b in TIER_0 if a != b]
    return {
        "outcome_outcome_t": outcome_outcome,
        "predictor_predictor_t1": predictor_predictor,
    }


_TRANSFORM_SUFFIXES = ("_bin", "_log")


def _base_name(name: str) -> str:
    for suffix in _TRANSFORM_SUFFIXES:
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def build_background_knowledge(node_names: list, allow_outcome_outcome: bool = False,
                                allow_predictor_predictor: bool = False,
                                size_vars: list = None) -> BackgroundKnowledge:
    size_vars = size_vars or []
    nodes = {name: GraphNode(name) for name in node_names}
    bk = BackgroundKnowledge()

    exogenous_names = [n for n in node_names if _base_name(n) in EXOGENOUS]
    size_names = [n for n in node_names if _base_name(n) in size_vars]
    tier0_names = [n for n in node_names if _base_name(n) in TIER_0]
    tier1_names = [n for n in node_names if _base_name(n) in TIER_1 or _base_name(n) == TIER_1_LOG_VARIANT]

    predictor_tier = 2 if size_names else 1
    outcome_tier = 3 if size_names else 2

    for name in exogenous_names:
        bk.add_node_to_tier(nodes[name], 0)
    for name in size_names:
        bk.add_node_to_tier(nodes[name], 1)
    for name in tier0_names:
        bk.add_node_to_tier(nodes[name], predictor_tier)
    for name in tier1_names:
        bk.add_node_to_tier(nodes[name], outcome_tier)

    if size_names:
        bk.forbid_within_tier(1)
    if not allow_predictor_predictor:
        bk.forbid_within_tier(predictor_tier)
    if not allow_outcome_outcome:
        bk.forbid_within_tier(outcome_tier)

    return bk


def export_json() -> dict:
    data = {
        "domain_context": {
            "dataset": "NeurIPS topic-year panel",
            "unit_of_analysis": "row = (topic, year)",
            "causal_question": (
                "Does topic-level collaboration structure at t-1 predict "
                "topic growth and early citation impact at t?"
            ),
            "temporal_rule": "t -> t-1 edges forbidden (no edges from the future to the past)",
        },
        "temporal_tiers": {
            "tier_0_exogenous": EXOGENOUS,
            "tier_1_predictors_t1": TIER_0,
            "tier_2_outcomes_t": TIER_1,
        },
        "main_model": {"predictors": MAIN_PREDICTORS, "outcomes": MAIN_OUTCOMES, "exogenous": EXOGENOUS},
        "sensitivity_only": {
            "predictors": SENSITIVITY_PREDICTORS_ONLY,
            "outcomes": SENSITIVITY_OUTCOMES_ONLY,
            "size_control": SIZE_VARS,
        },
        "log_variant_note": (
            f"{TIER_1_LOG_VARIANT} is median_cites_2yr, log1p-transformed for "
            "continuous CI tests -- same tier, same variable, never both in one run."
        ),
        "allowed_edges_main_model": [list(e) for e in allowed_edges()],
        "forbidden_edges": [list(e) for e in forbidden_edges()],
        "sensitivity_edges": {k: [list(e) for e in v] for k, v in sensitivity_edges().items()},
    }
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return data


def main():
    data = export_json()
    report = render_report(data, EXOGENOUS, TIER_0, TIER_1, TIER_1_LOG_VARIANT,
                            MAIN_PREDICTORS, MAIN_OUTCOMES,
                            SENSITIVITY_PREDICTORS_ONLY, SENSITIVITY_OUTCOMES_ONLY,
                            SIZE_VARS)
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUT.write_text(report, encoding="utf-8")

    print(f"Forbidden edges: {len(data['forbidden_edges'])}")
    print(f"Allowed edges (main model): {len(data['allowed_edges_main_model'])}")
    print(f"Sensitivity outcome-outcome edges: {len(data['sensitivity_edges']['outcome_outcome_t'])}")
    print(f"Sensitivity predictor-predictor edges: {len(data['sensitivity_edges']['predictor_predictor_t1'])}")
    print(f"Wrote {JSON_OUT}")
    print(f"Wrote {REPORT_OUT}")


if __name__ == "__main__":
    main()
