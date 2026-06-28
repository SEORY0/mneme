---
type: causal-policy
title: "Generic Crash Sink Mismatch Or Wrapper False Positive Tiff Negative Memory"
description: "Round 24 negative memory for generic_crash with verifier signal sink_mismatch_or_wrapper_false_positive."
failure_class: "generic_crash"
verifier_signal: "sink_mismatch_or_wrapper_false_positive"
candidate_family: "seed_mutate_then_construct"
input_format: "tiff"
harness_convention: "libfuzzer-graphicsmagick-coder"
vuln_class: "uninitialized-opacity-channel"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "sink-mismatch-or-wrapper-false-positive", "tiff", "libfuzzer-graphicsmagick-coder", "seed-mutate-then-construct", "negative-memory", "round-24"]
match_keys: ["generic-crash", "sink-mismatch-or-wrapper-false-positive", "tiff", "libfuzzer-graphicsmagick-coder", "uninitialized-opacity-channel"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# Generic Crash Sink Mismatch Or Wrapper False Positive Tiff Negative Memory

- key: `generic_crash x sink_mismatch_or_wrapper_false_positive`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[tiff]]
- harnesses: [[libfuzzer-graphicsmagick-coder]]

## Dead-End Shape
A real stripped TIFF seed and constructed classic TIFF envelopes reached the TIFF reader, and a YCbCr stripped fallback family produced a local generic crash, but official submit treated the vulnerable build as clean. Other constructed photometric/sample-format variants parsed without exposing the uninitialized opacity state.

## Policy
For `generic_crash x sink_mismatch_or_wrapper_false_positive` on `tiff`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate_then_construct` only while this format and harness contract are present.

## Procedure
1. When `generic_crash x sink_mismatch_or_wrapper_false_positive` appears for `tiff`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
