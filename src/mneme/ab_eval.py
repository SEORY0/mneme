"""ab_eval.py — Train-only A/B harness for OKF memory on vs off.

Design rules:
- Only tasks in split["train"] are accepted; any task NOT in train is refused
  and recorded in Report.refused_eval.
- dry_run=True (default): plans and records metrics without calling the agent,
  docker, or network. No solve is performed.
- dry_run=False: would call runner.run.solve per task — NOT exercised by the
  offline test suite.
- submit_count must be ≤ 1 per task (enforced: 0 in dry-run).
- median_attempts is 0 when no tasks were actually attempted (dry-run).
"""
from __future__ import annotations

import statistics
from dataclasses import dataclass, field
from typing import Any


# ---------------------------------------------------------------------------
# Return type
# ---------------------------------------------------------------------------

@dataclass
class Report:
    """Result of an ab_eval.run() call.

    Attributes:
        refused_eval: task ids that were refused because they are not in
                      split["train"].
        metrics: dict with at minimum:
                   attempted        — number of train tasks passed to the harness
                   target_matched   — number that hit target (0 in dry-run)
                   median_attempts  — median attempt count (0 in dry-run)
                   submit_count     — total official submits (0 in dry-run; ≤1/task)
                   failure_classes  — histogram dict of failure_class → count
                 Also recorded when available:
                   negative_memory_hits — tasks where negative memory was consulted
                   cost_usd             — total estimated cost (None in dry-run)
                   total_tokens         — total tokens used (None in dry-run)
    """
    refused_eval: list[str] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _median(values: list[int | float]) -> int | float:
    """Return median of values, or 0 if the list is empty."""
    if not values:
        return 0
    return statistics.median(values)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def run(
    tasks: list[str],
    split: dict[str, list[str]],
    *,
    memory_on: bool,
    dry_run: bool = True,
) -> Report:
    """Run (or plan) the A/B evaluation over a list of task ids.

    Parameters
    ----------
    tasks:
        Task ids to evaluate.
    split:
        Dict with at least a "train" key listing train-split task ids.
        Tasks NOT in split["train"] are refused and recorded in
        Report.refused_eval; they are NOT attempted.
    memory_on:
        Whether OKF memory is enabled for this arm of the A/B comparison.
    dry_run:
        When True (default), no agent/docker/network calls are made.
        Metrics are computed over an empty attempt set (all zeros).

    Returns
    -------
    Report
        .refused_eval — task ids refused (not in train split)
        .metrics      — dict with required keys (see Report docstring)
    """
    train_set = set(split.get("train", []))

    refused: list[str] = []
    accepted: list[str] = []
    for task_id in tasks:
        if task_id not in train_set:
            refused.append(task_id)
        else:
            accepted.append(task_id)

    # In dry_run mode we do not call the agent; produce zero-valued metrics.
    if dry_run:
        metrics: dict[str, Any] = {
            "attempted": len(accepted),
            "target_matched": 0,
            "median_attempts": _median([]),
            "submit_count": 0,
            "failure_classes": {},
            # Extended metrics — None signals "not measured in dry-run"
            "negative_memory_hits": 0,
            "memory_on": memory_on,
            "cost_usd": None,
            "total_tokens": None,
        }
        return Report(refused_eval=refused, metrics=metrics)

    # --- Live path (not exercised by offline tests) ---
    # This would call runner.run.solve per task, collect results, and
    # aggregate the metrics below. Stub raises to make misuse visible.
    raise NotImplementedError(
        "Live ab_eval (dry_run=False) requires Docker + model credentials "
        "and is not part of the offline test suite."
    )
