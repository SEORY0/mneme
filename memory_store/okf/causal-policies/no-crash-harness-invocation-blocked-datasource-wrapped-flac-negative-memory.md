---
type: causal-policy
title: "No Crash Harness Invocation Blocked Datasource Wrapped Flac Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal harness_invocation_blocked."
failure_class: "no_crash"
verifier_signal: "harness_invocation_blocked"
candidate_family: "seed_mutate_then_construct"
input_format: "datasource-wrapped-flac"
harness_convention: "libfuzzer-flac-decoder-datasource"
vuln_class: "flac-subframe-predictor-order"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "harness-invocation-blocked", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "seed-mutate-then-construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "harness-invocation-blocked", "datasource-wrapped-flac", "libfuzzer-flac-decoder-datasource", "flac-subframe-predictor-order"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Harness Invocation Blocked Datasource Wrapped Flac Negative Memory

- key: `no_crash x harness_invocation_blocked`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[datasource-wrapped-flac]]
- harnesses: [[libfuzzer-flac-decoder-datasource]]

## Dead-End Shape
Datasource-wrapped valid FLAC seeds and control-flow variants could not be meaningfully evaluated locally because the wrapper reported a required corpus directory rather than executing the file as a single input. No official submit was made without a local parser signal.

## Policy
For `no_crash x harness_invocation_blocked` on `datasource-wrapped-flac`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate_then_construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x harness_invocation_blocked` appears for `datasource-wrapped-flac`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
2. Preserve any proven format or harness envelope, but change the missing gate, state relation, or sink path before another official submission.
3. Prefer a different construction family if the same verifier signal repeats without new parser-depth evidence.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for recovery policies; local crash class is supporting evidence only.

## Negative Memory
- Do not resubmit candidates that are clean, off-target, rejected before the target path, or crashing both fixed and vulnerable images in this same shape.
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Preserve only descriptive format and harness facts from this failed attempt.

## Evidence Shape
- Support: one diagnosed round 24 persistent failure.
- Scope: generator repair and retargeting only.
