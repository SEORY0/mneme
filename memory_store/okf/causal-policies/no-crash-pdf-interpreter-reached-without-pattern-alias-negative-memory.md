---
type: causal-policy
title: No Crash Pdf Interpreter Reached Without Pattern Alias Negative Memory
description: Negative memory for no_crash with verifier signal pdf_interpreter_reached_without_pattern_alias.
failure_class: no_crash
verifier_signal: pdf_interpreter_reached_without_pattern_alias
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pdf-interpreter-reached-without-pattern-alias, negative_memory]
match_keys: [no-crash, pdf-interpreter-reached-without-pattern-alias, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Pdf Interpreter Reached Without Pattern Alias Negative Memory

- key: `no_crash x pdf_interpreter_reached_without_pattern_alias`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: pdf

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- A generic PDF graphics-state stress input reached the Ghostscript raster harness but did not create nested circular pattern reuse with a soft mask and mismatched color-space buffer sizing. A viable candidate needs a valid PDF object graph with a reusable pattern resource, nested pattern reference cycle, and a soft-mask group whose inner and outer color spaces differ.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
