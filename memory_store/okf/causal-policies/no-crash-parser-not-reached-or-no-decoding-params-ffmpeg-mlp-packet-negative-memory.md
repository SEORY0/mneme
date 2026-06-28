---
type: causal-policy
title: "No Crash Parser Not Reached Or No Decoding Params Ffmpeg Mlp Packet Negative Memory"
description: "Round 24 negative memory for no_crash with verifier signal parser_not_reached_or_no_decoding_params."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_no_decoding_params"
candidate_family: "construct"
input_format: "ffmpeg-mlp-packet"
harness_convention: "libfuzzer"
vuln_class: "index-out-of-bounds"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-no-decoding-params", "ffmpeg-mlp-packet", "libfuzzer", "construct", "negative-memory", "round-24"]
match_keys: ["no-crash", "parser-not-reached-or-no-decoding-params", "ffmpeg-mlp-packet", "libfuzzer", "index-out-of-bounds"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 24
---
# No Crash Parser Not Reached Or No Decoding Params Ffmpeg Mlp Packet Negative Memory

- key: `no_crash x parser_not_reached_or_no_decoding_params`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[ffmpeg-mlp-packet]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
A hand-built MLP-like packet with sync material did not reach the decoding-parameter path that leaves an invalid primitive-matrix count in decoder state. The hard gates are MLP parser framing, major/restart header checks, parity/checksum validation, and a decoding-parameters section with matrix parameters that survive until output rematrixing.

## Policy
For `no_crash x parser_not_reached_or_no_decoding_params` on `ffmpeg-mlp-packet`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Prefer `construct` only while this format and harness contract are present.

## Procedure
1. When `no_crash x parser_not_reached_or_no_decoding_params` appears for `ffmpeg-mlp-packet`, treat this candidate family as a basin-to-avoid rather than evidence of proximity.
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
