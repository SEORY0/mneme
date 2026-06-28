"""Canonical normalization of the free-form trace vocabulary.

Workers emit `vuln_class` / `candidate_family` as free text. Most values are one
of a small set of sanitizer classes spelled many ways (`uaf` /
`use-after-free` / `heap-use-after-free`), but a long tail is hyper-specific
free-form description (`adpcm-block-size-validation`) — of 516 distinct
`vuln_class` strings seen, 450 are singletons. So normalization is KEYWORD-BASED:
scan the slug for known sanitizer tokens and map onto a BOUNDED canonical set;
anything with no recognizable token falls into a single `other` bucket rather
than minting a per-string file. This keeps `okf/vuln-classes` a real taxonomy
(~20 files) instead of trace noise (~500).

See docs/superpowers/specs/2026-06-28-okf-taxonomy-census-design.md.

Pure module — no I/O, no dependency on the live solve path.
"""
from __future__ import annotations

import re

__all__ = ["canonicalize_vuln", "canonicalize_strategy", "slug", "OTHER"]

OTHER = "other"


def slug(value: str | None) -> str:
    """Lowercase, collapse non-alphanumeric runs to single hyphens, trim."""
    if value is None:
        return ""
    return re.sub(r"[^a-z0-9]+", "-", value.strip().lower()).strip("-")


# --- vuln_class ------------------------------------------------------------

# Ordered (substring, family). FIRST match wins, so list most-specific first.
# The terminal sink wins: "integer-overflow-to-out-of-bounds-read" is an OOB read,
# so out-of-bounds precedes integer-overflow.
_VULN_KEYWORDS: list[tuple[str, str]] = [
    ("use-after-poison", "use-after-poison"),
    ("use-after-scope", "use-after-free"),         # stack UAF variant
    ("use-after-return", "use-after-free"),        # stack UAF variant
    ("use-after-free", "use-after-free"),
    ("heap-use-after-free", "use-after-free"),
    ("uaf", "use-after-free"),
    ("double-free", "double-free"),
    ("invalid-free", "invalid-free"),
    ("uninitial", "use-of-uninitialized-value"),   # uninitialized / uninitialised
    ("uninit", "use-of-uninitialized-value"),
    ("heap-buffer-overflow", "heap-buffer-overflow"),
    ("heap-overflow", "heap-buffer-overflow"),
    ("stack-buffer-overflow", "stack-buffer-overflow"),
    ("global-buffer-overflow", "global-buffer-overflow"),
    ("global-overflow", "global-buffer-overflow"),
    ("out-of-bound", "out-of-bounds"),             # out-of-bound(s)
    ("out-of-range", "out-of-bounds"),
    ("index-out", "out-of-bounds"),
    ("bounds-check", "out-of-bounds"),
    ("oob", "out-of-bounds"),
    ("overread", "out-of-bounds"),
    ("overrun", "out-of-bounds"),
    ("buffer-overflow", "buffer-overflow"),        # generic, after heap/stack/global
    ("stack-overflow", "stack-overflow"),          # recursion/exhaustion (not a buffer)
    ("stack-exhaustion", "stack-overflow"),
    ("null", "null-pointer-dereference"),
    ("type-confusion", "type-confusion"),
    ("integer-overflow", "integer-overflow"),
    ("signed-integer-overflow", "integer-overflow"),
    ("memory-corruption", "memory-corruption"),
    ("memory-leak", "memory-leak"),
    ("undefined-behavior", "undefined-behavior"),
]

# Families that never carry a read/write suffix (access intrinsic or N/A).
_VULN_NO_ACCESS_FAMILIES: frozenset[str] = frozenset({
    "use-of-uninitialized-value",
    "double-free",
    "invalid-free",
    "null-pointer-dereference",
    "integer-overflow",
    "type-confusion",
    "memory-corruption",
    "memory-leak",
    "stack-overflow",
    "undefined-behavior",
})


def _vuln_access(s: str) -> str:
    if "write" in s:
        return "write"
    if "read" in s or "overread" in s:
        return "read"
    return ""


def canonicalize_vuln(raw: str | None) -> str:
    """Map a raw trace `vuln_class` onto a canonical `family[-access]` key.

    Keyword-based onto a bounded set; read/write preserved where the family
    carries it; unrecognized input -> ``other`` (one bucket, not a new file).
    """
    s = slug(raw)
    if not s:
        return "unknown"

    family = OTHER
    for token, fam in _VULN_KEYWORDS:
        if token in s:
            family = fam
            break
    if family == OTHER:
        return OTHER

    access = "" if family in _VULN_NO_ACCESS_FAMILIES else _vuln_access(s)
    return f"{family}-{access}" if access else family


# --- candidate_family / strategy -------------------------------------------

# Canonical strategy vocabulary, in deterministic output order. A compound
# candidate_family is matched by substring, so it can contribute several tags.
_CANON_STRATEGIES: tuple[str, ...] = (
    "construct",
    "seed-mutate",
    "seed-sweep",
    "seed-replay",
    "fuzzer",
    "hint-literal",
    "tiny-probe",
    "analysis-only",
)

# Substring -> canonical strategy (applied after slugging).
_STRATEGY_ALIASES: dict[str, str] = {
    "recon": "analysis-only",
    "analysis": "analysis-only",
    "source-inspection": "analysis-only",
    "seed-corpus-scan": "analysis-only",
    "smoke": "tiny-probe",
    "probe": "tiny-probe",
}


def canonicalize_strategy(raw: str | None) -> list[str]:
    """Map a raw `candidate_family` onto a list of canonical strategy tags.

    A compound family contributes to every canonical strategy it mentions.
    Unrecognized input -> ``["other"]``. Output order follows
    `_CANON_STRATEGIES` for determinism.
    """
    s = slug(raw)
    if not s:
        return ["unknown"]

    matched: set[str] = set()
    for canon in _CANON_STRATEGIES:
        if canon in s:
            matched.add(canon)
    for sub, canon in _STRATEGY_ALIASES.items():
        if sub in s:
            matched.add(canon)

    if not matched:
        return [OTHER]
    return [c for c in _CANON_STRATEGIES if c in matched]
