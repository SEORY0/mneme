---
type: causal-policy
title: No Crash Rar Parser Reached Without State Failure Negative Memory
description: Negative memory for no_crash with verifier signal rar_parser_reached_without_state_failure.
failure_class: no_crash
verifier_signal: rar_parser_reached_without_state_failure
candidate_family: seed-sweep
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, rar-parser-reached-without-state-failure, negative_memory]
match_keys: [no-crash, rar-parser-reached-without-state-failure, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Rar Parser Reached Without State Failure Negative Memory

- key: `no_crash x rar_parser_reached_without_state_failure`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-sweep
- observed_formats: rar

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Prioritized valid RAR and PPMd-oriented archive seeds reached the archive harness but did not create the failing compressed-data return followed by continued header processing with stale PPMd state. A useful next mutation should preserve a multi-block PPMd archive envelope while corrupting a later compressed block so the reader fails mid-stream and then advances to subsequent archive metadata.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
