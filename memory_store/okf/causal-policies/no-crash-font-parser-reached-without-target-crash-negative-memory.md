---
type: causal-policy
title: No Crash Font Parser Reached Without Target Crash Negative Memory
description: Negative memory for no_crash with verifier signal font_parser_reached_without_target_crash.
failure_class: no_crash
verifier_signal: font_parser_reached_without_target_crash
candidate_family: seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, font-parser-reached-without-target-crash, negative_memory]
match_keys: [no-crash, font-parser-reached-without-target-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Font Parser Reached Without Target Crash Negative Memory

- key: `no_crash x font_parser_reached_without_target_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-mutate
- observed_formats: sfnt-font

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- A valid corpus font exercised the shape fuzzer but did not contain the malformed AAT offset structure needed to dereference an unchecked table offset before validation.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
