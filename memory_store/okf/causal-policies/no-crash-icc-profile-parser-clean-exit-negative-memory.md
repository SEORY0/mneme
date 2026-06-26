---
type: causal-policy
title: No Crash Icc Profile Parser Clean Exit Negative Memory
description: Negative memory for no_crash with verifier signal icc_profile_parser_clean_exit.
failure_class: no_crash
verifier_signal: icc_profile_parser_clean_exit
candidate_family: seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, icc-profile-parser-clean-exit, negative_memory]
match_keys: [no-crash, icc-profile-parser-clean-exit, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Icc Profile Parser Clean Exit Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x icc_profile_parser_clean_exit`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-mutate
- observed_formats: icc-profile

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- Seed ICC profiles were accepted by the profile fuzzer and exercised raw-tag reads plus save-to-file behavior, but the attempts did not produce inconsistent per-table node counts that survive profile loading and fail during profile writing.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
