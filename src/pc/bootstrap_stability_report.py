import sys
from pathlib import Path as _Path
_SRC_ROOT = str(_Path(__file__).resolve().parents[1])
if _SRC_ROOT not in sys.path:
    sys.path.insert(0, _SRC_ROOT)
def render_report(version: str, seed: int, n_boot: int, boot_alpha: float,
                   cont_diag: dict, cont_freq, disc_diag: dict, disc_freq,
                   unc_diag: dict, provenance: dict) -> str:
    suffix = "" if version == "v4" else f"_{version}"
    lines = []
    lines.append(f"# Bootstrap Stability Analysis -- Step 4 ({version})\n")
    lines.append(
        f"Topic-level block bootstrap (seed={seed}, requested B={n_boot}) at the "
        f"frozen main-model setting (alpha={boot_alpha}, constrained, temporal + "
        "exogenous-year background knowledge applied). Each replicate resamples "
        "topics (not rows) with replacement and keeps every row of each sampled "
        "topic, per the 2026-08-19 correction: rows are repeated "
        "topic-year measurements, so plain row-level bootstrap would treat a "
        "topic's own yearly observations as independent draws. This is a "
        f"separate sensitivity axis from `reports/pc/settings_comparison{suffix}.md`'s "
        "alpha/representation grid -- that grid holds the sample fixed and "
        "varies settings; this analysis holds settings fixed and varies the "
        "sample.\n"
    )

    lines.append(
        "**Orientation-stability caveat**: in every table below, "
        "`orientation_rate_given_adjacent` is computed under the constrained "
        "(temporal background knowledge) setting. Under this pipeline's tier "
        "structure, every edge that can appear at all is between two "
        "different tiers, and `causal-learn` forcibly directs any such edge "
        "immediately after skeleton discovery -- before its own v-structure "
        "or Meek orientation rules ever run. So `orientation_rate_given_adjacent` "
        "here is mechanical (it reflects the constraint being applied, not an "
        "independent PC finding); `adjacency_rate` -- not orientation rate -- "
        "is the actual stability evidence (it is also the only quantity "
        "`final_graph.py`'s stable/candidate/ambiguous tiering ever reads). "
        "`same_direction_rate` is only informative for same-tier pairs (two "
        "predictors or two outcomes, where background knowledge doesn't force "
        "a direction either way): it reports whether replicates that did "
        "orient the pair agreed on *which* direction, so a pair that's "
        "oriented often but flips between A->B and B->A across replicates "
        "shows up as high `orientation_rate_given_adjacent` but low "
        "`same_direction_rate` -- a materially weaker finding than a "
        "consistently-oriented pair. See 'Orientation provenance' below for "
        "genuine, unconstrained-derived orientation evidence.\n"
    )

    for label, diag, freq in [
        ("continuous / Fisher-Z", cont_diag, cont_freq),
        ("discretized / chi-square", disc_diag, disc_freq),
    ]:
        lines.append(f"## {label}\n")
        lines.append(
            f"- Requested: {diag['n_boot_requested']} replicates. "
            f"Succeeded: {diag['n_succeeded']}. "
            f"Skipped (degenerate resample, a node had fewer than 2 distinct "
            f"values): {diag['n_degenerate_skipped']}. "
            f"Failed (PC raised an exception): {diag['n_failed']}."
        )
        if diag["row_counts_min"] is not None:
            lines.append(
                f"- Resampled row count per replicate: min={diag['row_counts_min']}, "
                f"mean={diag['row_counts_mean']:.1f}, max={diag['row_counts_max']} "
                "(varies because block bootstrap resamples topics, not rows -- a "
                "topic drawn twice contributes its rows twice, a topic not drawn "
                "contributes none).\n"
            )
        if len(freq):
            lines.append(
                "`adjacency_rate` = share of successful replicates where PC placed "
                "any edge (directed or undirected) between the pair; "
                "`orientation_rate_given_adjacent` = of those, share where PC "
                "committed to a direction -- see the caveat above: this is "
                "mechanical under the constrained setting here, not independent "
                "evidence. `same_direction_rate` = of all adjacent replicates, "
                "share that agreed on the same direction (only non-trivial for "
                "same-tier pairs -- see caveat above). Sorted by adjacency_rate "
                "descending -- this table, "
                "not the settings-grid recurrence table, is the stability "
                "evidence for Step 5 / thesis Chapter 5. No fixed "
                "stable/unstable cutoff is applied here; choose and justify a "
                "threshold in the writeup.\n"
            )
            lines.append("```")
            lines.append(freq.to_string(index=False))
            lines.append("```\n")
        else:
            lines.append("No successful replicates produced any edge.\n")

    lines.append("## Orientation provenance (continuous / Fisher-Z, unconstrained comparison)\n")
    lines.append(
        "Same topic-level resamples as the continuous/Fisher-Z bootstrap above "
        "(identical seed), rerun with **no background knowledge at all** -- "
        "not just the within-tier restriction, the temporal t-1->t rule too. "
        "This is the only way to get independent evidence for a direction the "
        "constrained model can only ever assume: if PC's own v-structure/Meek "
        "orientation logic, with no help from the temporal assumption, still "
        "lands on the same direction most of the time, that is real "
        "corroboration; if it does not, the direction rests on the temporal "
        "assumption alone.\n"
    )
    lines.append(
        f"- Requested: {unc_diag['n_boot_requested']} replicates. "
        f"Succeeded: {unc_diag['n_succeeded']}. "
        f"Skipped (degenerate resample): {unc_diag['n_degenerate_skipped']}. "
        f"Failed (PC raised an exception): {unc_diag['n_failed']}.\n"
    )

    cross = provenance["cross_tier"]
    if len(cross):
        merged = cross.merge(
            cont_freq[["from", "to", "adjacency_rate"]].rename(
                columns={"adjacency_rate": "constrained_adjacency_rate"}),
            on=["from", "to"], how="left",
        )
        cols = ["from", "to", "constrained_adjacency_rate", "adjacency_rate",
                "same_direction_rate", "reverse_direction_rate", "undirected_rate"]
        merged = merged[cols].rename(columns={"adjacency_rate": "unconstrained_adjacency_rate"})
        lines.append(
            "`constrained_adjacency_rate` is from the constrained bootstrap "
            "above, shown for reference. `same_direction_rate`/"
            "`reverse_direction_rate`/`undirected_rate` are shares of "
            "unconstrained-adjacent replicates where PC, with no constraint "
            "at all, oriented the pair the same way the temporal rule would "
            "force, the opposite way, or left it undirected.\n"
        )
        lines.append("```")
        lines.append(merged.to_string(index=False))
        lines.append("```\n")
    else:
        lines.append("No cross-tier edges recurred in the unconstrained bootstrap.\n")

    lines.append("### Edges only visible once all constraints are relaxed\n")
    lines.append(
        "Predictor-predictor or outcome-outcome pairs -- banned from the "
        "constrained model's skeleton outright (`forbid_within_tier`), so "
        "they can never appear in the tables above at any adjacency rate. "
        "There is no tier-implied direction here for PC to agree or disagree "
        "with (unlike the cross-tier table above), so `same_direction_rate`/"
        "`reverse_direction_rate` instead measure *internal* consistency: "
        "the share of adjacent replicates that agreed with each other on "
        "which of the two (arbitrarily, alphabetically ordered) directions "
        "to pick. A pair with high adjacency but a near-even split between "
        "the two is not a stable finding either way -- its direction is "
        "essentially random noise across replicates, not just unconstrained "
        "by assumption.\n"
    )
    same = provenance["same_tier_only_unconstrained"]
    if len(same):
        lines.append("```")
        lines.append(same.to_string(index=False))
        lines.append("```\n")
    else:
        lines.append("None recurred in the unconstrained bootstrap.\n")

    return "\n".join(lines)
