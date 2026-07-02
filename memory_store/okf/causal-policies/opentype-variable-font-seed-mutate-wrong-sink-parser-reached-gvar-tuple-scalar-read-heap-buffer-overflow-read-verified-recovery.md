---
type: causal-policy
title: "Opentype Variable Font Seed Mutate Wrong Sink Parser Reached Gvar Tuple Scalar Read Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_gvar_tuple_scalar_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_gvar_tuple_scalar_read"
candidate_family: "seed_mutate"
input_format: "opentype-variable-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "seed-mutate", "opentype-variable-font", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-gvar-tuple-scalar-read", "opentype-variable-font", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Opentype Variable Font Seed Mutate Wrong Sink Parser Reached Gvar Tuple Scalar Read Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_gvar_tuple_scalar_read` on `opentype-variable-font` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a complete in-repo variable-font seed so the SFNT table directory, glyph data, variation axis table, and glyph variation table gates are all satisfied.
2. Preserve the gvar offset-array and glyph-selection path, but make one glyph variation record declare an embedded peak tuple while its record span ends after the fixed tuple header.
3. Ensure the harness supplies a variation coordinate, causing glyph delta application to read the missing tuple coordinate; the fixed build rejects the incomplete tuple data.

## Format Contract
- Input format: [[opentype-variable-font]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `opentype-variable-font` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
A full seed was required because a hand-built font would need many coherent OpenType table relationships before HarfBuzz reaches gvar delta application. Mutating only the glyph variation span kept the parser on the intended path and avoided unrelated font validation failures.
