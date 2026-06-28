---
type: causal-policy
title: "No Crash Decoder Reached No Target Error Ffmpeg Target Decoder Vp6f Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal decoder_reached_no_target_error."
failure_class: "no_crash"
verifier_signal: "decoder_reached_no_target_error"
candidate_family: "seed_mutate_then_construct"
input_format: "ffmpeg-target-decoder-vp6f"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "uninitialized-video-buffer"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "decoder-reached-no-target-error", "ffmpeg-target-decoder-vp6f", "libfuzzer-ffmpeg-target-decoder", "seed-mutate-then-construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "decoder-reached-no-target-error", "ffmpeg-target-decoder-vp6f", "libfuzzer-ffmpeg-target-decoder", "uninitialized-video-buffer"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Decoder Reached No Target Error Ffmpeg Target Decoder Vp6f Negative Memory

- key: `no_crash x decoder_reached_no_target_error`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[ffmpeg-target-decoder-vp6f]]
- harnesses: [[libfuzzer-ffmpeg-target-decoder]]

## Dead-End Shape
VP6F sample packets, truncations, packet-split variants, parser-enabled variants, and context-trailer variants decoded frames but did not expose the missing-slice uninitialized buffer condition. The decoder was reached, so the miss is likely in the slice/frame content rather than the harness envelope.

## Policy
For `no_crash x decoder_reached_no_target_error` on `ffmpeg-target-decoder-vp6f`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `seed_mutate_then_construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x decoder_reached_no_target_error` appears for `ffmpeg-target-decoder-vp6f`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
