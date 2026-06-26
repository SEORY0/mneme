---
type: causal-policy
title: "UCL Configuration Construct Target Sink Crash Local Mislabeled Heap Buffer Overflow Read Verified Recovery"
description: "Round 8 verified recovery for wrong_sink with verifier signal target_sink_crash_local_mislabeled."
failure_class: "wrong_sink"
verifier_signal: "target_sink_crash_local_mislabeled"
candidate_family: "construct"
input_format: "ucl configuration"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "target-sink-crash-local-mislabeled", "ucl-configuration", "construct", "verified-recovery", "round-8"]
match_keys: ["wrong_sink", "target_sink_crash_local_mislabeled", "ucl configuration", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 8
---
# UCL Configuration Construct Target Sink Crash Local Mislabeled Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x target_sink_crash_local_mislabeled`, preserve the format and harness gates that reached the target path, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Use a built-in macro path rather than an ordinary key/value assignment, because macro arguments are expanded even when the harness has not registered user variables. Make the macro argument terminate immediately after a bare variable marker so expansion calls the variable checker with its cursor at the end of the buffer.
2. Keep the carrier abstract: preserve the gate/invariant relation, not task-local bytes, offsets, checksums, or submission metadata.
3. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- UCL supports ordinary assignments and dot-prefixed built-in macros. Ordinary scalar values may avoid variable expansion when no variables are registered, while macro values go through the expansion routine directly. Multiline-string syntax reaches a separate parser path and can produce off-target crashes.
- Harness: The fuzzer passes raw bytes to ucl_parser_add_string with an explicit length. It does not add variables, does not prepend a selector, and does not use FuzzedDataProvider carving.

## Negative Memory
- Do not broaden mutations after the parser/harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin.
