---
type: causal-policy
title: No Crash Reader Path Reached No Target State Negative Memory
description: Negative memory for no_crash with verifier signal reader_path_reached_no_target_state.
failure_class: no_crash
verifier_signal: reader_path_reached_no_target_state
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, reader-path-reached-no-target-state, negative_memory]
match_keys: [no-crash, reader-path-reached-no-target-state, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Reader Path Reached No Target State Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x reader_path_reached_no_target_state`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: smartcard-apdu-chunks

### Procedure
Use the signal as a selector map: preserve any reachability it proved, then change the missing protocol/table/module state before changing sizes or payload bytes.

### Diagnosed Dead Ends
- Used the harness chunked reader format with an ATR and repeated successful APDU-style responses containing an empty ASN.1 ACL-like object. The simulated card did not bind deeply enough into the IAS/ECC empty-ACL path to trigger the stack overwrite.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
