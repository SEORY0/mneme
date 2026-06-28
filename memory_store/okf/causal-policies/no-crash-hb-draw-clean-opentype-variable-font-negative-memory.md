---
type: negative-memory
title: "No Crash Hb Draw Clean Opentype Variable Font Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal hb-draw-clean."
failure_class: "no-crash"
verifier_signal: "hb-draw-clean"
candidate_family: "seed-mutate"
input_format: "opentype-variable-font"
harness_convention: "afl-hb-draw-fuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "hb-draw-clean", "opentype-variable-font", "afl-hb-draw-fuzzer", "seed-mutate", "negative-memory", "round-21"]
match_keys: ["no-crash", "hb-draw-clean", "opentype-variable-font", "afl-hb-draw-fuzzer", "out-of-bounds-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Hb Draw Clean Opentype Variable Font Negative Memory

- key: `no-crash x hb-draw-clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opentype-variable-font]]
- harnesses: [[afl-hb-draw-fuzzer]]

## Failure Shape
Real variable-font seeds with gvar tables stayed clean after single-relation mutations to glyph variation offsets, both before and after appending the harness tail that enables a variation coordinate. The likely missing piece is selecting a glyph path whose outline drawing actually consumes the malformed GlyphVarData span.

## Policy
Treat `no-crash x hb-draw-clean` on `opentype-variable-font` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
