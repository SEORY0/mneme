---
type: causal-policy
title: "Generic Crash Target Mismatch Runtime Harness Mismatch Jpeg Card But Qpdf Runtime Negative Memory"
description: "Round 6 negative memory for generic_crash with verifier signal target_mismatch_runtime_harness_mismatch."
failure_class: "generic_crash"
verifier_signal: "target_mismatch_runtime_harness_mismatch"
candidate_family: "construct"
input_format: "jpeg-card-but-qpdf-runtime"
harness_convention: "libfuzzer"
vuln_class: "progressive-jpeg-uninitialized-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "target-mismatch-runtime-harness-mismatch", "jpeg-card-but-qpdf-runtime", "negative-memory", "round-6"]
match_keys: ["generic_crash", "target_mismatch_runtime_harness_mismatch", "jpeg-card-but-qpdf-runtime", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 6
---
# Generic Crash Target Mismatch Runtime Harness Mismatch Jpeg Card But Qpdf Runtime Negative Memory

- key: `generic_crash x target_mismatch_runtime_harness_mismatch`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg-card-but-qpdf-runtime]]

## Failure Shape
- The task card described a progressive JPEG smoothing bug, but the runtime exercised a qpdf fuzzer. A tiny JPEG-shaped input produced an off-target vulnerable-side crash locally and official submission rejected it; a PDF-shaped input did not crash. This looks like a card/runtime mismatch rather than a reachable JPEG task in this run directory.

## Policy
Treat `generic_crash x target_mismatch_runtime_harness_mismatch` on this format family as negative memory for the attempted carrier. Preserve only verifier-proven reachability, then retarget the missing gate or sink-specific state instead of resubmitting candidates with the same signal.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or nonreproducible basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, or wrong-sink labels as success.
- Do not broaden random mutation after reachability is known; move to the smallest missing format contract.
- Do not submit another candidate with this exact failure signal unless the candidate changes the causal gate being tested.
- Do not store raw payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: 1 diagnosed persistent failure(s) from round 6.
- Scope: generator repair and basin avoidance only.
