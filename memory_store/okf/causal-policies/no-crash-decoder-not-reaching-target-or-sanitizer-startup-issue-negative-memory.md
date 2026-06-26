---
type: causal-policy
title: No Crash Decoder Not Reaching Target Or Sanitizer Startup Issue Negative Memory
description: Negative memory for no_crash with verifier signal decoder_not_reaching_target_or_sanitizer_startup_issue.
failure_class: no_crash
verifier_signal: decoder_not_reaching_target_or_sanitizer_startup_issue
candidate_family: seed-probe
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, decoder-not-reaching-target-or-sanitizer-startup-issue, negative_memory]
match_keys: [no-crash, decoder-not-reaching-target-or-sanitizer-startup-issue, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Decoder Not Reaching Target Or Sanitizer Startup Issue Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x decoder_not_reaching_target_or_sanitizer_startup_issue`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-probe
- observed_formats: jxl

### Procedure
Use the signal as a selector map: preserve any reachability it proved, then change the missing protocol/table/module state before changing sizes or payload bytes.

### Diagnosed Dead Ends
- A synthetic JXL container header did not reach the decoder state needed for per-rect YCbCr upsampling. A checked-in cropped/blending JXL seed was closer to the described path, but local execution failed before useful target feedback with a sanitizer shadow-memory startup error, leaving the late-FIR upsampling invariant untested.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
