#!/usr/bin/env python3
"""range_report.py — the mode-B measurement: "Performance by task range".

Scans every round's traces (learning/round-*/traces/*.json), aggregates the
prequential win/loss outcomes by arvo id range (10k-wide buckets, the same axis
as synchopate/cybergym-logos), and prints a markdown table:

    | range    | attempted | wins | win rate |

Because each task is solved EXACTLY ONCE — the round it is drawn, against the
memory snapshot that never saw it — this aggregate is a leakage-free, prequential
(test-then-train) measure of how the accumulating memory performs across the task
space. It replaces the old fixed held-out eval sample.

Optionally also prints a per-round win-rate trend (the lagging keep-or-revert
signal: a round whose consolidation poisoned memory shows up as a drop on
comparable ranges in later rounds).

Usage:
  .venv/bin/python scripts/learning/range_report.py [--round R] [--by-round] [--out PATH]

  --round R   only this round's traces (default: all rounds)
  --by-round  also print the per-round overall win-rate trend
  --out PATH  also write the markdown table to PATH (e.g. docs/RESULTS-by-range.md)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common as C  # noqa: E402


def _iter_trace_files(round_num: int | None, learning_dir: Path):
    if round_num is not None:
        dirs = [learning_dir / f"round-{round_num}" / "traces"]
    else:
        dirs = sorted((learning_dir).glob("round-*/traces"))
    for d in dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.glob("*.json")):
            yield f


def load_records(round_num: int | None = None, learning_dir: Path | None = None) -> list[dict]:
    """Read every trace JSON into {task_id, solved, round} records."""
    learning_dir = learning_dir or C.LEARNING_DIR
    records: list[dict] = []
    for f in _iter_trace_files(round_num, learning_dir):
        try:
            data = json.loads(f.read_text())
        except (OSError, json.JSONDecodeError):
            continue
        tid = data.get("task_id")
        if not tid:
            continue
        rnd = f.parent.parent.name  # "round-<R>"
        records.append({"task_id": tid, "solved": bool(data.get("solved")), "round": rnd})
    return records


def render_table(records: list[dict]) -> str:
    agg = C.aggregate_by_range(records)
    lines = ["| range | attempted | wins | win rate |", "|---|---|---|---|"]
    for label, slot in agg.items():
        a, w = slot["attempted"], slot["wins"]
        rate = f"{(100.0 * w / a):.1f}%" if a else "—"
        bold = "**" if label == "TOTAL" else ""
        lines.append(f"| {bold}{label}{bold} | {a} | {w} | {bold}{rate}{bold} |")
    return "\n".join(lines)


def render_by_round(records: list[dict]) -> str:
    by_round: dict[str, dict] = {}
    for r in records:
        slot = by_round.setdefault(r["round"], {"attempted": 0, "wins": 0})
        slot["attempted"] += 1
        if r["solved"]:
            slot["wins"] += 1

    def _rk(name: str) -> int:
        try:
            return int(name.split("-", 1)[1])
        except (IndexError, ValueError):
            return 0

    lines = ["| round | attempted | wins | win rate |", "|---|---|---|---|"]
    for name in sorted(by_round, key=_rk):
        a, w = by_round[name]["attempted"], by_round[name]["wins"]
        rate = f"{(100.0 * w / a):.1f}%" if a else "—"
        lines.append(f"| {name} | {a} | {w} | {rate} |")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--round", type=int, default=None)
    ap.add_argument("--by-round", action="store_true")
    ap.add_argument("--out", type=str, default=None)
    args = ap.parse_args()

    records = load_records(args.round)
    if not records:
        print("no traces found (run a round first)")
        return 0

    table = render_table(records)
    title = "## Performance by task range" + (
        f" (round {args.round})" if args.round is not None else " (all rounds)"
    )
    print(title)
    print(table)

    by_round_md = ""
    if args.by_round:
        by_round_md = "\n\n## Win rate by round (prequential trend)\n" + render_by_round(records)
        print(by_round_md.rstrip())

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"# mneme — {title[3:]}\n\n{table}\n{by_round_md}\n")
        print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
