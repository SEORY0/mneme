---
type: causal-policy
title: No Crash Pkcs15 Reader Reached Without Cflex Path Underflow Negative Memory
description: Negative memory for no_crash with verifier signal pkcs15_reader_reached_without_cflex_path_underflow.
failure_class: no_crash
verifier_signal: pkcs15_reader_reached_without_cflex_path_underflow
candidate_family: seed-sweep
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, pkcs15-reader-reached-without-cflex-path-underflow, negative_memory]
match_keys: [no-crash, pkcs15-reader-reached-without-cflex-path-underflow, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Pkcs15 Reader Reached Without Cflex Path Underflow Negative Memory

- key: `no_crash x pkcs15_reader_reached_without_cflex_path_underflow`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: seed-sweep
- observed_formats: smartcard-pkcs15

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- Existing PKCS#15 reader corpus entries did not select the CardFlex path handling case with an unchecked short path length. A useful next input should preserve the reader envelope while selecting CardFlex-specific object metadata and providing a path object whose declared length is below the parser's subtraction assumption.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
