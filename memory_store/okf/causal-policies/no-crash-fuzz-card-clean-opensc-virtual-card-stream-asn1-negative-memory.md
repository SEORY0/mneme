---
type: negative-memory
title: "No Crash Fuzz Card Clean Opensc Virtual Card Stream Asn1 Negative Memory"
description: "Round 21 negative memory for no-crash with verifier signal fuzz-card-clean."
failure_class: "no-crash"
verifier_signal: "fuzz-card-clean"
candidate_family: "construct"
input_format: "opensc-virtual-card-stream-asn1"
harness_convention: "libfuzzer"
vuln_class: "invalid-memory-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "fuzz-card-clean", "opensc-virtual-card-stream-asn1", "libfuzzer", "construct", "negative-memory", "round-21"]
match_keys: ["no-crash", "fuzz-card-clean", "opensc-virtual-card-stream-asn1", "libfuzzer", "invalid-memory-access"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 21
---
# No Crash Fuzz Card Clean Opensc Virtual Card Stream Asn1 Negative Memory

- key: `no-crash x fuzz-card-clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[opensc-virtual-card-stream-asn1]]
- harnesses: [[libfuzzer]]

## Failure Shape
Standalone BER/DER sequences, long-length ASN.1 forms, CRT-like TLVs, and a simple virtual-reader chunk stream did not drive the card fuzzer into the ASN.1 buffer-pointer bug. The missing gate is card-driver selection and APDU response state before ASN.1 parsing.

## Policy
Treat `no-crash x fuzz-card-clean` on `opensc-virtual-card-stream-asn1` as negative memory for the attempted carrier. Preserve only the reachability that was actually observed, then retarget the missing gate or sink-specific state before spending more verification attempts.

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
