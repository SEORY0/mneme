"""Shared helpers for the 5-worker no-API learning scripts.

Pure, offline-friendly helpers. The only function that touches docker /
filesystem state is `is_runnable_local`; everything else is deterministic and
unit-testable. Tests monkeypatch `runnable_local_filter` to avoid docker.
"""
from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path
from typing import Iterable, List

# Repo root = two levels up from this file (scripts/learning/_common.py).
REPO_ROOT = Path(__file__).resolve().parents[2]

SPLIT_PATH = REPO_ROOT / "data" / "okf_split.json"
LEARNING_DIR = REPO_ROOT / "learning"
USED_TASKS_PATH = LEARNING_DIR / "used_tasks.txt"

ARVO_DATA_ROOT = Path(os.environ.get("CYBERGYM_DATA_ROOT", "/data/cybergym_data/data")) / "arvo"


def load_split(split_path: Path = SPLIT_PATH) -> dict:
    return json.loads(Path(split_path).read_text())


def read_task_list(path: Path) -> List[str]:
    """Read newline-delimited task ids; ignore blanks and '#' comments."""
    p = Path(path)
    if not p.exists():
        return []
    out = []
    for line in p.read_text().splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s)
    return out


def write_task_list(path: Path, tasks: Iterable[str]) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("".join(f"{t}\n" for t in tasks))


def append_task_list(path: Path, tasks: Iterable[str]) -> None:
    existing = read_task_list(path)
    seen = set(existing)
    merged = list(existing)
    for t in tasks:
        if t not in seen:
            merged.append(t)
            seen.add(t)
    write_task_list(path, merged)


def safe_task(task_id: str) -> str:
    """arvo:12345 -> arvo_12345 (safe for filenames / run dirs)."""
    return task_id.replace(":", "_").replace("/", "_")


def is_runnable_local(task_id: str) -> bool:
    """A task is runnable-local iff it is an arvo:<N> with both the data dir and
    a non-empty `docker images -q n132/arvo:<N>-vul`.

    This is the ONLY helper that touches docker/fs; tests monkeypatch
    `runnable_local_filter` so they never call it.
    """
    if not task_id.startswith("arvo:"):
        return False
    n = task_id.split(":", 1)[1]
    if not n.isdigit():
        return False
    if not (ARVO_DATA_ROOT / n).exists():
        return False
    try:
        out = subprocess.run(
            ["docker", "images", "-q", f"n132/arvo:{n}-vul"],
            capture_output=True, text=True, timeout=30,
        )
    except (OSError, subprocess.SubprocessError):
        return False
    return out.returncode == 0 and out.stdout.strip() != ""


def _available_arvo_vul_ids() -> set[str]:
    """Set of arvo numeric ids that have a local n132/arvo:<N>-vul image.

    ONE `docker images` call (not one per task) — listing all n132/arvo tags and
    keeping the <N> of every <N>-vul tag.
    """
    try:
        out = subprocess.run(
            ["docker", "images", "n132/arvo", "--format", "{{.Tag}}"],
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return set()
    if out.returncode != 0:
        return set()
    ids = set()
    for tag in out.stdout.split():
        if tag.endswith("-vul"):
            ids.add(tag[: -len("-vul")])
    return ids


def runnable_local_filter(tasks: Iterable[str]) -> List[str]:
    """Filter an iterable of task ids to the runnable-local ones, order-preserving.

    Uses a SINGLE `docker images` query for the vul-image check (not one docker
    call per task — that made filtering ~1300 tasks take minutes). A task is
    runnable-local iff it is arvo:<N> with the data dir present and an <N>-vul
    image locally.

    Tests monkeypatch THIS function so they never call docker.
    """
    tasks = list(tasks)
    vul_ids = _available_arvo_vul_ids()
    out = []
    for t in tasks:
        if not t.startswith("arvo:"):
            continue
        n = t.split(":", 1)[1]
        if not n.isdigit():
            continue
        if n not in vul_ids:
            continue
        if not (ARVO_DATA_ROOT / n).exists():
            continue
        out.append(t)
    return out


def local_pool(split: dict | None = None) -> List[str]:
    """The full prequential learning pool: ALL runnable-local tasks across both
    splits, de-duplicated and order-preserving (train first, then eval).

    Mode B learns from every local task — there is NO held-out eval split — so
    the pool is train ∪ eval, not train-only. Tasks are removed from the round
    draw only once they appear in used_tasks.txt (each measured exactly once).
    """
    split = split if split is not None else load_split()
    merged: List[str] = []
    seen = set()
    for t in list(split.get("train", [])) + list(split.get("eval", [])):
        if t not in seen:
            merged.append(t)
            seen.add(t)
    return runnable_local_filter(merged)


def range_bucket(task_id: str) -> str:
    """Map a task id to a 10k-wide arvo id range label (the synchopate
    "Performance by task range" axis), e.g. arvo:3938 -> "0k-10k",
    arvo:12345 -> "10k-20k", arvo:64574 -> "60k-70k". Non-arvo ids -> "oss-fuzz";
    malformed arvo ids -> "arvo-other".
    """
    if task_id.startswith("arvo:"):
        n = task_id.split(":", 1)[1]
        if n.isdigit():
            lo = (int(n) // 10000) * 10
            return f"{lo}k-{lo + 10}k"
        return "arvo-other"
    return "oss-fuzz"


def _bucket_sort_key(label: str) -> tuple:
    """Sort range labels numerically ("0k-10k" < "10k-20k" < ... < oss-fuzz)."""
    if label.endswith("k") and "k-" in label:
        try:
            return (0, int(label.split("k-", 1)[0]))
        except ValueError:
            return (1, 0)
    return (2, 0)


def aggregate_by_range(records: Iterable[dict]) -> dict:
    """Aggregate {task_id, solved} records into per-range win stats.

    Returns an ordered dict: {range_label: {"attempted": a, "wins": w}}, sorted
    by range, with a final "TOTAL" key. `records` is any iterable of dicts with
    a `task_id` and a truthy/falsy `solved` field (e.g. parsed trace JSONs).
    """
    buckets: dict[str, dict] = {}
    for rec in records:
        tid = rec.get("task_id")
        if not tid:
            continue
        b = range_bucket(tid)
        slot = buckets.setdefault(b, {"attempted": 0, "wins": 0})
        slot["attempted"] += 1
        if rec.get("solved"):
            slot["wins"] += 1
    out: dict[str, dict] = {}
    for label in sorted(buckets, key=_bucket_sort_key):
        out[label] = buckets[label]
    total_a = sum(v["attempted"] for v in buckets.values())
    total_w = sum(v["wins"] for v in buckets.values())
    out["TOTAL"] = {"attempted": total_a, "wins": total_w}
    return out
