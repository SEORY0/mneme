---
type: causal-policy
title: "No Crash Parser Reached No Target Error Opentype Font Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_reached_no_target_error."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_error"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-ots"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-error", "opentype-font", "libfuzzer-ots", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-reached-no-target-error", "opentype-font", "libfuzzer-ots", "use-after-free"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Reached No Target Error Opentype Font Negative Memory

- key: `no_crash x parser_reached_no_target_error`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[opentype-font]]
- harnesses: [[libfuzzer-ots]]

## Dead-End Shape
Multiple real OTS fuzzing font seeds, including TrueType, OpenType, and collection inputs, parsed without triggering the stream Write/WriteRaw aliasing UAF. The attempts likely did not force a serialization path where Write receives a pointer into the stream buffer that is reallocated by WriteRaw.

## Policy
For `no_crash x parser_reached_no_target_error` on `opentype-font`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_reached_no_target_error` appears for `opentype-font`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
