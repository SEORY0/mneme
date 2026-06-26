---
type: causal-policy
title: Generic Crash Harness Mismatch Off Target Crash Negative Memory
description: Negative memory for generic_crash with verifier signal harness_mismatch_off_target_crash.
failure_class: generic_crash
verifier_signal: harness_mismatch_off_target_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, harness-mismatch-off-target-crash, negative_memory]
match_keys: [generic-crash, harness-mismatch-off-target-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Harness Mismatch Off Target Crash Negative Memory

- key: `generic_crash x harness_mismatch_off_target_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: xcf

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Quarantine the crashing basin. Shrink or discard the off-target crash and retarget the described sink; never submit a candidate that also fails on the fixed image.

## Diagnosed Dead Ends
- A structured XCF-like candidate was built to reach a layer level after tile-image allocation and then return through an exceptional compression path, but local verification invoked the PNG coder fuzzer rather than the XCF coder. The only local crash was off-target and did not reproduce as an official vulnerable-image failure.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
