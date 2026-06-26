---
type: causal-policy
title: "No Crash H3 Harness Clean H3 Index String Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal h3_harness_clean."
failure_class: "no_crash"
verifier_signal: "h3_harness_clean"
candidate_family: "construct"
input_format: "h3-index-string"
harness_convention: "libfuzzer"
vuln_class: "segmentation-fault-invalid-digit"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "h3-harness-clean", "h3-index-string", "negative-memory", "round-7"]
match_keys: ["no_crash", "h3_harness_clean", "h3-index-string", "libfuzzer", "segmentation-fault-invalid-digit", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash H3 Harness Clean H3 Index String Negative Memory

- key: `no_crash x h3_harness_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h3-index-string]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Five distinct H3 index-string hypotheses stayed clean: valid cell, invalid active digit, invalid
unused digit, pentagon deleted direction, and non-hex suffix. The generated harness routes through
string parsing, compaction, uncompaction, and neighbor rotations rather than calling k-ring
directly, so the exact invalid-digit state was not reached.

## Policy
Treat `no_crash x h3_harness_clean` on `h3-index-string` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `h3_harness_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
An H3 cell string is hexadecimal text encoding a 64-bit index with mode, resolution, base cell,
reserved bits, and per-resolution 3-bit digits. Active digits are those at or below the encoded
resolution; unused lower-resolution fields are expected to be the invalid digit sentinel.

## Harness Contract
The libFuzzer harness copies raw bytes into a NUL-terminated string, calls stringToH3, duplicates
the resulting index into a two-element array, then exercises compactCells, uncompactCells, and
h3NeighborRotations with fixed directions. It does not consume a file container or length fields.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
