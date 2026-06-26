---
type: causal-policy
title: Local Crash Official Clean Negative Memory
description: Negative memory for local sanitizer or process crashes that do not reproduce as vulnerable-only official crashes.
failure_class: generic_crash
verifier_signal: sanitizer_or_process_crash_then_official_clean
candidate_family: seed_mutate
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [generic_crash, official_clean, local_crash_off_target, negative_memory]
match_keys: [generic_crash, sanitizer_or_process_crash_then_official_clean, local_crash_off_target, local_crash_not_reproduced_officially]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
related: [local-crash-server-clean-negative-memory]
---
## Policy
A local crash followed by official clean or target mismatch is negative memory for that candidate family. Treat it as an off-target or environment-specific basin unless a later candidate changes the semantic gate and reproduces as vulnerable-only.

## Procedure
1. Record the local-crash family as non-helping when official verification is clean.
2. Remove mutations that only damage the outer header or generic decoder path.
3. Recenter on the task's named invariant: slice coverage, extra-channel state, Unicode isolate state, allocation frame, or debug-record initialization.
4. Require stable local reproduction before any second submit.
5. Prefer a new format-valid carrier over minimizing the off-target crash.

## Negative Memory
- Do not keep submitting variants of a local-only crash.
- Do not call an official-clean crash progress unless the semantic gate changed.
- Do not preserve malformed-header crashes when the diagnosis says a valid specialized carrier is required.

## Evidence Shape
- Support: multiple diagnosed round failures with local-crash but official-clean signals.
- Scope: generator repair only.
