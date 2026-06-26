---
type: causal-policy
title: Generic Crash Generic Crash Not Target Match Negative Memory
description: Negative memory for generic_crash with verifier signal generic_crash_not_target_match.
failure_class: generic_crash
verifier_signal: generic_crash_not_target_match
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, generic-crash-not-target-match, negative_memory]
match_keys: [generic-crash, generic-crash-not-target-match, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Generic Crash Not Target Match Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `generic_crash x generic_crash_not_target_match`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: libxml2-xml-fuzzer-entity-envelope

### Procedure
Quarantine the crash basin. A candidate that also fails the fixed build or is rejected by the server is negative evidence; shrink back to target-specific state rather than amplifying the crash.

### Diagnosed Dead Ends
- The XML fuzzer envelope and main-document entity gate were satisfied, including a zero byte in character data near a push-parser chunk boundary. The local run produced a generic crash, but official submission did not match the vulnerable/fixed differential target, so the crash was not the described progress-check failure.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
