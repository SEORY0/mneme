"""specialist_core.py — GPT-5.5 hard-failure specialist advisor.

Design rules:
- SCOPE HYGIENE: diagnosis is run through task_card.redact_for_promotion before
  it leaves this box — task ids / offsets / checksums never reach the specialist.
- The specialist NEVER writes memory or submits. Returns {"strategy": <text>} only.
- resolve_model() queries the live client for a gpt-5.5* id; falls back to
  env MEMONAEMO_SPECIALIST_MODEL (or "gpt-5.5" as last resort).
"""
from __future__ import annotations

import json
import os
from typing import Any

from memonaemo.task_card import redact_for_promotion

# ---------------------------------------------------------------------------
# Allowed kinds
# ---------------------------------------------------------------------------

_ALLOWED_KINDS: frozenset[str] = frozenset({
    "rethink_reachability",
    "relocalize_sink",
    "escape_basin",
    "diversify_family",
    "review_consolidation",
})

# ---------------------------------------------------------------------------
# Model resolution
# ---------------------------------------------------------------------------

def resolve_model(client: Any) -> str:
    """Return the GPT-5.5 model id.

    Queries client.models.list() for an id starting with 'gpt-5.5' or
    containing '5.5'. Falls back to env MEMONAEMO_SPECIALIST_MODEL, then
    to the literal string "gpt-5.5".
    """
    env_fallback = os.environ.get("MEMONAEMO_SPECIALIST_MODEL", "gpt-5.5")
    try:
        models = client.models.list()
        # models may be a paged object or a plain list; iterate safely
        items = getattr(models, "data", None)
        if items is None:
            items = list(models)
        for m in items:
            mid = getattr(m, "id", "") or ""
            if mid.startswith("gpt-5.5") or "5.5" in mid:
                return mid
    except Exception:
        pass
    return env_fallback


# ---------------------------------------------------------------------------
# Core advisor
# ---------------------------------------------------------------------------

def advise(
    kind: str,
    diagnosis: dict,
    repair_policy: dict | None,
    *,
    client: Any,
    model: str,
) -> dict[str, str]:
    """Call the specialist for a given hard-failure kind.

    Args:
        kind: One of the five specialist kinds (validated).
        diagnosis: Failure diagnosis dict — will be redacted before sending.
        repair_policy: Compact repair policy dict, or None.
        client: OpenAI-compatible client (chat.completions.create interface).
        model: Model id to call.

    Returns:
        {"strategy": <text>}

    Raises:
        ValueError: if kind is not in the allowed set.
    """
    if kind not in _ALLOWED_KINDS:
        raise ValueError(
            f"Unknown specialist kind {kind!r}. "
            f"Must be one of: {sorted(_ALLOWED_KINDS)}"
        )

    # SCOPE HYGIENE — redact before the diagnosis leaves the box
    redacted_diagnosis = redact_for_promotion(json.dumps(diagnosis))

    policy_text = json.dumps(repair_policy, indent=2) if repair_policy else "null"

    system_msg = (
        "You are a hard-failure specialist for a CyberGym fuzzing agent. "
        "You MUST NOT write memory, submit solutions, or reference task infrastructure. "
        "Return only a concrete strategy to overcome the failure described."
    )
    user_msg = (
        f"Specialist kind: {kind}\n\n"
        f"Failure diagnosis (redacted):\n{redacted_diagnosis}\n\n"
        f"Repair policy:\n{policy_text}\n\n"
        "Provide a concise strategy (no more than 400 words)."
    )

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg},
        ],
    )
    strategy = resp.choices[0].message.content
    return {"strategy": strategy}
