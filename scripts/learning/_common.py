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
EVAL_SAMPLE_PATH = LEARNING_DIR / "eval_sample.txt"
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


def runnable_local_filter(tasks: Iterable[str]) -> List[str]:
    """Filter an iterable of task ids to the runnable-local ones, order-preserving.

    Tests monkeypatch THIS function (not is_runnable_local) so they can supply a
    fake runnable set without docker.
    """
    return [t for t in tasks if is_runnable_local(t)]
