---
type: negative-memory
title: "No Crash Validation Error Without Sanitizer Crash Unit Json Config Construct Buffer Under Read Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal validation_error_without_sanitizer_crash."
failure_class: "no_crash"
verifier_signal: "validation_error_without_sanitizer_crash"
candidate_family: "construct"
input_format: "unit-json-config"
harness_convention: "libfuzzer"
vuln_class: "buffer-under-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "validation-error-without-sanitizer-crash", "unit-json-config", "libfuzzer", "construct", "negative-memory", "round-23"]
match_keys: ["no-crash", "validation-error-without-sanitizer-crash", "unit-json-config", "libfuzzer", "buffer-under-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Validation Error Without Sanitizer Crash Unit Json Config Construct Buffer Under Read Negative Memory

- key: `no_crash x validation_error_without_sanitizer_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[unit-json-config]]
- harnesses: [[libfuzzer]]

## Failure Shape
JSON configs with colon-starting listener addresses reached Unit's address validation and produced invalid-address errors, but the byte before the copied address remained readable under the pool allocator. Upstream/server address variants and longer colon-starting names also failed to make the under-read sanitizer-visible.

## Policy
Treat `no_crash x validation_error_without_sanitizer_crash` on `unit-json-config` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
- Support: 1 diagnosed persistent failure from round 23 after 7 attempts.
- Scope: generator repair and basin avoidance only.
