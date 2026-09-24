import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path

import numpy as np

from pc_bootstrap_stability import resample_topics, _is_degenerate
from golem_learning import (add_optimizer_arguments, config_from_args, graph_result,
                            load_pc, model_nodes, panel_fingerprint, paths, write_json)
from golem_model import FitConfig, fit_many, vocabulary
from pc_learning import load_continuous, load_discretized


def implementation_fingerprint():
    root = Path(__file__).parent
    names = ["golem_model.py", "golem_learning.py", "golem_bootstrap_stability.py",
             "pc_learning.py", "bootstrap_stability.py", "constraints.py"]
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
                  threshold=0.10, batch_size=50, existing=None, save=None):
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
                fits = fit_many(frames, names, representation, True, config, categories)
            except (ValueError, RuntimeError, FloatingPointError, np.linalg.LinAlgError):
                # Isolate failures rather than losing all otherwise valid batch members.
                fits = []
                for frame in frames:
                    try:
                        fits.append(fit_many([frame], names, representation, True, config, categories)[0])
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
    from golem_bootstrap_stability_report import render_report
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
                "implementation_fingerprint": implementation_fingerprint(),
                "input_fingerprints": {k: panel_fingerprint(v) for k, v in panels.items()}}
    report, out = paths(args.version, bootstrap=True)
    payload = {"metadata": metadata, "continuous": [], "discretized": []}
    if args.resume and out.exists():
        payload = json.loads(out.read_text(encoding="utf-8"))
        if payload.get("metadata") != metadata:
            raise ValueError("Checkpoint configuration, inputs, or implementation changed; run without --resume to restart")
    for representation, df in panels.items():
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
    pc, note = load_pc(args.version, bootstrap=True)
    report.write_text(render_report(args.version, payload, pc, note), encoding="utf-8")
    print(f"Wrote {report}", flush=True)


if __name__ == "__main__":
    main()
