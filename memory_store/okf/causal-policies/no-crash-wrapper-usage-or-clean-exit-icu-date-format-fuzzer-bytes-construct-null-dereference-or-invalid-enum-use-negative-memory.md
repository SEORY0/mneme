---
type: negative-memory
title: "No Crash Wrapper Usage Or Clean Exit Icu Date Format Fuzzer Bytes Construct Null Dereference Or Invalid Enum Use Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal wrapper_usage_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "wrapper_usage_or_clean_exit"
candidate_family: "construct"
input_format: "icu-date-format-fuzzer-bytes"
harness_convention: "honggfuzz/libfuzzer wrapper"
vuln_class: "null-dereference-or-invalid-enum-use"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "wrapper-usage-or-clean-exit", "icu-date-format-fuzzer-bytes", "honggfuzz-libfuzzer-wrapper", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "wrapper-usage-or-clean-exit", "icu-date-format-fuzzer-bytes", "honggfuzz-libfuzzer-wrapper", "null-dereference-or-invalid-enum-use"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Wrapper Usage Or Clean Exit Icu Date Format Fuzzer Bytes Construct Null Dereference Or Invalid Enum Use Negative Memory

- key: `no_crash x wrapper_usage_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[icu-date-format-fuzzer-bytes]]
- harnesses: [[honggfuzz-libfuzzer-wrapper]]

## Failure Shape
Invalid dateStyle/timeStyle values across negative, relative-style, just-out-of-range, and very large enum families did not produce the expected vulnerable exit. The local wrapper mostly emitted a honggfuzz usage banner, and the official submit of an invalid-style candidate exited cleanly.

## Policy
Treat `no_crash x wrapper_usage_or_clean_exit` on `icu-date-format-fuzzer-bytes` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser, envelope, or harness contract that the trace showed was reached.
2. Identify the missing causal relation from the verifier signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, nonreproducible, or both-crash basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 23 after 12 attempts.
- Scope: generator repair and basin avoidance only.
