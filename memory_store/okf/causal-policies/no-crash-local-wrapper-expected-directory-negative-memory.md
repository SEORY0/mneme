---
type: causal-policy
title: No Crash Local Wrapper Expected Directory Negative Memory
description: Negative memory for no_crash with verifier signal local_wrapper_expected_directory.
failure_class: no_crash
verifier_signal: local_wrapper_expected_directory
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, local-wrapper-expected-directory, negative_memory]
match_keys: [no-crash, local-wrapper-expected-directory, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Local Wrapper Expected Directory Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x local_wrapper_expected_directory`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: xml

### Procedure
Treat this as an envelope or harness-shape failure. Rebuild the carrier around the exact fuzzer input contract, confirm parser reachability, then add one target invariant.

### Diagnosed Dead Ends
- A small XML document using entity expansion and namespace scope changes was constructed for the XML Reader namespace-lifetime path. The local wrapper reported that it expected a directory input rather than the supplied file, so the parser path was not exercised and no target signal was available.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
