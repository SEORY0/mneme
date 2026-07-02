---
type: causal-policy
title: "Opentype Font Seed Mutate Wrong Sink Parser Reached Gvar Glyph Var Data Overread Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for wrong_sink / parser_reached_gvar_glyph_var_data_overread_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_gvar_glyph_var_data_overread_official_target_match"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "seed-mutate", "opentype-font", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["wrong-sink", "parser-reached-gvar-glyph-var-data-overread-official-target-match", "opentype-font", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Opentype Font Seed Mutate Wrong Sink Parser Reached Gvar Glyph Var Data Overread Official Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink` with verifier signal `parser_reached_gvar_glyph_var_data_overread_official_target_match` on `opentype-font` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a real variable OpenType font that already reaches glyph drawing.
2. Preserve the sfnt table directory, glyph tables, variation axes, and glyph count gates.
3. Mutate one glyph variation-data span so the start is accepted as in-range but the claimed span reaches past the valid gvar backing data, then keep variation coordinates present so glyph drawing applies deltas.
4. The vulnerable build iterates tuple/shared-point data beyond the gvar buffer; the fixed build rejects or bounds the span.

## Format Contract
- Input format: [[opentype-font]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `opentype-font` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
