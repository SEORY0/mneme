---
type: causal-policy
title: No Crash Parser Reached Non Target Path Negative Memory
description: Negative memory for no_crash with verifier signal parser_reached_non_target_path.
failure_class: no_crash
verifier_signal: parser_reached_non_target_path
candidate_family: seed-mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, parser-reached-non-target-path, negative_memory]
match_keys: [no-crash, parser-reached-non-target-path, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Parser Reached Non Target Path Negative Memory

- key: `no_crash x parser_reached_non_target_path`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-mutate
- observed_formats: mdl

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- A valid MDL5 seed reached the Assimp importer, but mutating the apparent embedded texture dimensions led to importer warnings and normal rejection/post-processing rather than the vulnerable material-loader allocation path. The remaining gap is identifying the precise skin lump or texture record consumed by MDLMaterialLoader.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
