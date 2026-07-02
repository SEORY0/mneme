---
type: causal-policy
title: "Opentype Font Construct No Crash Local Verify Harness Path Unusable Official Submit Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Verified recovery distilled from a round trace for no_crash / local_verify_harness_path_unusable; official_submit_target_match."
failure_class: "no_crash"
verifier_signal: "local_verify_harness_path_unusable; official_submit_target_match"
candidate_family: "construct"
input_format: "opentype-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "opentype-font", "heap-buffer-overflow-write", "verified-recovery"]
match_keys: ["no-crash", "local-verify-harness-path-unusable-official-submit-target-match", "opentype-font", "libfuzzer", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Opentype Font Construct No Crash Local Verify Harness Path Unusable Official Submit Target Match Heap Buffer Overflow Write Verified Recovery

## Policy
For `no_crash` with verifier signal `local_verify_harness_path_unusable; official_submit_target_match` on `opentype-font` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a valid SFNT font that maps the harness-selected text to one glyph.
2. Add a GSUB alternate substitution so subsetting retains many widely spaced glyphs, then add a GPOS pair-position format-2 lookup whose first class definition covers those retained glyphs compactly in the source.
3. Let normal subsetting renumber the retained sparse glyphs into a dense output range, which makes the class definition choose format 1 during serialization.
4. The source GPOS table remains small enough that the subset size estimate undershoots the dense output class array, so the unchecked class-array allocation failure is followed by writes past the serializer buffer.

## Format Contract
- Input format: [[opentype-font]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `opentype-font` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
