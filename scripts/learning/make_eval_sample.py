#!/usr/bin/env python3
"""make_eval_sample.py — pick a deterministic, fixed held-out eval sample.

Draws ~20 runnable-local task ids from split.eval (seeded → reproducible) and
writes them to learning/eval_sample.txt. Idempotent: does NOT overwrite an
existing file unless --force is given, so the held-out measurement stays
comparable across rounds and sessions.

Usage:
  .venv/bin/python scripts/learning/make_eval_sample.py [--size 20] [--seed 20260625] [--force]
"""
from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _common as C  # noqa: E402


def make_eval_sample(size: int = 20, seed: int = 20260625, force: bool = False,
                     out_path: Path = None) -> list[str]:
    out_path = out_path or C.EVAL_SAMPLE_PATH
    if out_path.exists() and not force:
        existing = C.read_task_list(out_path)
        print(f"eval_sample already exists ({len(existing)} tasks) at {out_path}; "
              f"use --force to regenerate")
        return existing

    split = C.load_split()
    candidates = C.runnable_local_filter(split["eval"])
    if not candidates:
        raise SystemExit("no runnable-local eval candidates found")

    rng = random.Random(seed)
    pool = sorted(set(candidates))
    rng.shuffle(pool)
    chosen = sorted(pool[:size])
    C.write_task_list(out_path, chosen)
    print(f"wrote {len(chosen)} fixed eval tasks to {out_path} (seed={seed})")
    return chosen


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--size", type=int, default=20)
    ap.add_argument("--seed", type=int, default=20260625)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    make_eval_sample(size=args.size, seed=args.seed, force=args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
