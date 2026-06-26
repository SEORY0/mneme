---
type: causal-policy
title: No Crash Parser Rejected Or Clean Compile Negative Memory
description: Negative memory for no_crash with verifier signal parser_rejected_or_clean_compile.
failure_class: no_crash
verifier_signal: parser_rejected_or_clean_compile
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-rejected-or-clean-compile, negative_memory]
match_keys: [no-crash, parser-rejected-or-clean-compile, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Rejected Or Clean Compile Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x parser_rejected_or_clean_compile`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: lwan-template

### Procedure
The parser or executor ran, but the target state was absent. Keep the valid envelope and retarget the semantic selector, state transition, table kind, or option named by the diagnosis.

### Diagnosed Dead Ends
- Tried malformed and crossed template sections to make post-processing walk unmatched control chunks. The parser either rejected the syntax before post-processing or compiled cleanly, so the sentinel-comparison invariant was not violated.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
