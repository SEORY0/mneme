---
type: negative-memory
title: "No Crash Harness Contract Mismatch Jpeg Seed Mutate Coverage Regression Memory Safety Negative Memory"
description: "Round 23 negative memory for no_crash with verifier signal harness_contract_mismatch."
failure_class: "no_crash"
verifier_signal: "harness_contract_mismatch"
candidate_family: "seed_mutate"
input_format: "jpeg"
harness_convention: "libfuzzer-libjpeg-turbo-transform"
vuln_class: "coverage-regression-memory-safety"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "harness-contract-mismatch", "jpeg", "libfuzzer-libjpeg-turbo-transform", "seed-mutate", "negative-memory", "round-23"]
match_keys: ["no-crash", "harness-contract-mismatch", "jpeg", "libfuzzer-libjpeg-turbo-transform", "coverage-regression-memory-safety"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# No Crash Harness Contract Mismatch Jpeg Seed Mutate Coverage Regression Memory Safety Negative Memory

- key: `no_crash x harness_contract_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg]]
- harnesses: [[libfuzzer-libjpeg-turbo-transform]]

## Failure Shape
Multiple valid JPEG seeds and a directory-shaped candidate did not execute the transform fuzzer under the local verifier; the wrapper reported that its expected input path must be a directory. No parser-level signal was obtained, so this task remained blocked at the verifier/input-contract layer rather than the JPEG transform logic.

## Policy
Treat `no_crash x harness_contract_mismatch` on `jpeg` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
- Support: 1 diagnosed persistent failure from round 23 after 5 attempts.
- Scope: generator repair and basin avoidance only.
