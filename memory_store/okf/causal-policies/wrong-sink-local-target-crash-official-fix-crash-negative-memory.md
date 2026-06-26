---
type: causal-policy
title: Wrong Sink Local Target Crash Official Fix Crash Negative Memory
description: Negative memory for wrong_sink with verifier signal local_target_crash_official_fix_crash.
failure_class: wrong_sink
verifier_signal: local_target_crash_official_fix_crash
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [wrong-sink, local-target-crash-official-fix-crash, negative_memory]
match_keys: [wrong-sink, local-target-crash-official-fix-crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Wrong Sink Local Target Crash Official Fix Crash Negative Memory

## Policy
Treat this verifier signal as negative memory for the attempted candidate family. Preserve any parser reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Round 4 Reinforcement
- key: `wrong_sink x local_target_crash_official_fix_crash`
- outcome: persistent failure basin
- support_count: 1
- candidate_families: construct
- observed_formats: stun

### Procedure
Quarantine the crash basin. A candidate that also fails the fixed build or is rejected by the server is negative evidence; shrink back to target-specific state rather than amplifying the crash.

### Diagnosed Dead Ends
- A structurally valid STUN message with a message-integrity attribute reached the HMAC comparison and produced the intended uninitialized-value signal locally. Official submission rejected it because the fixed side also exited nonzero, so the envelope was not accepted as a differential PoC.

### Negative Memory
Do not repeat the same carrier plus broad mutation after this signal. Do not promote this basin into a recovery until a later verifier-confirmed candidate flips the official gate.
