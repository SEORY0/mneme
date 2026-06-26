---
type: causal-policy
title: No Crash Template Parser Rejected Or Clean Exit Negative Memory
description: Negative memory for no_crash with verifier signal template_parser_rejected_or_clean_exit.
failure_class: no_crash
verifier_signal: template_parser_rejected_or_clean_exit
candidate_family: construct-seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, template-parser-rejected-or-clean-exit, negative_memory]
match_keys: [no-crash, template-parser-rejected-or-clean-exit, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Template Parser Rejected Or Clean Exit Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x template_parser_rejected_or_clean_exit`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct-seed-mutate
- observed_formats: lwan-template

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- Valid template seeds and constructed nested section/variable templates reached the compile-only template harness, but either compiled cleanly or were rejected by parser balance and symbol checks before any overflow was observed.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
