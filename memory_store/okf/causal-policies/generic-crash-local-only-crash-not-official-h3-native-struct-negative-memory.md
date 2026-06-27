---
type: causal-policy
title: "Generic Crash Local Only Crash Not Official H3 Native Struct Negative Memory"
description: "Round 17 negative memory for generic_crash with verifier signal local_only_crash_not_official."
failure_class: "generic_crash"
verifier_signal: "local_only_crash_not_official"
candidate_family: "construct"
input_format: "h3-native-struct"
harness_convention: "libfuzzer-raw-struct"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "local-only-crash-not-official", "h3-native-struct", "libfuzzer-raw-struct", "negative-memory", "round-17"]
match_keys: ["generic-crash", "local-only-crash-not-official", "h3-native-struct", "libfuzzer-raw-struct", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 17
---
# Generic Crash Local Only Crash Not Official H3 Native Struct Negative Memory

- key: `generic_crash x local_only_crash_not_official`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[h3-native-struct]]
- related harness facts: [[libfuzzer-raw-struct]]

## Failure Shape
- Several H3 index and vertex-number combinations produced local wrapper-level crashes, but official submission exited cleanly.
- The missing invariant is likely a valid cell/vertex ownership edge case that reaches cellToVertex with an initialized-looking index while still exposing the uninitialized value.

## Policy
Treat `generic_crash x local_only_crash_not_official` on `h3-native-struct` as a basin to avoid unless a new candidate changes the parser gate, state relation, or target-sink relation described above. Preserve any proven reachability, but discard variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to this same basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `local_only_crash_not_official`.
- Do not count parser reachability, local wrapper crashes, both-image crashes, or clean exits as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[h3-native-struct]] for descriptive format gates and invariants.

## Harness Contract
Use [[libfuzzer-raw-struct]] for the input-carving contract.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 17.
- Scope: generator repair and basin avoidance only.
