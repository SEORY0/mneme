---
type: negative-memory
title: "Generic Crash Generic Non Target Canon Ciff Crw Construct Memory Safety Crash Negative Memory"
description: "Round 23 negative memory for generic_crash with verifier signal generic_non_target."
failure_class: "generic_crash"
verifier_signal: "generic_non_target"
candidate_family: "construct"
input_format: "canon-ciff-crw"
harness_convention: "libfuzzer-rawspeed-ciff-parser"
vuln_class: "memory-safety-crash"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "generic-non-target", "canon-ciff-crw", "libfuzzer-rawspeed-ciff-parser", "construct", "negative-memory", "round-23"]
match_keys: ["generic-crash", "generic-non-target", "canon-ciff-crw", "libfuzzer-rawspeed-ciff-parser", "memory-safety-crash"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 23
---
# Generic Crash Generic Non Target Canon Ciff Crw Construct Memory Safety Crash Negative Memory

- key: `generic_crash x generic_non_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[canon-ciff-crw]]
- harnesses: [[libfuzzer-rawspeed-ciff-parser]]

## Failure Shape
Synthetic Canon CIFF inputs could pass initial parser gates and sometimes crashed the local target, but the crash was not an official target match and did not reproduce as a vulnerable-image failure on submit. No real CRW seed was available in the extracted tree, so the decompressor-specific row/column invariant was not reliably reached.

## Policy
Treat `generic_crash x generic_non_target` on `canon-ciff-crw` as negative memory for the attempted carrier. Preserve only reachability that was actually observed, then retarget the missing gate, harness contract, or sink-specific state before spending more verification attempts.

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
