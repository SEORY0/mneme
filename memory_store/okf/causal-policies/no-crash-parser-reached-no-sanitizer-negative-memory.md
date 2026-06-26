---
type: causal-policy
title: No Crash Parser Reached No Sanitizer Negative Memory
description: Negative memory for no_crash with verifier signal parser_reached_no_sanitizer.
failure_class: no_crash
verifier_signal: parser_reached_no_sanitizer
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-no-sanitizer, negative_memory]
match_keys: [no-crash, parser-reached-no-sanitizer, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Reached No Sanitizer Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x parser_reached_no_sanitizer`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: audio-container

### Procedure
Use the signal as a selector map: preserve any reachability it proved, then change the missing protocol/table/module state before changing sizes or payload bytes.

### Diagnosed Dead Ends
- Constructed small RIFF/WAV-family envelopes to exercise binary-header reads, including short extended and compressed format chunks. The files opened or failed cleanly and did not leave the targeted binary-header state uninitialized in a sanitizer-visible way.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
