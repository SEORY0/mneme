---
type: causal-policy
title: "No Crash Compressor Executed Clean Zstd Simple Compress Fuzzer Bytes Negative Memory"
description: "Round 13 negative memory for no_crash with verifier signal compressor_executed_clean."
failure_class: "no_crash"
verifier_signal: "compressor_executed_clean"
candidate_family: "construct"
input_format: "zstd-simple-compress-fuzzer-bytes"
harness_convention: "honggfuzz/libfuzzer-style raw bytes to simple_compress"
vuln_class: "compressor-optimal-parser-state-bug"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "compressor-executed-clean", "zstd-simple-compress-fuzzer-bytes", "negative-memory", "round-13"]
match_keys: ["no_crash", "compressor_executed_clean", "zstd-simple-compress-fuzzer-bytes", "honggfuzz/libfuzzer-style raw bytes to simple_compress", "compressor-optimal-parser-state-bug", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 13
---
# No Crash Compressor Executed Clean Zstd Simple Compress Fuzzer Bytes Negative Memory

- key: `no_crash x compressor_executed_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[zstd-simple-compress-fuzzer-bytes]]
- related harness facts: [[honggfuzz-libfuzzer-style-raw-bytes-to-simple-compress]]

## Failure Shape
The harness was reached and compression executed, but tested raw source shapes and parameter suffixes did not trigger a sanitizer crash. The missing condition is likely a narrower repeated-match/repcode state relation inside the high-compression optimal parser rather than just selecting a high compression level.

## Policy
Treat `no_crash x compressor_executed_clean` on `zstd-simple-compress-fuzzer-bytes` as a basin to avoid unless a new candidate changes the specific parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `compressor_executed_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
The input is not a zstd frame. The fuzzer treats a prefix of the raw bytes as source data to compress and consumes suffix bytes as parameter data. Repetitive source prefixes are valid inputs; zstd magic or compressed frames have no special meaning to this target except as ordinary source bytes.

## Harness Contract
The target creates a FUZZ_dataProducer over the whole input, consumes bytes from the back to choose how much of the front remains as source data, then consumes more back bytes to choose destination capacity and compression level. It calls ZSTD_compressCCtx and accepts only dstSize_tooSmall as an expected error. There is no checksum, file wrapper, or FuzzedDataProvider object beyond this back-consuming suffix contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
## Round 13 Failure Reinforcement

- key: `no_crash x compressor_executed_clean`
- related format facts: [[zstd-simple-compress-fuzzer-bytes]]
- related harness facts: [[honggfuzz-libfuzzer-style-raw-bytes-to-simple-compress]]

### Failure Shape Delta
The harness was reached and compression executed, but tested raw source shapes and parameter suffixes did not trigger a sanitizer crash. The missing condition is likely a narrower repeated-match/repcode state relation inside the high-compression optimal parser rather than just selecting a high compression level.

### Format Contract Delta
The input is not a zstd frame. The fuzzer treats a prefix of the raw bytes as source data to compress and consumes suffix bytes as parameter data. Repetitive source prefixes are valid inputs; zstd magic or compressed frames have no special meaning to this target except as ordinary source bytes.

### Harness Contract Delta
The target creates a FUZZ_dataProducer over the whole input, consumes bytes from the back to choose how much of the front remains as source data, then consumes more back bytes to choose destination capacity and compression level. It calls ZSTD_compressCCtx and accepts only dstSize_tooSmall as an expected error. There is no checksum, file wrapper, or FuzzedDataProvider object beyond this back-consuming suffix contract.

### Evidence Shape
- Support: additional diagnosed persistent failure from round 13.
- Scope: generator repair and basin avoidance only.
