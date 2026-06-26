---
type: causal-policy
title: No Crash Card Driver Sequence Not Target Crashing Negative Memory
description: Negative memory for no_crash with verifier signal card_driver_sequence_not_target_crashing.
failure_class: no_crash
verifier_signal: card_driver_sequence_not_target_crashing
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, card-driver-sequence-not-target-crashing, negative_memory]
match_keys: [no-crash, card-driver-sequence-not-target-crashing, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Card Driver Sequence Not Target Crashing Negative Memory

- key: `no_crash x card_driver_sequence_not_target_crashing`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: opensc-fuzzer-reader-apdu-trace

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- The APDU trace matched a CardOS ATR and supplied later directory-list responses, but the crafted malformed file information block did not reach or destabilize the vulnerable list-files parser.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
