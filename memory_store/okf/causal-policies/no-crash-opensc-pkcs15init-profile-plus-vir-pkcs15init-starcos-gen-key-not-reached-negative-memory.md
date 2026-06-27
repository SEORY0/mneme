---
type: causal-policy
title: "No Crash Opensc Pkcs15init Profile Plus Vir Pkcs15init Starcos Gen Key Not Reached Negative Memory"
description: "Negative memory for no_crash with pkcs15init_starcos_gen_key_not_reached on opensc-pkcs15init-profile-plus-virtual-reader-stream inputs."
failure_class: no_crash
verifier_signal: pkcs15init_starcos_gen_key_not_reached
candidate_family: construct
input_format: opensc-pkcs15init-profile-plus-virtual-reader-stream
harness_convention: libfuzzer
vuln_class: missing-status-word-check
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pkcs15init-starcos-gen-key-not-reached, opensc-pkcs15init-profile-plus-virtual-reader-stream, missing-status-word-check, negative_memory]
match_keys: [no-crash, pkcs15init-starcos-gen-key-not-reached, opensc-pkcs15init-profile-plus-virtual-reader-stream, missing-status-word-check]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Opensc Pkcs15init Profile Plus Vir Pkcs15init Starcos Gen Key Not Reached Negative Memory

- key: `no_crash x pkcs15init_starcos_gen_key_not_reached`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[opensc-pkcs15init-profile-plus-virtual-reader-stream]]

## Dead End
A simple virtual-card chunk stream with a Starcos-like ATR and APDU status responses did not reach the vulnerable key-generation path. The missing state is likely the pkcs15init profile and operation parameters that select Starcos key generation before the reader transcript returns SW1 success with a non-success SW2.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
