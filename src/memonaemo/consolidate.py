"""consolidate.py — Offline, train-only, dry-run consolidation with optional review gate.

Design (ported from causal_distill.py):
- Refusal conditions (returns Refusal):
    1. Task is in the eval split (never promote eval knowledge)
    2. Run is unsolved  (result_json["solved"] is not True)
    3. Run is unverified (result_json["verified"] is not True)
    4. PoC path is missing/unreadable

- Abstract proposal keyed by: vuln_class × input_format × harness × failure_class
  All forbidden fields are stripped via task_card.redact_for_promotion:
  raw PoC bytes, task ids, submit metadata, server URLs, checksums, exact offsets.
  Abstract keys (vuln_class, input_format, harness, failure_class) ARE kept.

- Dry-run by default: returns Proposal object and writes a markdown file under
  out_dir (or a default scratch dir), but NEVER mutates memory_store/okf/.

- Optional specialist: if provided, calls specialist.review_consolidation(payload)
  which must return {"approved": bool, "notes": str}.
  A non-approving verdict sets proposal.status = "blocked".

Specialist contract:
    specialist.review_consolidation(payload: dict) -> {"approved": bool, "notes": str}
"""
from __future__ import annotations

import re
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from memonaemo.task_card import redact_for_promotion


# ---------------------------------------------------------------------------
# Patterns ported from causal_distill._UNSAFE_ABSTRACT_PATTERNS
# ---------------------------------------------------------------------------
_SAFE_ABSTRACT_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
_UNSAFE_ABSTRACT_PATTERNS = (
    re.compile(r"\b0x[0-9a-f]{2,}\b", re.IGNORECASE),
    re.compile(r"\b[0-9a-f]{8,}\b", re.IGNORECASE),
    re.compile(r"\boffset\s+\d+\b", re.IGNORECASE),
    re.compile(r"://"),
    re.compile(r"[/\\]"),
)
_UNSAFE_ABSTRACT_TERMS = (
    "agent_id", "candidate_path", "checksum", "raw_candidate_bytes",
    "raw_poc", "server_url", "submit_metadata", "task_id",
    "schema-simple-memory",
)


def _abstract_slug(value: str | None) -> str:
    """Ported from causal_distill._abstract_slug — sanitises a field value into a safe slug."""
    if value is None:
        return "unknown"
    lowered = value.strip().lower()
    if any(term in lowered for term in _UNSAFE_ABSTRACT_TERMS):
        return "unknown"
    if any(p.search(lowered) is not None for p in _UNSAFE_ABSTRACT_PATTERNS):
        return "unknown"
    slug = re.sub(r"[^a-z0-9]+", "-", lowered).strip("-")
    if _SAFE_ABSTRACT_SLUG.fullmatch(slug) is None:
        return "unknown"
    return slug


# ---------------------------------------------------------------------------
# Return types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Refusal:
    """Returned when consolidation is refused."""
    refused: bool = True
    reason: str = ""


@dataclass
class Proposal:
    """Returned when consolidation proceeds."""
    refused: bool = False
    status: str = "proposed"           # "proposed" | "blocked"
    abstract_key: dict = field(default_factory=dict)
    markdown: str = ""
    out_path: Path | None = None
    specialist_verdict: dict | None = None


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _is_eval(task_id: str | None, split: dict) -> bool:
    eval_tasks = split.get("eval", [])
    return task_id in eval_tasks


def _poc_readable(poc_path: str | None) -> bool:
    if not poc_path:
        return False
    return Path(poc_path).is_file()


def _build_markdown(abstract_key: dict, raw_result: dict) -> str:
    """Build the abstract proposal markdown — all forbidden fields stripped."""
    vuln_class = abstract_key["vuln_class"]
    input_format = abstract_key["input_format"]
    harness = abstract_key["harness"]
    failure_class = abstract_key["failure_class"]

    # Collect any extra safe fields to surface (sink_loc only — no offsets/checksums)
    sink_loc = raw_result.get("sink_loc", "")
    if isinstance(sink_loc, str):
        sink_loc = redact_for_promotion(sink_loc)
    else:
        sink_loc = ""

    lines = [
        "---",
        "type: consolidation-proposal",
        "access_scope: offline_consolidation",
        f"vuln_class: {vuln_class}",
        f"input_format: {input_format}",
        f"harness: {harness}",
        f"failure_class: {failure_class}",
        "---",
        "",
        "# Consolidation Proposal",
        "",
        "## Abstract key",
        f"- vuln_class: {vuln_class}",
        f"- input_format: {input_format}",
        f"- harness: {harness}",
        f"- failure_class: {failure_class}",
    ]
    if sink_loc:
        lines += ["", "## Sink location (abstract)", f"- {sink_loc}"]

    return "\n".join(lines)


def _default_out_dir() -> Path:
    """Return a session-scoped scratch dir that is NOT under memory_store/okf."""
    scratch = Path(tempfile.gettempdir()) / "memonaemo-consolidate-scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    return scratch


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def propose(
    result_json: dict,
    split: dict,
    *,
    specialist=None,
    out_dir: Path | str | None = None,
) -> Proposal | Refusal:
    """Build an abstract consolidation proposal from a solved, verified run result.

    Refusal conditions:
    - task is in eval split
    - run is unsolved
    - run is unverified
    - PoC path is missing/unreadable

    Returns a Refusal (refused=True) or a Proposal (refused=False).
    Dry-run by default — NEVER writes under memory_store/okf/.
    """
    task_id = result_json.get("task_id")

    # Gate 1: eval split — refused outright
    if _is_eval(task_id, split):
        return Refusal(reason="eval_refused")

    # Gate 2: unsolved
    if not result_json.get("solved"):
        return Refusal(reason="unsolved_refused")

    # Gate 3: unverified
    if not result_json.get("verified"):
        return Refusal(reason="unverified_refused")

    # Gate 4: PoC missing
    poc_path = result_json.get("poc_path")
    if not _poc_readable(poc_path):
        return Refusal(reason="poc_missing_refused")

    # Build abstract key — slugify each dimension
    abstract_key = {
        "vuln_class": _abstract_slug(result_json.get("vuln_class")),
        "input_format": _abstract_slug(result_json.get("input_format")),
        "harness": _abstract_slug(result_json.get("harness")),
        "failure_class": _abstract_slug(result_json.get("failure_class")),
    }

    # Build markdown — all forbidden fields stripped
    markdown = _build_markdown(abstract_key, result_json)
    # Extra safety pass: run redact_for_promotion over the whole markdown
    markdown = redact_for_promotion(markdown)

    # Determine output directory — never okf/
    if out_dir is not None:
        write_dir = Path(out_dir)
    else:
        write_dir = _default_out_dir()

    # Dry-run: write the proposal markdown file but NOT under okf/
    stem = "__".join([
        abstract_key["vuln_class"],
        abstract_key["input_format"],
        abstract_key["harness"],
        abstract_key["failure_class"],
    ])
    out_path = write_dir / f"proposal__{stem}.md"
    out_path.write_text(markdown + "\n", encoding="utf-8")

    proposal = Proposal(
        abstract_key=abstract_key,
        markdown=markdown,
        out_path=out_path,
    )

    # Optional specialist review gate
    if specialist is not None:
        verdict = specialist.review_consolidation({
            "abstract_key": abstract_key,
            "markdown": markdown,
        })
        proposal.specialist_verdict = verdict
        if not verdict.get("approved", False):
            proposal.status = "blocked"

    return proposal
