---
type: causal-policy
title: "Wrong Sink Local Target Stack Reached But Official Fixed Crashed Ffmpeg Target Encoder Frame Negative Memory"
description: "Round 15 negative memory for wrong_sink with verifier signal local_target_stack_reached_but_official_fixed_crashed."
failure_class: "wrong_sink"
verifier_signal: "local_target_stack_reached_but_official_fixed_crashed"
candidate_family: "construct"
input_format: "ffmpeg-target-encoder-frame"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["wrong-sink", "local-target-stack-reached-but-official-fixed-crashed", "ffmpeg-target-encoder-frame", "negative-memory", "round-15"]
match_keys: ["wrong_sink", "local_target_stack_reached_but_official_fixed_crashed", "ffmpeg-target-encoder-frame", "libfuzzer", "use-of-uninitialized-value", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 15
---
# Wrong Sink Local Target Stack Reached But Official Fixed Crashed Ffmpeg Target Encoder Frame Negative Memory

- key: `wrong_sink x local_target_stack_reached_but_official_fixed_crashed`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ffmpeg-target-encoder-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- A raw frame plus encoder-configuration suffix reached the CFHD encoder and produced a local
  MemorySanitizer report from the DWT temporary buffer allocation path, but official submission
  reported both vulnerable and fixed images exiting non-zero. The remaining issue is separating the
  intended uninitialized-buffer read from behavior that still fails under the fixed image.

## Policy
Treat `wrong_sink x local_target_stack_reached_but_official_fixed_crashed` on `ffmpeg-target-encoder-frame` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- The FFmpeg encoder fuzzer treats the leading bytes as frame-plane data. When the input is large
  enough, a fixed-size trailing configuration block supplies width, height, timing, compliance flags,
  and a pixel-format selector before encoder initialization.

## Harness Contract
- The harness is a libFuzzer target for the selected FFmpeg encoder. It opens a codec context from the
  trailer configuration, allocates an AVFrame, copies front-region bytes into available frame buffers
  with zero-fill for the rest, and repeatedly sends the frame to the encoder.

## Negative Memory
- Do not resubmit variants that only reproduce `local_target_stack_reached_but_official_fixed_crashed`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from Round 15.
- Scope: generator repair and basin avoidance only.
