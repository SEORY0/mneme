"""
memory_api: pure functions implementing the memory MCP tool scope boundaries (D3).

Design rule D3: SCOPE = TOOL NAME.
  - search_okf_for_generate / get_repair_policy  →  GENERATE scope (full OKF access)
  - get_discriminator_evidence                   →  DISCRIMINATE scope (structurally
        no OKF parameter; cannot reach causal policy by construction)
  - record_proposal                              →  writes under run_dir/proposals/ ONLY
  - scope_check                                  →  consults the VISIBILITY constant

All functions are pure (no global state, no MCP) so they can be unit-tested directly.
"""
from __future__ import annotations

import json
import uuid
from pathlib import Path

from memonaemo import okf as _okf

# ---------------------------------------------------------------------------
# Visibility map — the single source of truth for scope_check.
# Keys are memory_class names; values are the tool names that may see them.
# ---------------------------------------------------------------------------
VISIBILITY: dict[str, set[str]] = {
    "causal_policy": {
        "memory.get_repair_policy",
        "memory.search_okf_for_generate",
    },
    "okf_example": {
        "memory.get_repair_policy",
        "memory.search_okf_for_generate",
    },
    "procedure": {
        "memory.get_repair_policy",
        "memory.search_okf_for_generate",
    },
    "negative_memory": {
        "memory.get_repair_policy",
        "memory.search_okf_for_generate",
    },
    "verifier_summary": {
        "memory.get_discriminator_evidence",
        "memory.get_repair_policy",
        "memory.search_okf_for_generate",
    },
    "candidate_metadata": {
        "memory.get_discriminator_evidence",
    },
    "proposal": {
        "memory.record_proposal",
    },
}


# ---------------------------------------------------------------------------
# GENERATE-scope tools
# ---------------------------------------------------------------------------

def search_okf_for_generate(store_dir: Path, stats, query_keys: dict) -> dict:
    """
    GENERATE scope.  Returns ranked compact records matching query_keys.
    Uses okf.load_policies + okf.rank + okf.compact_record.
    """
    store_dir = Path(store_dir)
    policies = _okf.load_policies(store_dir)
    ranked = _okf.rank(policies, query_keys, stats)
    # Return only policies that actually match (score base=0).
    results = [
        _okf.compact_record(p)
        for p in ranked
        if _okf.matches(p, query_keys)
    ]
    return {"results": results}


def get_repair_policy(
    store_dir: Path,
    stats,
    failure_class: str,
    verifier_signal: str,
    input_format: str | None = None,
    harness_convention: str | None = None,
    vuln_class: str | None = None,
) -> dict:
    """
    GENERATE scope.  Returns the best-matching compact record (or null).
    NEVER returns the full Policy body — only compact_record output.
    """
    store_dir = Path(store_dir)
    query: dict = {"failure_class": failure_class, "verifier_signal": verifier_signal}
    if input_format:
        query["input_format"] = input_format
    if harness_convention:
        query["harness_convention"] = harness_convention
    if vuln_class:
        query["vuln_class"] = vuln_class

    policies = _okf.load_policies(store_dir)
    ranked = _okf.rank(policies, query, stats)
    matching = [p for p in ranked if _okf.matches(p, query)]
    if not matching:
        return {"policy": None}
    return {"policy": _okf.compact_record(matching[0])}


# ---------------------------------------------------------------------------
# DISCRIMINATE-scope tool
# ---------------------------------------------------------------------------

def get_discriminator_evidence(
    candidate_meta: dict,
    verifier_summary: dict,
) -> dict:
    """
    DISCRIMINATE scope.

    Structural isolation: this function accepts ONLY candidate_meta and
    verifier_summary.  There is no store_dir / stats / okf parameter, so
    there is no code path that can reach OKF, causal policies, or generate
    reasoning — the isolation is enforced by the function signature itself,
    not by a runtime check.

    Returns exactly {verifier_summary, candidate_metadata}.
    """
    return {
        "verifier_summary": verifier_summary,
        "candidate_metadata": candidate_meta,
    }


# ---------------------------------------------------------------------------
# Write tool — promotion guard (D9)
# ---------------------------------------------------------------------------

def record_proposal(run_dir: Path, payload: dict) -> dict:
    """
    Writes a dry-run proposal JSON under run_dir/proposals/.
    NEVER writes to memory_store/okf/ or any OKF path.
    The write location is always a subdirectory of run_dir provided by the caller.
    """
    run_dir = Path(run_dir)
    proposals_dir = run_dir / "proposals"
    proposals_dir.mkdir(parents=True, exist_ok=True)
    proposal_id = uuid.uuid4().hex[:12]
    proposal_path = proposals_dir / f"proposal-{proposal_id}.json"
    proposal_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return {"proposal_path": str(proposal_path)}


# ---------------------------------------------------------------------------
# Scope check utility
# ---------------------------------------------------------------------------

def scope_check(memory_class: str, tool: str) -> dict:
    """
    Reports whether `tool` is permitted to see `memory_class`.
    Consults the VISIBILITY constant; unknown classes/tools default to invisible.
    """
    visible = tool in VISIBILITY.get(memory_class, set())
    return {"visible": visible, "memory_class": memory_class, "tool": tool}
