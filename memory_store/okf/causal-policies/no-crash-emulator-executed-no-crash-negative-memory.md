---
type: causal-policy
title: No Crash Emulator Executed No Crash Negative Memory
description: Negative memory for no_crash with verifier signal emulator_executed_no_crash.
failure_class: no_crash
verifier_signal: emulator_executed_no_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, emulator-executed-no-crash, negative_memory]
match_keys: [no-crash, emulator-executed-no-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Emulator Executed No Crash Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x emulator_executed_no_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: x86-machine-code

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- The x86 emulator harness accepts raw instruction bytes and does not expose CPU model selection. CPUID instruction streams executed without process failure, so the hardcoded-CPU semantic mismatch could not be converted into the required vul/fix crash differential.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
