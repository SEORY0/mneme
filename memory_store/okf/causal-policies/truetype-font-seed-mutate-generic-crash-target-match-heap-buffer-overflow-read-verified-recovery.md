---
type: causal-policy
title: "Truetype Font Seed Mutate Generic Crash Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / target_match."
failure_class: "generic_crash"
verifier_signal: "target_match"
candidate_family: "seed_mutate"
input_format: "truetype-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "seed-mutate", "truetype-font", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "target-match", "truetype-font", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Truetype Font Seed Mutate Generic Crash Target Match Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `target_match` on `truetype-font` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a valid variable TrueType font.
2. Keep the outline-location data capable of resolving a physically present high-numbered glyph, make a low-numbered drawn glyph composite-reference that high glyph, and declare a smaller glyph count for maxp and gvar so the gvar per-glyph offset array is shorter than the composite target.
3. Provide variation coordinates through the draw harness tail so glyph drawing applies gvar deltas while recursing into the high component.

## Format Contract
- Input format: [[truetype-font]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `truetype-font` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
