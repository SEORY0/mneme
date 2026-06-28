#!/usr/bin/env python3
"""build_taxonomy.py — deterministic taxonomy census for okf/vuln-classes & okf/strategies.

Workers' `vuln-classes/` and `strategies/` dirs are in no consolidator write
channel, so the 2026-06-25 hand-seeded taxonomy went stale while the trace
vocabulary grew and fragmented (70% of vuln_class values had no matching file).
This script reads every trace (the same way range_report.py does), normalizes the
free-form `vuln_class` / `candidate_family` onto canonical keys (mneme.vocab),
and writes a DESCRIPTIVE census per canonical key.

It is the same grade as the consolidator's "factual breadth channel"
(formats/harnesses): descriptive, NOT verifier-gated, and NEVER fed into
memory_stats ranking. Each file's machine-owned census lives between
`<!-- BEGIN observed-census -->` markers; hand-authored prose outside the
markers (the seeds' Schema/Recipe) is never touched. Runs are idempotent.

Usage:
  .venv/bin/python scripts/learning/build_taxonomy.py [--through-round R] [--all]
                                                      [--okf DIR] [--learning DIR]

See docs/superpowers/specs/2026-06-28-okf-taxonomy-census-design.md.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import _common as C  # noqa: E402
from mneme.vocab import canonicalize_strategy, canonicalize_vuln, slug  # noqa: E402
from mneme.task_card import redact_for_promotion  # noqa: E402

BEGIN = "<!-- BEGIN observed-census (auto) -->"
END = "<!-- END observed-census -->"
_DISCLAIMER = "_Descriptive trace census — NOT a causal policy; not used for memory ranking._"
_ALIAS_CAP = 40


# --- read + aggregate ------------------------------------------------------

def _round_of(traces_dir: Path) -> int:
    try:
        return int(traces_dir.parent.name.split("-", 1)[1])
    except (IndexError, ValueError):
        return 0


def iter_traces(learning_dir: Path, through_round: int | None = None):
    """Yield every trace dict under learning/round-*/traces/, optionally capped
    at `through_round`. Malformed/unreadable JSON is skipped."""
    for d in sorted(learning_dir.glob("round-*/traces")):
        if not d.is_dir():
            continue
        if through_round is not None and _round_of(d) > through_round:
            continue
        for f in sorted(d.glob("*.json")):
            try:
                yield json.loads(f.read_text())
            except (OSError, json.JSONDecodeError):
                continue


def _new_vuln_slot() -> dict:
    return {"count": 0, "solved": 0, "formats": Counter(), "harnesses": Counter(),
            "strategies": Counter(), "aliases": set()}


def _new_strat_slot() -> dict:
    return {"count": 0, "solved": 0, "vulns": Counter(), "formats": Counter(), "aliases": set()}


def aggregate(traces) -> tuple[dict, dict]:
    """Return (vuln_census, strat_census), keyed by canonical slug."""
    vuln: dict[str, dict] = {}
    strat: dict[str, dict] = {}
    for t in traces:
        solved = 1 if t.get("solved") else 0
        ifmt = slug(t.get("input_format")) or "unknown"
        harn = slug(t.get("harness")) or "unknown"
        vraw = t.get("vuln_class")
        vkey = canonicalize_vuln(vraw)
        strategies = canonicalize_strategy(t.get("candidate_family"))

        v = vuln.setdefault(vkey, _new_vuln_slot())
        v["count"] += 1
        v["solved"] += solved
        v["formats"][ifmt] += 1
        v["harnesses"][harn] += 1
        for s in strategies:
            v["strategies"][s] += 1
        vraw_slug = slug(vraw)
        if vraw_slug and vraw_slug != vkey:
            v["aliases"].add(vraw_slug)

        craw_slug = slug(t.get("candidate_family"))
        for s in strategies:
            st = strat.setdefault(s, _new_strat_slot())
            st["count"] += 1
            st["solved"] += solved
            st["vulns"][vkey] += 1
            st["formats"][ifmt] += 1
            if craw_slug and craw_slug != s:
                st["aliases"].add(craw_slug)
    return vuln, strat


# --- render + upsert -------------------------------------------------------

def _top(counter: Counter, n: int = 8) -> str:
    items = sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
    return ", ".join(f"{k} ({v})" for k, v in items) or "—"


def _census_body(kind: str, key: str, st: dict) -> str:
    lines = [
        "## Observed census (auto)",
        "",
        _DISCLAIMER,
        "",
        f"- canonical: `{key}`",
        f"- observed: {st['count']} traces; solved: {st['solved']} (illustrative — not for ranking)",
    ]
    if kind == "vuln-class":
        lines += [
            f"- top input_formats: {_top(st['formats'])}",
            f"- top harnesses: {_top(st['harnesses'])}",
            f"- observed strategies: {_top(st['strategies'])}",
        ]
    else:  # strategy
        lines += [
            f"- top vuln_classes: {_top(st['vulns'])}",
            f"- top input_formats: {_top(st['formats'])}",
        ]
    aliases = sorted(a for a in st["aliases"] if a != key)
    if aliases:
        shown, extra = aliases[:_ALIAS_CAP], len(aliases) - _ALIAS_CAP
        tail = f" (+{extra} more)" if extra > 0 else ""
        lines.append(f"- collapsed aliases: {', '.join(shown)}{tail}")
    return "\n".join(lines)


def _new_frontmatter(kind: str, key: str) -> str:
    return (
        "---\n"
        f"type: {kind}\n"
        f"title: {key.replace('-', ' ')}\n"
        f"tags: [{key}]\n"
        "generated: taxonomy-census\n"
        "---\n"
    )


def upsert_census(path: Path, kind: str, key: str, st: dict) -> None:
    """Write/refresh the marker-delimited census block in `path`, preserving any
    hand-authored prose outside the markers. Idempotent."""
    block = redact_for_promotion(f"{BEGIN}\n{_census_body(kind, key, st)}\n{END}")
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if BEGIN in text and END in text:
            i, j = text.index(BEGIN), text.index(END) + len(END)
            new = text[:i] + block + text[j:]
        else:
            new = text.rstrip() + "\n\n" + block + "\n"
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        new = _new_frontmatter(kind, key) + "\n" + block + "\n"
    if not new.endswith("\n"):
        new += "\n"
    path.write_text(new, encoding="utf-8")


# --- index.md --------------------------------------------------------------

def _render_links(slugs: list[str], subdir: str, prefix: str = "") -> list[str]:
    return [f"- [{prefix}{s}]({subdir}/{s}.md)" for s in sorted(set(slugs))]


def _replace_section(lines: list[str], header: str, body: list[str]) -> list[str]:
    """Replace the bullet body under `## <header>` (up to the next `## ` header)."""
    try:
        i = next(n for n, ln in enumerate(lines) if ln.rstrip() == header)
    except StopIteration:
        return lines  # section absent — leave file alone
    j = i + 1
    while j < len(lines) and not lines[j].startswith("## "):
        j += 1
    # keep a single trailing blank line before the next header
    return lines[: i + 1] + body + [""] + lines[j:]


def update_index(index_path: Path, vuln_slugs: list[str], strat_slugs: list[str]) -> None:
    text = index_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    lines = _replace_section(lines, "## vuln-classes", _render_links(vuln_slugs, "vuln-classes"))
    lines = _replace_section(lines, "## strategies", _render_links(strat_slugs, "strategies"))
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- orchestration ---------------------------------------------------------

def build(learning_dir: Path, okf_dir: Path, through_round: int | None = None) -> tuple[int, int]:
    vuln, strat = aggregate(iter_traces(learning_dir, through_round))
    for key, st in vuln.items():
        upsert_census(okf_dir / "vuln-classes" / f"{key}.md", "vuln-class", key, st)
    for key, st in strat.items():
        upsert_census(okf_dir / "strategies" / f"{key}.md", "strategy", key, st)
    index = okf_dir / "index.md"
    if index.exists():
        # Link every file present (seeds with no traces this pass included), not
        # only the trace-derived keys.
        vuln_slugs = [p.stem for p in (okf_dir / "vuln-classes").glob("*.md")]
        strat_slugs = [p.stem for p in (okf_dir / "strategies").glob("*.md")]
        update_index(index, vuln_slugs, strat_slugs)
    return len(vuln), len(strat)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--through-round", type=int, default=None)
    ap.add_argument("--all", action="store_true", help="all rounds (default if --through-round absent)")
    ap.add_argument("--okf", type=str, default=str(REPO_ROOT / "memory_store" / "okf"))
    ap.add_argument("--learning", type=str, default=str(C.LEARNING_DIR))
    args = ap.parse_args()
    through = None if args.all else args.through_round
    nv, ns = build(Path(args.learning), Path(args.okf), through)
    print(f"taxonomy census: {nv} vuln-classes, {ns} strategies "
          f"(through round {through if through is not None else 'ALL'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
