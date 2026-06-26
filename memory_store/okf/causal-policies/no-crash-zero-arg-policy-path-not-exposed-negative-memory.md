---
type: causal-policy
title: No Crash Zero Arg Policy Path Not Exposed Negative Memory
description: Negative memory for no_crash with verifier signal zero_arg_policy_path_not_exposed.
failure_class: no_crash
verifier_signal: zero_arg_policy_path_not_exposed
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, zero-arg-policy-path-not-exposed, negative_memory]
match_keys: [no-crash, zero-arg-policy-path-not-exposed, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Zero Arg Policy Path Not Exposed Negative Memory

- key: `no_crash x zero_arg_policy_path_not_exposed`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: sudo-policy-text

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Procedure
Use the diagnosis as a selector map: keep the valid base, then change the missing protocol/table/module state rather than increasing file size or randomizing payload bytes.

## Diagnosed Dead Ends
- The policy fuzzer is line-oriented and initializes user/settings state, but it injects a default command when no argv entry is supplied, preventing the zero-argument policy path that would leave a static command string to be freed.

## Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote the diagnosis into a recovery until a later verifier-confirmed candidate flips the official gate.
