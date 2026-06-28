---
type: negative-memory
title: "No Crash Pkcs15init Usage Or Clean Opensc Pkcs15init Reader Chunk Stream Iasecc Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal pkcs15init-usage-or-clean."
failure_class: "no-crash"
verifier_signal: "pkcs15init-usage-or-clean"
candidate_family: "construct"
input_format: "opensc-pkcs15init-reader-chunk-stream-iasecc"
harness_convention: "honggfuzz-pkcs15init"
vuln_class: "length-check-missing"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pkcs15init-usage-or-clean", "opensc-pkcs15init-reader-chunk-stream-iasecc", "honggfuzz-pkcs15init", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "pkcs15init-usage-or-clean", "opensc-pkcs15init-reader-chunk-stream-iasecc", "honggfuzz-pkcs15init", "length-check-missing"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Pkcs15init Usage Or Clean Opensc Pkcs15init Reader Chunk Stream Iasecc Negative Memory

- key: `no-crash x pkcs15init-usage-or-clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-pkcs15init-reader-chunk-stream-iasecc]]
- harnesses: [[honggfuzz-pkcs15init]]

## Failure Shape
Bare ASN.1/CRT TLVs and a simple reader chunk stream only reached the pkcs15init harness usage/clean path. The missing state is a complete pkcs15init argument/profile plus virtual-reader response flow that binds an IASECC card and reaches CRT parsing.

## Policy
Treat `no-crash x pkcs15init-usage-or-clean` on `opensc-pkcs15init-reader-chunk-stream-iasecc` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

## Procedure
1. Keep any parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, feature gate, length relation, stateful subobject, or official target sink.
3. Change one relation at a time and reject variants that return to this same clean-exit, off-target, usage-only, both-crash, or nonreproducible basin.
4. Promote a recovery from this basin only after a later server-confirmed target match.

## Negative Memory
- Do not resubmit another candidate with this exact failure signal unless it changes the causal gate being tested.
- Do not broaden random mutation after reachability is known; move to the smallest missing format or state contract.
- Do not treat local generic crashes, wrapper usage paths, clean parser exits, fixed-build crashes, or wrong-sink labels as success.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 21.
- Scope: generator repair and basin avoidance only.
