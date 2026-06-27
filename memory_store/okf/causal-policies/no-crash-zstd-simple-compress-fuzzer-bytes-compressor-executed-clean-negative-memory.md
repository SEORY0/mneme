---
type: causal-policy
title: "No Crash Zstd Simple Compress Fuzzer Bytes Compressor Executed Clean Negative Memory"
description: "Negative memory for no_crash with compressor_executed_clean on zstd-simple-compress-fuzzer-bytes inputs."
failure_class: no_crash
verifier_signal: compressor_executed_clean
candidate_family: construct
input_format: zstd-simple-compress-fuzzer-bytes
harness_convention: "honggfuzz/libfuzzer-style raw bytes to simple_compress"
vuln_class: compressor-optimal-parser-state-bug
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, compressor-executed-clean, zstd-simple-compress-fuzzer-bytes, compressor-optimal-parser-state-bug, negative_memory]
match_keys: [no-crash, compressor-executed-clean, zstd-simple-compress-fuzzer-bytes, compressor-optimal-parser-state-bug]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Zstd Simple Compress Fuzzer Bytes Compressor Executed Clean Negative Memory

- key: `no_crash x compressor_executed_clean`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[zstd-simple-compress-fuzzer-bytes]]

## Dead End
The harness was reached and compression executed, but tested raw source shapes and parameter suffixes did not trigger a sanitizer crash. The missing condition is likely a narrower repeated-match/repcode state relation inside the high-compression optimal parser rather than just selecting a high compression level.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
