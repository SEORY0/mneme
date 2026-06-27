---
type: causal-policy
title: "Generic Crash Local Crash Official Clean Swift Protobuf Text Format Negative Memory"
description: "Round 12 negative memory for generic_crash with verifier signal local_crash_official_clean."
failure_class: "generic_crash"
verifier_signal: "local_crash_official_clean"
candidate_family: "construct"
input_format: "swift-protobuf-text-format"
harness_convention: "libfuzzer"
vuln_class: "scanner-state-parse-bug"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-crash-official-clean", "swift-protobuf-text-format", "negative-memory", "round-12"]
match_keys: ["generic_crash", "local_crash_official_clean", "swift-protobuf-text-format", "libfuzzer", "scanner-state-parse-bug", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 12
---
# Generic Crash Local Crash Official Clean Swift Protobuf Text Format Negative Memory

- key: `generic_crash x local_crash_official_clean`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[swift-protobuf-text-format]]
- related harness facts: [[libfuzzer]]

## Failure Shape
The known ending-minus style and several numeric-field text-format variants mostly failed cleanly. Two variants produced a local process crash, but official submission reported the vulnerable build clean, so the local crash was not the benchmark target. The missing condition is a text-format parse context where the minus-sign scanner advancement becomes externally unsafe rather than just a parse error.

## Policy
Treat `generic_crash x local_crash_official_clean` on `swift-protobuf-text-format` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
SwiftProtobuf text format accepts numeric field tags and named fields with colon-separated values. Floating values recognize nan/inf/infinity spellings with optional sign. The bug is in optional-infinity scanning, where a leading minus can advance the scanner before a later spelling check fails.

## Harness Contract
The fuzzer may consume a small leading options prefix when the input starts with the options sentinel; otherwise the bytes are interpreted as UTF-8 text format. It parses into a generated fuzz message and serializes or validates the message if parsing succeeds.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_crash_official_clean`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 12.
- Scope: generator repair and basin avoidance only.
