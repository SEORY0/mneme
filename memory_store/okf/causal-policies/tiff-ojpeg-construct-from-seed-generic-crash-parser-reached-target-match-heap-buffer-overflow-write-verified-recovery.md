---
type: causal-policy
title: "Tiff Ojpeg Construct From Seed Generic Crash Parser Reached Target Match Heap Buffer Overflow Write Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct_from_seed"
input_format: "tiff-ojpeg"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct-from-seed", "tiff-ojpeg", "heap-buffer-overflow-write", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-target-match", "tiff-ojpeg", "libfuzzer", "heap-buffer-overflow-write", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Tiff Ojpeg Construct From Seed Generic Crash Parser Reached Target Match Heap Buffer Overflow Write Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_target_match` on `tiff-ojpeg` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a structurally valid legacy JPEG-in-TIFF carrier rather than changing only the compression field of a modern TIFF.
2. Preserve the legacy JPEG interchange and strip relationships from a real sample, keep the image metadata coherent enough for the old-JPEG decode path, then declare a grayscale sub-byte sample depth so the RGBA fallback writes byte-sized pixels into a low-depth Pix allocation.

## Format Contract
- Input format: [[tiff-ojpeg]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `tiff-ojpeg` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
