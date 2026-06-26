---
type: causal-policy
title: No Crash Local Wrapper Usage Only Negative Memory
description: Negative memory for no_crash with verifier signal local_wrapper_usage_only.
failure_class: no_crash
verifier_signal: local_wrapper_usage_only
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, local-wrapper-usage-only, negative_memory]
match_keys: [no-crash, local-wrapper-usage-only, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Local Wrapper Usage Only Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `no_crash x local_wrapper_usage_only`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: pkcs15-reader-chunks

### Procedure
Treat this as an envelope or harness-shape failure. Rebuild the carrier around the exact fuzzer input contract, confirm parser reachability, then add one target invariant.

### Diagnosed Dead Ends
- The selected OpenSC target is the PKCS#15 reader fuzzer, whose input should be length-prefixed simulated reader chunks. Both a direct ASN.1 object and a chunked Italian-CNS ATR/APDU sequence only made the local wrapper print honggfuzz usage, so the harness did not execute the parser path far enough to evaluate the pkcs15-itacns boundary condition.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
