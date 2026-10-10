import sys
from pathlib import Path as _Path
_SRC_ROOT = str(_Path(__file__).resolve().parents[1])
if _SRC_ROOT not in sys.path:
    sys.path.insert(0, _SRC_ROOT)
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path

import numpy as np

from pc.bootstrap_stability import resample_topics, _is_degenerate
from golem.learning import (add_optimizer_arguments, config_from_args, graph_result,
                            model_nodes, panel_fingerprint, paths, write_json)
from golem.model import FitConfig, fit_many, vocabulary
from pc.learning import load_continuous, load_discretized


def implementation_fingerprint():
    root = Path(__file__).resolve().parents[1]
    names = ["golem/model.py", "golem/learning.py", "golem/bootstrap_stability.py",
             "golem/predictive_usefulness.py", "pc/learning.py", "pc/bootstrap_stability.py",
             "constraints.py"]
    return hashlib.sha256(b"".join((root / n).read_bytes() for n in names)).hexdigest()


def diagnostics(records, requested):
    counts = {s: sum(r["status"] == s for r in records) for s in
              ("converged", "failed", "nonconverged", "degenerate")}
    row_counts = [r["n_rows"] for r in records]
    return {"n_boot_requested": requested, "n_completed": len(records),
            "n_succeeded": counts["converged"], "n_failed": counts["failed"],
            "n_nonconverged": counts["nonconverged"], "n_degenerate_skipped": counts["degenerate"],
            "row_counts_min": min(row_counts) if row_counts else None,
            "row_counts_mean": float(np.mean(row_counts)) if row_counts else None,
            "row_counts_max": max(row_counts) if row_counts else None}


def run_bootstrap(df, names, representation, n_boot=500, seed=0, config=FitConfig(),
                  threshold=0.10, batch_size=50, existing=None, save=None,
                  constrained=True):
    if n_boot < 1 or batch_size < 1:
        raise ValueError("n_boot and batch_size must be positive")
    config.validate()
    if not np.isfinite(threshold) or threshold < 0:
        raise ValueError("threshold must be finite and nonnegative")
    records = list(existing or [])
    if [r["replicate"] for r in records] != list(range(len(records))) or len(records) > n_boot:
        raise ValueError("Checkpoint replicate sequence does not match request")
    groups = {t: g for t, g in df.groupby("topic")}
    topics = df["topic"].unique()
    rng = np.random.default_rng(seed)
    categories = vocabulary(df, names) if representation == "discretized" else None
    # Advance the same RNG sequence, including degenerate/failed draws, on resume.
    for _ in records:
        rng.choice(topics, size=len(topics), replace=True)
    for start in range(len(records), n_boot, batch_size):
        pending, frames, valid_positions = [], [], []
        for replicate in range(start, min(start + batch_size, n_boot)):
            frame = resample_topics(groups, topics, rng)
            base = {"replicate": replicate, "n_rows": len(frame), "representation": representation}
            if _is_degenerate(frame, names):
                pending.append(dict(base, status="degenerate", failure_reason="A node has fewer than two distinct values"))
            else:
                valid_positions.append(len(pending))
                pending.append(base)
                frames.append(frame)
        if frames:
            try:
                fits = fit_many(frames, names, representation, constrained, config, categories)
            except (ValueError, RuntimeError, FloatingPointError, np.linalg.LinAlgError):
                # Isolate failures rather than losing all otherwise valid batch members.
                fits = []
                for frame in frames:
                    try:
                        fits.append(fit_many([frame], names, representation, constrained, config, categories)[0])
                    except (ValueError, RuntimeError, FloatingPointError, np.linalg.LinAlgError) as exc:
                        fits.append({"status": "failed", "strengths": None, "failure_reason": str(exc)})
            for pos, fit in zip(valid_positions, fits):
                pending[pos].update(graph_result(fit, threshold))
        records.extend(pending)
        if save is not None:
            save(records)
        diag = diagnostics(records, n_boot)
        print(f"{representation}: {len(records)}/{n_boot}; converged={diag['n_succeeded']}, "
              f"nonconverged={diag['n_nonconverged']}, failed={diag['n_failed']}", flush=True)
    return records, diagnostics(records, n_boot)


def main():
    from golem.bootstrap_stability_report import render_report
    parser = argparse.ArgumentParser(description=__doc__)
    add_optimizer_arguments(parser)
    parser.add_argument("--n-boot", type=int, default=500)
    parser.add_argument("--lambda1", type=float, default=0.02)
    parser.add_argument("--threshold", type=float, default=0.10)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--resume", action="store_true", help="Resume only an exactly matching checkpoint")
    args = parser.parse_args()
    config = config_from_args(args, args.lambda1)
    config.validate()
    panels = {"continuous": load_continuous(args.version), "discretized": load_discretized(args.version)}
    metadata = {"version": args.version, "seed": args.seed, "n_boot": args.n_boot,
                "config": asdict(config), "threshold": args.threshold,
                "continuous_unconstrained": True,
                "implementation_fingerprint": implementation_fingerprint(),
                "input_fingerprints": {k: panel_fingerprint(v) for k, v in panels.items()}}
    report, out = paths(args.version, bootstrap=True)
    payload = {"metadata": metadata, "continuous": [], "discretized": [],
               "continuous_unconstrained": []}
    if args.resume and out.exists():
        saved = json.loads(out.read_text(encoding="utf-8"))
        old_meta = saved.get("metadata", {})
        # Older checkpoints contain both constrained representations but not
        # the unconstrained direction-provenance run. Reuse them only when the
        # data and fit settings match exactly; the new unconstrained run is
        # then appended to those same bootstrap draws.
        comparable = ("version", "seed", "n_boot", "config", "threshold", "input_fingerprints")
        if any(old_meta.get(key) != metadata.get(key) for key in comparable):
            raise ValueError("Checkpoint configuration, inputs, or implementation changed; run without --resume to restart")
        if old_meta.get("implementation_fingerprint") != metadata["implementation_fingerprint"] \
                and saved.get("continuous_unconstrained"):
            raise ValueError("Checkpoint implementation changed after the unconstrained run; run without --resume")
        payload = {**saved, "metadata": metadata,
                   "continuous_unconstrained": saved.get("continuous_unconstrained", [])}
    for representation, df in panels.items():
        if len(payload.get(representation, [])) == args.n_boot:
            continue
        def save(records):
            payload[representation] = records
            payload[f"{representation}_diagnostics"] = diagnostics(records, args.n_boot)
            write_json(out, payload)
        records, diag = run_bootstrap(df, model_nodes(representation), representation,
                                     args.n_boot, args.seed, config, args.threshold,
                                     args.batch_size, payload[representation], save)
        payload[representation] = records
        payload[f"{representation}_diagnostics"] = diag
        write_json(out, payload)
    # Reset the RNG so unconstrained fits pair with continuous constrained
    # fits on the identical topic-block draws.
    def save_unconstrained(records):
        payload["continuous_unconstrained"] = records
        payload["continuous_unconstrained_diagnostics"] = diagnostics(records, args.n_boot)
        write_json(out, payload)
    unc_records, unc_diag = run_bootstrap(
        panels["continuous"], model_nodes("continuous"), "continuous", args.n_boot,
        args.seed, config, args.threshold, args.batch_size,
        payload.get("continuous_unconstrained", []), save_unconstrained,
        constrained=False,
    )
    payload["continuous_unconstrained"] = unc_records
    payload["continuous_unconstrained_diagnostics"] = unc_diag
    write_json(out, payload)
    report.write_text(render_report(args.version, payload), encoding="utf-8")
    print(f"[{args.version}] continuous unconstrained: "
          f"{unc_diag['n_succeeded']}/{args.n_boot} converged", flush=True)
    print(f"Wrote {report}", flush=True)


if __name__ == "__main__":
    main()
