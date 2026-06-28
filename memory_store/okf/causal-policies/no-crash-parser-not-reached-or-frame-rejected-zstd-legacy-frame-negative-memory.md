---
type: causal-policy
title: "No Crash Parser Not Reached Or Frame Rejected Zstd Legacy Frame Negative Memory"
description: "Round 7 negative memory for no_crash with verifier signal parser_not_reached_or_frame_rejected."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_frame_rejected"
candidate_family: "construct"
input_format: "zstd-legacy-frame"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-frame-rejected", "zstd-legacy-frame", "negative-memory", "round-7"]
match_keys: ["no_crash", "parser_not_reached_or_frame_rejected", "zstd-legacy-frame", "libfuzzer", "heap-buffer-overflow-write", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 7
---
# No Crash Parser Not Reached Or Frame Rejected Zstd Legacy Frame Negative Memory

- key: `no_crash x parser_not_reached_or_frame_rejected`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zstd-legacy-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed legacy v0.2 and v0.4 frames with old magic values, a compressed block, and an oversized
raw-literals section intended to exceed the fixed literal buffer. The decompression harness rejected
or exited without an observable crash, suggesting another frame-header gate or block/sequences
invariant still needs to be satisfied.

## Policy
Treat `no_crash x parser_not_reached_or_frame_rejected` on `zstd-legacy-frame` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_not_reached_or_frame_rejected`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Format Contract
Legacy zstd frames begin with a version-specific magic and then block headers. Compressed blocks
contain a literals sub-block before sequence data. Raw-literals headers encode a literal byte count,
and the vulnerable code path copies literals to an internal fixed-size literal buffer when the
declared raw literal count fits within the compressed block.

## Harness Contract
The local wrapper ran the simple decompression libFuzzer target on raw file bytes. No outer file
format or length prefix is used, but the decompressor performs legacy-frame and block-header
validation before reaching literal decoding.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 7.
- Scope: generator repair and basin avoidance only.
