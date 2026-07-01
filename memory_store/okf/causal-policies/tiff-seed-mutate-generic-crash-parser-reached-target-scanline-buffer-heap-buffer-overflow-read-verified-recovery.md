---
type: causal-policy
title: "Tiff Seed Mutate Generic Crash Parser Reached Target Scanline Buffer Heap Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / parser_reached_target_scanline_buffer."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_scanline_buffer"
candidate_family: "seed_mutate"
input_format: "tiff"
harness_convention: "honggfuzz-libfuzzer-image-prefix"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "seed-mutate", "tiff", "heap-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "parser-reached-target-scanline-buffer", "tiff", "honggfuzz-libfuzzer-image-prefix", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Tiff Seed Mutate Generic Crash Parser Reached Target Scanline Buffer Heap Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `parser_reached_target_scanline_buffer` on `tiff` under `honggfuzz-libfuzzer-image-prefix`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Start from a valid in-repo gray+alpha TIFF seed and preserve its image data, dimensions, sample count, bit depth, extra-sample alpha metadata, strip metadata, and compression.
2. Add the harness image-control prefix, then mutate only the TIFF planar-layout relation so libtiff reports a per-plane scanline while Leptonica's gray+alpha conversion still reads interleaved gray/alpha pairs.
3. The vulnerable build allocates the smaller scanline buffer and reads past it during RGBA conversion; the fixed build rejects the inconsistent scanline relation.

## Format Contract
- Input format: [[tiff]].
- Harness contract: [[honggfuzz-libfuzzer-image-prefix]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `tiff` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.
