---
type: causal-policy
title: No Crash Decoded Or Rejected Without Order Crash Negative Memory
description: Negative memory for no_crash with verifier signal decoded_or_rejected_without_order_crash.
failure_class: no_crash
verifier_signal: decoded_or_rejected_without_order_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, decoded-or-rejected-without-order-crash, negative_memory]
match_keys: [no-crash, decoded-or-rejected-without-order-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Decoded Or Rejected Without Order Crash Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x decoded_or_rejected_without_order_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: open62541-binary

### Procedure
Use the signal as a selector map: preserve any reachability it proved, then change the missing protocol/table/module state before changing sizes or payload bytes.

### Diagnosed Dead Ends
- Constructed inputs using the fuzzer's memory-limit prefix, type selector, and compact binary values for pointer-carrying builtin types. Candidates either decoded and compared cleanly or were rejected before the generic ordering routine dereferenced invalid state.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
