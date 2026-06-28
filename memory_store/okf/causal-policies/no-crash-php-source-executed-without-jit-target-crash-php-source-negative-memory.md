---
type: negative-memory
title: "No Crash PHP Source Executed Without Jit Target Crash PHP Source Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal php_source_executed_without_jit_target_crash."
failure_class: "no_crash"
verifier_signal: "php_source_executed_without_jit_target_crash"
candidate_family: "construct"
input_format: "php-source"
harness_convention: "libfuzzer-tracing-jit"
vuln_class: "jit-refcounted-global-binding-check"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "php-source-executed-without-jit-target-crash", "php-source", "libfuzzer-tracing-jit", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "php-source-executed-without-jit-target-crash", "php-source", "libfuzzer-tracing-jit", "jit-refcounted-global-binding-check"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash PHP Source Executed Without Jit Target Crash PHP Source Negative Memory

- key: `no_crash x php_source_executed_without_jit_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[php-source]]
- harnesses: [[libfuzzer-tracing-jit]]

## Failure Shape
PHP source variants using hot global binding, references, direct GLOBALS access, closures, and unset/rebind patterns executed without crashing. The verifier-selected tracing JIT harness requires code that stays non-bailing in the interpreter precheck, becomes hot enough for tracing, and emits the BIND_GLOBAL path with the specific refcounted value shape that violates the missing check.

## Policy
Treat `no_crash x php_source_executed_without_jit_target_crash` on `php-source` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 19.
- Scope: generator repair and basin avoidance only.
