---
type: causal-policy
title: "Ffmpeg AIC Target Decoder Packet Construct AIC Decode Slice Reaches Msan Uninitialized Idct Read Use Of Uninitialized Value Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal aic_decode_slice_reaches_msan_uninitialized_idct_read."
failure_class: "wrong_sink"
verifier_signal: "aic_decode_slice_reaches_msan_uninitialized_idct_read"
candidate_family: "construct"
input_format: "ffmpeg-aic-target-decoder-packet"
harness_convention: "oss-fuzz-run-poc-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "aic-decode-slice-reaches-msan-uninitialized-idct-read", "ffmpeg-aic-target-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "construct", "use-of-uninitialized-value", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "aic_decode_slice_reaches_msan_uninitialized_idct_read", "ffmpeg-aic-target-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "use-of-uninitialized-value", "wrong-sink", "aic-decode-slice-reaches-msan-uninitialized-idct-read", "ffmpeg-aic-target-decoder-packet", "oss-fuzz-run-poc-ffmpeg-target-decoder", "use-of-uninitialized-value", "verified_recovery", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Ffmpeg AIC Target Decoder Packet Construct AIC Decode Slice Reaches Msan Uninitialized Idct Read Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x aic_decode_slice_reaches_msan_uninitialized_idct_read`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[ffmpeg-aic-target-decoder-packet]]
- related harness facts: [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

## Policy
For `wrong_sink x aic_decode_slice_reaches_msan_uninitialized_idct_read` on `ffmpeg-aic-target-decoder-packet`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Construct a tiny raw AIC decoder packet with context dimensions supplied through the target-decoder configuration trailer. Keep the AIC header, slice table, and slice-size units self-consistent, then encode the coefficient bands so each band is skipped rather than explicitly written. In the vulnerable build the decoder later recombines and IDCTs slice coefficients that were allocated but not cleared; the fixed build zeroes that buffer.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[ffmpeg-aic-target-decoder-packet]]: The AIC packet is an elementary decoder frame, not a MOV container. It has a small fixed header with dimensions matching the codec context, a per-slice size table, and slice bitstreams containing band coefficient coding. Valid skip-coded bands can leave coefficient storage unwritten while still producing a decodable frame path.
- Harness [[oss-fuzz-run-poc-ffmpeg-target-decoder]]: The OSS-Fuzz run_poc wrapper invokes the compiled FFmpeg AIC target-decoder fuzzer. The input is raw decoder packet data; for larger inputs the final fixed-size configuration block can set codec-context fields such as dimensions and parser flags. There is no demuxer container requirement, front selector byte, or FuzzedDataProvider split.

## Negative Memory
- Do not corrupt the outer `ffmpeg-aic-target-decoder-packet` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[ffmpeg-aic-target-decoder-packet]] and [[oss-fuzz-run-poc-ffmpeg-target-decoder]].
