---
type: causal-policy
title: No Crash Pin Change Cleanup Not Reached Negative Memory
description: Negative memory for no_crash with verifier signal pin_change_cleanup_not_reached.
failure_class: no_crash
verifier_signal: pin_change_cleanup_not_reached
candidate_family: seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pin-change-cleanup-not-reached, negative_memory]
match_keys: [no-crash, pin-change-cleanup-not-reached, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Pin Change Cleanup Not Reached Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x pin_change_cleanup_not_reached`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-mutate
- observed_formats: argv-envelope-plus-virtual-smart-card-apdu-trace

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- The argv envelope for the vulnerable PIN-change command was satisfied, and an in-tree virtual-reader seed was tried. The candidate did not reach the successful PIN-change cleanup path where option-backed PIN buffers are freed before the harness later frees the argument strings.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
