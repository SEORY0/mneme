#!/usr/bin/env python3
"""shard_round.py — draw a fresh batch and split it DISJOINTLY across 5 workers.

Mode B (prequential, all-task): from the FULL local pool (train ∪ eval ∩
runnable-local) MINUS used_tasks.txt, draw `batch` fresh tasks (seeded by round →
reproducible), split them disjointly into `workers` shard files
learning/round-<R>/shard-1..N.txt, append the drawn tasks to used_tasks.txt (so
future rounds never repeat — each task is measured exactly once, against the
memory snapshot that never saw it), and create the per-round traces/ dir.

There is NO held-out eval set in mode B: every local task is both measured (the
round it is drawn, before any learning from it) and learned from (afterwards, by
the consolidator). Leakage is prevented by ORDER, not by a held-out split.

Usage:
  .venv/bin/python scripts/learning/shard_round.py --round 1 [--workers 5] [--batch 50] [--seed-base 770000]
"""
from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common as C  # noqa: E402


def shard_round(round_num: int, workers: int = 5, batch: int = 50,
                seed_base: int = 770000, learning_dir: Path = None) -> dict:
    learning_dir = learning_dir or C.LEARNING_DIR
    used_path = learning_dir / "used_tasks.txt"

    pool = C.local_pool()

    used = set(C.read_task_list(used_path))

    available = sorted(set(pool) - used)
    if not available:
        raise SystemExit("no available tasks left (local pool exhausted)")

    # Seed by round so a given round's draw is reproducible.
    rng = random.Random(seed_base + round_num)
    rng.shuffle(available)
    drawn = sorted(available[:batch])

    round_dir = learning_dir / f"round-{round_num}"
    traces_dir = round_dir / "traces"
    traces_dir.mkdir(parents=True, exist_ok=True)

    # Disjoint round-robin assignment across workers (worker ids 1..workers).
    shards: dict[int, list[str]] = {w: [] for w in range(1, workers + 1)}
    for i, t in enumerate(drawn):
        shards[(i % workers) + 1].append(t)

    for w in range(1, workers + 1):
        C.write_task_list(round_dir / f"shard-{w}.txt", shards[w])

    # Append the drawn tasks to used_tasks so future rounds don't repeat.
    C.append_task_list(used_path, drawn)

    summary = {
        "round": round_num,
        "workers": workers,
        "batch_requested": batch,
        "drawn": len(drawn),
        "runnable_pool": len(pool),
        "available_before": len(available),
        "per_worker": {w: len(shards[w]) for w in range(1, workers + 1)},
        "round_dir": str(round_dir),
    }

    print(f"Round {round_num}: drew {len(drawn)} tasks "
          f"(requested {batch}; {len(available)} were available, "
          f"{len(pool)} runnable-local in pool).")
    for w in range(1, workers + 1):
        print(f"  shard-{w}: {len(shards[w])} tasks -> {round_dir / f'shard-{w}.txt'}")
    print(f"  traces dir: {traces_dir}")
    print(f"  appended {len(drawn)} ids to {used_path} (now {len(used | set(drawn))} used)")
    return summary


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--round", type=int, required=True)
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--batch", type=int, default=50)
    ap.add_argument("--seed-base", type=int, default=770000)
    args = ap.parse_args()
    shard_round(args.round, workers=args.workers, batch=args.batch, seed_base=args.seed_base)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
