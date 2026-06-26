---
type: causal-policy
title: No Crash Target Harness Not Tiff Reader Negative Memory
description: Negative memory for no_crash with verifier signal target_harness_not_tiff_reader.
failure_class: no_crash
verifier_signal: target_harness_not_tiff_reader
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, target-harness-not-tiff-reader, negative_memory]
match_keys: [no-crash, target-harness-not-tiff-reader, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Target Harness Not Tiff Reader Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x target_harness_not_tiff_reader`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: tiff

### Procedure
Treat this as an envelope or harness-shape failure. Rebuild the carrier around the exact fuzzer input contract, confirm parser reachability, then add one target invariant.

### Diagnosed Dead Ends
- A minimal uncompressed grayscale-plus-alpha TIFF envelope was built with image and alpha tags, but the local verifier invoked a different image-transform fuzzer path and did not reach the described TIFF scanline reader.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
