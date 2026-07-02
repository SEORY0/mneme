---
type: causal-policy
title: "No Crash Hb Draw Clean Opentype Variable Font Out Of Bounds Read Negative Memory"
description: "Negative memory for persistent no_crash / hb_draw_clean basin."
failure_class: "no_crash"
verifier_signal: "hb_draw_clean"
candidate_family: "seed_mutate"
input_format: "opentype-variable-font"
harness_convention: "afl-hb-draw-fuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "seed-mutate", "opentype-variable-font", "out-of-bounds-read", "negative-memory"]
match_keys: ["no-crash", "hb-draw-clean", "opentype-variable-font", "afl-hb-draw-fuzzer", "out-of-bounds-read", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Hb Draw Clean Opentype Variable Font Out Of Bounds Read Negative Memory

## Policy
For `no_crash` with verifier signal `hb_draw_clean` on `opentype-variable-font` under `afl-hb-draw-fuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- Valid variable-font seeds reached the draw harness but stayed clean.
- Attempts covered an avar segment-map boundary, physical final-table placement, larger file-boundary placement, existing crash/variable-font corpus seeds, a gvar glyph-extent mutation for an early drawn glyph, and fake post-extent gvar data.
- The likely unresolved gate is a glyph variation span that is both consumed by one of the first drawn glyphs and detected by the sanitizer as crossing the declared variation-data extent.

## Recovery Direction
- Keep the parser/harness reachability facts in [[opentype-variable-font]] and [[afl-hb-draw-fuzzer]].
- Retarget away from the failed relation named by `hb_draw_clean`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
