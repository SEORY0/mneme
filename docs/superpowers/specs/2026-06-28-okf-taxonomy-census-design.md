# OKF Taxonomy Census — design

**Date:** 2026-06-28
**Status:** approved (design); implementation pending
**Branch context:** authored while the learning pass runs on `feat/learning-rounds-6plus`.

## Problem

`memory_store/okf/` has five category dirs. Three grow every round; two are frozen:

| dir | written by | count | covers traces? |
|---|---|---:|---|
| `causal-policies/` | consolidator (verifier-gated) | 961 | — |
| `formats/` | consolidator breadth channel (every trace) | 596 | — |
| `harnesses/` | consolidator breadth channel (every trace) | 235 | — |
| `vuln-classes/` | **nothing** — hand-seeded 2026-06-25 | 9 | **no** |
| `strategies/` | **nothing** — hand-seeded 2026-06-25 | 6 | partial |

Measured over 1054 existing traces:

- **vuln_class: 70% (741/1054) of traces have a `vuln_class` with no matching seed file.** Two causes mixed: (a) genuine gaps — `out-of-bounds-read` (89, the 2nd-most-common class) has no seed at all, plus `stack-buffer-overflow-write` (22), `integer-overflow` (12), `null-dereference`/`null-pointer-dereference` (15), `type-confusion` (5); (b) vocabulary drift — `use-after-free` (26) / `heap-use-after-free` (19) / seed `heap-use-after-free-read` (7) are the same concept counted three ways; `double-free` (11) vs seed `heap-double-free`.
- **strategy (`candidate_family`): ~95% token-covered but file keys don't match** — traces emit `seed_mutate` (underscore) vs seed `seed-mutate` (hyphen), plus a free-form long tail (`seed_mutate_and_construct`, `construct_tiff_minimal_extra_alpha`, …).

Root cause: the consolidator prompt directs writes only to `causal-policies/`, `formats/`, `harnesses/`. `vuln-classes/` and `strategies/` are in no write channel, so the 2026-06-25 seed taxonomy is static while the trace vocabulary grew and fragmented.

The seed files are themselves trace **census** artifacts — they already carry `Support: N train-set solves`, `Winning strategies (observed): {...}`, `Format families (observed): {...}`. So these dirs are fundamentally aggregate statistics over traces, not causal policies.

## Goal

Make `vuln-classes/` and `strategies/` cover what actually appears in traces, with consistent canonical naming, maintained automatically every round — without disturbing the live pass or the verifier-gated causal-policy pipeline.

## Approach (chosen)

A **deterministic Python taxonomy aggregator** plus a **canonical vocabulary module**, wired as one step in the consolidator. Deterministic (not Codex-prompt-driven) because the present failure mode *is* non-deterministic free-form authoring; determinism guarantees normalization, is testable, backfills the existing 1054 traces immediately, and stays clear of the causal-policy logic.

### Canonical naming

`canonicalize_vuln`: keep the **access axis** (`-read`/`-write`) where present — read vs write have different sinks/recipes, which is why the seeds split them — and collapse only synonym noise.

- `canonical = family[-access]`
- access ∈ {`read`, `write`, ∅}; trailing `-access` is dropped (direction unknown → no suffix).
- family stems mapped through a synonym table, e.g.:
  - `uaf`, `heap-use-after-free` → `use-after-free`
  - `oob`, `out-of-bounds-access` → `out-of-bounds`
  - `null-dereference`, `null-deref` → `null-pointer-dereference`
  - `uninitialized-read`, `uninitialized-value`, `uninitialized-memory-read`, `use-of-uninitialized-memory` → `use-of-uninitialized-value`
  - `heap-double-free` → `double-free` (`invalid-free` kept distinct)
- **Unregistered families pass through slugged** — a new class auto-creates its file. This is what closes the 70% gap.

`canonicalize_strategy` → `list[slug]`: tokenize on `_ + | / ` and the literal `-and-`; tag the trace under every token matching the canonical strategy vocab (`construct`, `seed-mutate`, `seed-sweep`, `fuzzer`, `hint-literal`, `tiny-probe`, `seed-replay`, `analysis-only`); a compound family contributes to multiple files; if no token matches, file under the whole slug.

## Components

### `src/mneme/vocab.py` (new, pure)
- `canonicalize_vuln(raw: str | None) -> str`
- `canonicalize_strategy(raw: str | None) -> list[str]`
- The synonym/family/strategy tables as explicit module constants (reviewable). No I/O. No dependency on the running code paths (`task_card`, `consolidate`, `memory_api`), so adding it is invisible to the live pass.

### `scripts/learning/build_taxonomy.py` (new)
- `--through-round R` (per-round) | `--all` (one-time backfill). Reads `learning/*/traces/*.json` the same way `range_report.py` already does.
- For each canonical key, creates/refreshes `okf/vuln-classes/<slug>.md` and `okf/strategies/<slug>.md`.
- **Machine-owned region is marker-delimited and rewritten idempotently:**
  ```
  <!-- BEGIN observed-census (auto) -->
  …census…
  <!-- END observed-census -->
  ```
  Everything **outside** the markers (the seeds' hand-authored Schema/Sink/Recipe/Candidate-families prose) is never touched — seed knowledge is preserved; reruns are idempotent.
- Census block (descriptive, non-causal): `observed_count`, `solved_count` (marked illustrative), top `input_formats` / `harnesses` / `strategies`, and the raw aliases collapsed into this canonical key.
- Refreshes the `## vuln-classes` and `## strategies` link sections of `okf/index.md`.
- Every emitted text passes `task_card.redact_for_promotion`.

### Consolidator wiring
Add **step 4b** to `docs/codex-consolidator-prompt.md`, immediately after the breadth channel (step 4):

> **4b. TAXONOMY CENSUS (deterministic, descriptive — like the range report).** Run `.venv/bin/python scripts/learning/build_taxonomy.py --through-round $ROUND` to refresh `okf/vuln-classes/` and `okf/strategies/` and the index links from all traces so far. It is descriptive, not verifier-gated, and is NOT fed into `memory_stats.jsonl` ranking. Its output is already covered by `git add memory_store/okf`.

The prompt file is not itself `git add`ed by the consolidator, so editing it is safe.

## Data flow

```
learning/*/traces/*.json
   │  (read all, same as range_report.py)
   ▼
vocab.canonicalize_vuln / canonicalize_strategy   ← normalization
   ▼
per-canonical census aggregation
   ▼
rewrite <!-- observed-census --> block in okf/<dir>/<slug>.md   ← marker-scoped, idempotent
   │  (hand-authored prose untouched)              redact_for_promotion on every text
   ▼
refresh okf/index.md link sections
```

## Leakage / prequential treatment

This census re-reads every prior round's traces each round — **identical in kind to `range_report.py`, which already aggregates all traces by task range every round.** It is a descriptive taxonomy census, not a re-measurement of memory effect, and is **never written into `memory_stats.jsonl` or the causal-policy success-rate ranking**. It is the same grade as the existing non-verifier-gated breadth channel (`formats/`, `harnesses/`). `solved_count` is recorded as illustrative only and does not feed ranking. This keeps the prequential leakage guard (which governs the *causal* store) intact.

## Error handling

- Malformed/unreadable trace JSON is skipped (counted), not fatal — matches `range_report.py`.
- A trace missing `vuln_class`/`candidate_family` is filed under `unknown`.
- Marker block absent in an existing file → inserted at end; present → replaced in place. Never duplicates.
- The script only writes `okf/vuln-classes/`, `okf/strategies/`, and `okf/index.md`; it touches no other okf paths and makes no git calls (commits stay with the consolidator / the backfill step).

## Testing (TDD)

- `tests/test_vocab.py` — synonym collapse, access-suffix preservation/`-access` drop, unregistered-family passthrough, compound-strategy multi-tag, separator normalization.
- `tests/test_build_taxonomy.py` — census idempotency (run twice → byte-identical), **hand-authored prose outside markers preserved**, index link sections refreshed, unregistered class produces a slug-only file, malformed trace skipped.
- Existing gates unchanged: `scripts/audit_leak.py memory_store/okf` clean; `pytest -q` green.

## Rollout (git-safety aware)

The pass commits `git add memory_store/okf … && git commit` every round on the shared working tree/branch, so concurrent commits risk `index.lock` contention.

1. **Now (no git, no okf writes):** implement `vocab.py`, `build_taxonomy.py`, and the tests; verify green. Adding new files is invisible to the running workers/consolidator (they import only `task_card`/`consolidate`/`memory_api`).
2. **In an idle window (just after a consolidation, ~30 min gap) or after the pass finishes:** run `build_taxonomy.py --all` backfill, edit the consolidator prompt (step 4b), commit once. From then on each round maintains the census.

## Expected effect

Backfill grows `vuln-classes/` from 9 to ~18 canonical files, filling `out-of-bounds-read` (89), `stack-buffer-overflow-write` (22), `integer-overflow`, `null-pointer-dereference`, `type-confusion`, etc., and converging fragmented spellings onto canonical keys; `strategies/` keys align to the canonical set with the free-form tail collapsed.

## Out of scope (YAGNI)

- No change to `causal-policies/`, `formats/`, `harnesses/`, or the verifier-gated promotion logic.
- No per-class win-rate feeding into policy ranking.
- No retroactive renaming of existing `causal-policies` filenames.
- No worker-prompt change (workers already read `okf/**`; richer coverage is transparent to them).
