---
type: causal-policy
title: "No Crash Javascript Evaluated No Native Fault Javascript Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal javascript_evaluated_no_native_fault."
failure_class: "no_crash"
verifier_signal: "javascript_evaluated_no_native_fault"
candidate_family: "construct"
input_format: "javascript"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "javascript-evaluated-no-native-fault", "javascript", "negative-memory", "round-9"]
match_keys: ["no_crash", "javascript_evaluated_no_native_fault", "javascript", "libfuzzer", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Javascript Evaluated No Native Fault Javascript Negative Memory

- key: `no_crash x javascript_evaluated_no_native_fault`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[javascript]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Raw JavaScript regexp boundary assertions on empty and end-of-string subjects executed without
  crashing.
- The attempted cases likely exercised the safe word-boundary executor path; a more precise trigger
  may need a specific compiled regexp shape or cursor state rather than ordinary boundary tests.

## Policy
Treat `no_crash x javascript_evaluated_no_native_fault` on `javascript` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The input format is plain JavaScript source.
- RegExp literals and RegExp constructor calls are parsed and compiled by Hermes before execution;
  JavaScript exceptions are swallowed by the harness.

## Harness Contract
- The libFuzzer target receives raw bytes, rejects Hermes bytecode, appends a terminator for the
  source buffer, creates a Hermes runtime, evaluates the source, and catches JSI exceptions.
- There is no input carving or FuzzedDataProvider contract.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `javascript_evaluated_no_native_fault`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
