---
type: causal-policy
title: No Crash Generated Ruby No Target Crash Negative Memory
description: Negative memory for no_crash with verifier signal generated_ruby_no_target_crash.
failure_class: no_crash
verifier_signal: generated_ruby_no_target_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, generated-ruby-no-target-crash, negative_memory]
match_keys: [no-crash, generated-ruby-no-target-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Generated Ruby No Target Crash Negative Memory

- key: `no_crash x generated_ruby_no_target_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: protobuf-text

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- The harness accepts protobuf text and generates Ruby from a restricted schema. Valid assignment and array builtin programs executed, but the schema did not expose a direct way to suspend minor GC in the required sweep state while performing the write-barrier operation.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
