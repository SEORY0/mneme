---
type: negative-memory
title: "No Crash Pkcs15 Crypt Target Completed Or Usage Only Opensc Virtual Reader Chunk Stream Iasecc Negative Memory"
description: "Round 19 negative memory for no_crash with verifier signal pkcs15_crypt_target_completed_or_usage_only."
failure_class: "no_crash"
verifier_signal: "pkcs15_crypt_target_completed_or_usage_only"
candidate_family: "construct"
input_format: "opensc-virtual-reader-chunk-stream-iasecc"
harness_convention: "honggfuzz/libfuzzer-compatible"
vuln_class: "buffer-length-validation"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15-crypt-target-completed-or-usage-only", "opensc-virtual-reader-chunk-stream-iasecc", "honggfuzz-libfuzzer-compatible", "construct", "negative-memory", "round-19"]
match_keys: ["no-crash", "pkcs15-crypt-target-completed-or-usage-only", "opensc-virtual-reader-chunk-stream-iasecc", "honggfuzz-libfuzzer-compatible", "buffer-length-validation"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 19
---
# No Crash Pkcs15 Crypt Target Completed Or Usage Only Opensc Virtual Reader Chunk Stream Iasecc Negative Memory

- key: `no_crash x pkcs15_crypt_target_completed_or_usage_only`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-virtual-reader-chunk-stream-iasecc]]
- harnesses: [[honggfuzz-libfuzzer-compatible]]

## Failure Shape
A structurally valid split buffer and virtual-reader stream did not reach an IASECC buffer-length violation. The missing piece is a recognized IASECC card/application state plus APDU responses that expose a length-bearing cryptographic or PKCS#15 object whose advertised size is inconsistent with the actual returned buffer.

## Policy
Treat `no_crash x pkcs15_crypt_target_completed_or_usage_only` on `opensc-virtual-reader-chunk-stream-iasecc` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
