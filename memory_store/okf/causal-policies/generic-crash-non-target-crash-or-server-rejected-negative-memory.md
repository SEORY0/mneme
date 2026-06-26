---
type: causal-policy
title: Generic Crash Non Target Crash Or Server Rejected Negative Memory
description: Negative memory for generic_crash with verifier signal non_target_crash_or_server_rejected.
failure_class: generic_crash
verifier_signal: non_target_crash_or_server_rejected
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [generic-crash, non-target-crash-or-server-rejected, negative_memory]
match_keys: [generic-crash, non-target-crash-or-server-rejected, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Generic Crash Non Target Crash Or Server Rejected Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `generic_crash x non_target_crash_or_server_rejected`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: pdf

### Procedure
Quarantine the crash basin. A candidate that also fails the fixed build or is rejected by the server is negative evidence; shrink back to target-specific state rather than amplifying the crash.

### Diagnosed Dead Ends
- A minimal encrypted PDF with an intentionally malformed Standard security dictionary produced a local crash signal, but the official server reported no vulnerable-build crash. The likely missing gate is a linearized or hint-table path that queries the security handler's encryption algorithm after the handler was created from an incomplete dictionary.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
