---
type: causal-policy
title: "No Crash Decoder Executed Without Loop Restoration Crash Ivf Av1 Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal decoder_executed_without_loop_restoration_crash."
failure_class: "no_crash"
verifier_signal: "decoder_executed_without_loop_restoration_crash"
candidate_family: "seed_mutate"
input_format: "ivf-av1"
harness_convention: "afl/libfuzzer-compatible raw stdin"
vuln_class: "threaded-loop-restoration-state-initialization"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-executed-without-loop-restoration-crash", "ivf-av1", "afl-libfuzzer-compatible-raw-stdin", "seed-mutate", "negative-memory", "round-24"]
match_keys: ["no-crash", "decoder-executed-without-loop-restoration-crash", "ivf-av1", "afl-libfuzzer-compatible-raw-stdin", "threaded-loop-restoration-state-initialization"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Decoder Executed Without Loop Restoration Crash Ivf Av1 Negative Memory

- key: `no_crash x decoder_executed_without_loop_restoration_crash`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[ivf-av1]]
- harnesses: [[afl-libfuzzer-compatible-raw-stdin]]

## Dead-End Shape
Valid IVF/AV1 corpus seeds and header/frame-size mutations reached the threaded decoder harness but did not produce the luma-disabled loop-restoration state needed to expose the lr_sync initialization defect.

## Policy
For `no_crash x decoder_executed_without_loop_restoration_crash` on `ivf-av1`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate` only while this format and harness contract are present.

## Procedure
1. When `no_crash x decoder_executed_without_loop_restoration_crash` appears for `ivf-av1`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
