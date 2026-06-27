---
type: causal-policy
title: "Generic Crash Roundtrip Abort Both Images Raw Lzxpress Roundtrip Plain Bytes Negative Memory"
description: "Round 12 negative memory for generic_crash with verifier signal roundtrip_abort_both_images."
failure_class: "generic_crash"
verifier_signal: "roundtrip_abort_both_images"
candidate_family: "construct"
input_format: "raw-lzxpress-roundtrip-plain-bytes"
harness_convention: "honggfuzz-style-file"
vuln_class: "buffer-overflow-or-allocation-size-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "roundtrip-abort-both-images", "raw-lzxpress-roundtrip-plain-bytes", "negative-memory", "round-12"]
match_keys: ["generic_crash", "roundtrip_abort_both_images", "raw-lzxpress-roundtrip-plain-bytes", "honggfuzz-style-file", "buffer-overflow-or-allocation-size-error", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# Generic Crash Roundtrip Abort Both Images Raw Lzxpress Roundtrip Plain Bytes Negative Memory

- key: `generic_crash x roundtrip_abort_both_images`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[raw-lzxpress-roundtrip-plain-bytes]]
- related harness facts: [[honggfuzz-style-file]]

## Failure Shape
A large incompressible raw buffer caused the round-trip fuzzer to abort locally, but the fixed image also exited nonzero. This likely hit the generic round-trip mismatch/failure condition rather than the intended compressed-buffer allocation bug.

## Policy
Treat `generic_crash x roundtrip_abort_both_images` on `raw-lzxpress-roundtrip-plain-bytes` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
The fuzzer input is the uncompressed byte string. The target compresses it with LZXpress into an internal compressed buffer, immediately decompresses the result into an internal output buffer, and checks size and byte equality.

## Harness Contract
There is no file header or selector. Inputs over the decompressed buffer capacity are ignored. A crash can come from the target bug or from the harness aborting when compression/decompression does not round-trip exactly, so official fixed-image behavior is essential.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `roundtrip_abort_both_images`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
