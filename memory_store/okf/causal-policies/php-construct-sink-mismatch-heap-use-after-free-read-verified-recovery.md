---
type: causal-policy
title: "PHP Construct Sink Mismatch Heap Use After Free Read Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal sink_mismatch."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch"
candidate_family: "construct"
input_format: "php"
harness_convention: "libfuzzer"
vuln_class: "heap-use-after-free-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "sink-mismatch", "php", "libfuzzer", "construct", "heap-use-after-free-read", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "sink_mismatch", "php", "libfuzzer", "heap-use-after-free-read", "wrong-sink", "sink-mismatch", "php", "libfuzzer", "heap-use-after-free-read", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# PHP Construct Sink Mismatch Heap Use After Free Read Verified Recovery

- key: `wrong_sink x sink_mismatch`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[php]]
- related harness facts: [[libfuzzer]]

## Policy
For `wrong_sink x sink_mismatch` on `php`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Feed raw PHP source to the execution fuzzer. Use a compound divide assignment whose left operand is a runtime-allocated numeric string, not an interned literal, make the divisor convert to zero, and consume the assignment expression's result so the VM copies the in-place result after the division failure. This keeps parsing and execution valid while violating only the failed in-place conversion/division invariant.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[php]]: The input is not a container format: the libFuzzer buffer is compiled and executed as PHP source, with a size cap in the execution fuzzer. PHP opening tags are accepted, and normal try/catch syntax can keep ordinary arithmetic errors from aborting before sanitizer handling. Literal strings may be interned, while strings created at runtime are heap allocated.
- Harness [[libfuzzer]]: The harness is libFuzzer over raw bytes. It rejects oversized inputs, then passes the complete byte buffer to the PHP fuzzer SAPI as one request and executes it under a step limit. There is no front/back byte carving or FuzzedDataProvider contract.

## Negative Memory
- Do not corrupt the outer `php` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[php]] and [[libfuzzer]].
