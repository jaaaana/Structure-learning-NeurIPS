import sys
from pathlib import Path as _Path
_SRC_ROOT = str(_Path(__file__).resolve().parents[1])
if _SRC_ROOT not in sys.path:
    sys.path.insert(0, _SRC_ROOT)
import argparse
import json

from constraints import TIER_0, TIER_1, TIER_1_LOG_VARIANT, _base_name
from data_prep import DATASETS
from golem.learning import edge_recurrence, paths
from golem.learning_report import recurrence_text, table


def direction_provenance(constrained, unconstrained):
    """Compare GOLEM directions on the same successful bootstrap draws."""
    c_ok = {r["replicate"]: r for r in constrained if r["status"] == "converged"}
    u_ok = {r["replicate"]: r for r in unconstrained if r["status"] == "converged"}
    paired_ids = sorted(set(c_ok) & set(u_ok))
    constrained_dirs, constrained_adj = {}, {}
    for rep in paired_ids:
        r = c_ok[rep]
        for src, dst in r.get("directed_edges", []):
            a, b = _base_name(src), _base_name(dst)
            pair = tuple(sorted((a, b)))
            state = constrained_dirs.setdefault(pair, {"ab": 0, "ba": 0})
            state["ab" if (a, b) == pair else "ba"] += 1
            constrained_adj[pair] = constrained_adj.get(pair, 0) + 1
        for src, dst in r.get("undirected_edges", []):
            pair = tuple(sorted((_base_name(src), _base_name(dst))))
            constrained_adj[pair] = constrained_adj.get(pair, 0) + 1

    rows = []
    for pair, n_adj in constrained_adj.items():
        d = constrained_dirs.get(pair, {"ab": 0, "ba": 0})
        if d["ab"] == d["ba"]:
            continue
        expected = "ab" if d["ab"] > d["ba"] else "ba"
        same = reverse = undirected = adjacent = 0
        for rep in paired_ids:
            r = u_ok[rep]
            found = None
            for src, dst in r.get("directed_edges", []):
                a, b = _base_name(src), _base_name(dst)
                if tuple(sorted((a, b))) == pair:
                    found = "ab" if (a, b) == pair else "ba"
                    break
            if found is None:
                for src, dst in r.get("undirected_edges", []):
                    if tuple(sorted((_base_name(src), _base_name(dst)))) == pair:
                        found = "undirected"
                        break
            if found is not None:
                adjacent += 1
                if found == expected:
                    same += 1
                elif found == "undirected":
                    undirected += 1
                else:
                    reverse += 1
        rows.append({
            "a": pair[0], "b": pair[1],
            "constrained_adjacency_rate": n_adj / len(paired_ids) if paired_ids else 0.0,
            "constrained_direction": f"{pair[0]} -> {pair[1]}" if expected == "ab" else f"{pair[1]} -> {pair[0]}",
            "unconstrained_adjacency_rate": adjacent / len(paired_ids) if paired_ids else 0.0,
            "same_direction_rate": same / adjacent if adjacent else 0.0,
            "reverse_direction_rate": reverse / adjacent if adjacent else 0.0,
            "undirected_rate": undirected / adjacent if adjacent else 0.0,
        })
    return sorted(rows, key=lambda r: -r["constrained_adjacency_rate"])


def relaxed_tier_recurrence(unconstrained):
    """Return bootstrap recurrence for edges unavailable under the tier bans."""
    tier_sets = [set(TIER_0), set(TIER_1) | {TIER_1_LOG_VARIANT}]
    table = edge_recurrence([r for r in unconstrained if r["status"] == "converged"])
    if table.empty:
        return table
    return table[[
        not any(row.a in tier and row.b in tier for tier in tier_sets)
        for row in table.itertuples(index=False)
    ]]


def render_report(version, payload):
    meta = payload["metadata"]
    cfg = meta["config"]
    lines = [f"# GOLEM Bootstrap Stability ({version})\n",
             f"Topic-block bootstrap: seed={meta['seed']}, requested B={meta['n_boot']} per run. "
             f"Constrained continuous and discretized fits, plus paired unconstrained continuous refits. "
             f"lambda1={cfg['lambda1']}, lambda_dag={cfg['lambda_dag']}, "
             f"learning_rate={cfg['learning_rate']}, edge threshold={meta['threshold']}, "
             f"tolerance={cfg['tolerance']}, max_iter={cfg['max_iter']}.\n",
             recurrence_text()]
    for representation in ("continuous", "discretized"):
        records = payload[representation]
        successful = [r for r in records if r["status"] == "converged"]
        lines += [f"## {representation} representation\n", table([payload[f"{representation}_diagnostics"]]),
                  "Frequencies use converged replicates, including empty graphs; nonconverged fits are excluded.\n",
                  table(edge_recurrence(successful))]
    unconstrained = payload.get("continuous_unconstrained")
    if unconstrained is not None:
        representation = "continuous"
        constrained = payload.get(representation, [])
        paired_n = len({r["replicate"] for r in constrained if r["status"] == "converged"}
                       & {r["replicate"] for r in unconstrained if r["status"] == "converged"})
        lines += ["## Direction provenance (continuous, paired unconstrained refits)\n",
                  "Same topic-block draws refit without constraints. Direction rates use successful paired "
                  "fits; same/reverse/undirected rates are conditional on unconstrained adjacency.\n",
                  f"Common successful replicate IDs: {paired_n}. Requested unconstrained replicates: "
                  f"{len(unconstrained)}; converged: "
                  f"{sum(r['status'] == 'converged' for r in unconstrained)}.\n"]
        lines.append(table(direction_provenance(constrained, unconstrained)) if paired_n
                     else "No paired fits converged in both constraint modes; direction corroboration is unavailable.\n")
        lines += ["## Edges only visible with tier restrictions relaxed\n",
                  "Same-tier edge recurrence in the unconstrained bootstrap.\n",
                  table(relaxed_tier_recurrence(unconstrained))]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", choices=list(DATASETS), default="v5")
    args = parser.parse_args()
    report, source = paths(args.version, bootstrap=True)
    payload = json.loads(source.read_text(encoding="utf-8"))
    report.write_text(render_report(args.version, payload), encoding="utf-8")
    print(f"Wrote {report}")


if __name__ == "__main__":
    main()
