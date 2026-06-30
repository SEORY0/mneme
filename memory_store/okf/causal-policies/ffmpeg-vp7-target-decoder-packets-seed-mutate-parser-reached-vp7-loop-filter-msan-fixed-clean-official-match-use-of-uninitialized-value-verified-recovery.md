---
type: causal-policy
title: "Ffmpeg VP7 Target Decoder Packets Seed Mutate Parser Reached VP7 Loop Filter Msan Fixed Clean Official Match Use Of Uninitialized Value Verified Recovery"
description: "Round 29 verified recovery for wrong_sink with verifier signal parser_reached_vp7_loop_filter_msan_fixed_clean_official_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vp7_loop_filter_msan_fixed_clean_official_match"
candidate_family: "seed_mutate"
input_format: "ffmpeg-vp7-target-decoder-packets"
harness_convention: "oss-fuzz-run_poc-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-vp7-loop-filter-msan-fixed-clean-official-match", "ffmpeg-vp7-target-decoder-packets", "oss-fuzz-run-poc-ffmpeg-target-decoder", "seed-mutate", "use-of-uninitialized-value", "verified-recovery", "round-29"]
match_keys: ["wrong_sink", "parser_reached_vp7_loop_filter_msan_fixed_clean_official_match", "ffmpeg-vp7-target-decoder-packets", "oss-fuzz-run_poc-ffmpeg-target-decoder", "use-of-uninitialized-value", "wrong-sink", "parser-reached-vp7-loop-filter-msan-fixed-clean-official-match", "ffmpeg-vp7-target-decoder-packets", "oss-fuzz-run-poc-ffmpeg-target-decoder", "use-of-uninitialized-value", "verified_recovery", "seed_mutate", "seed-mutate"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 29
---
# Ffmpeg VP7 Target Decoder Packets Seed Mutate Parser Reached VP7 Loop Filter Msan Fixed Clean Official Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_vp7_loop_filter_msan_fixed_clean_official_match`
- outcome: verified target match / recovery policy
- success_count: 1
- related format facts: [[ffmpeg-vp7-target-decoder-packets]]
- related harness facts: [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

## Policy
For `wrong_sink x parser_reached_vp7_loop_filter_msan_fixed_clean_official_match` on `ffmpeg-vp7-target-decoder-packets`, keep the parser and harness gates that produced the verifier signal, then vary only the causal relation described below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from a real VP7 sample, extract the raw video decoder packets from the media carrier, and feed them through the target-decoder packet separator. Preserve the first packet's VP7 header and dimensions but truncate its reconstruction payload so the decoder accepts the frame while leaving part of the fuzzer-allocated frame buffer unreconstructed. Follow it with later valid interframe packets; VP7 prediction and loop filtering then consume the partially initialized reference frame in the vulnerable build, while the fixed build's zeroed allocation exits cleanly.
2. Preserve format recognition and the harness input contract while mutating the narrow sink invariant; do not broaden into an off-target crash or a both-image crash.
3. If later verifier output changes the failure key, re-rank against that new key before mutating unrelated fields.

## Format Contract
- Format [[ffmpeg-vp7-target-decoder-packets]]: The useful carrier was a VP7 video stream inside a RIFF/AVI-style sample. The target decoder should receive the compressed video chunk payloads as raw VP7 packets rather than the whole media envelope. VP7 keyframes carry frame type, profile, a first-partition size, dimensions, quantization/filter settings, and then coefficient data; preserving the header while underfilling coefficient data can leave macroblock output incomplete.
- Harness [[oss-fuzz-run-poc-ffmpeg-target-decoder]]: The generated run_poc wrapper invokes the FFmpeg VP7 target-decoder fuzzer on the PoC file. The fuzzer treats bytes as decoder packets, optionally split by its fixed packet separator, and for larger inputs reads a fixed-size control area for codec context, parser, keyframe, flush, and extradata settings. There is no FuzzedDataProvider front/back layout and no demuxer stage in the wrapper.

## Negative Memory
- Do not corrupt the outer `ffmpeg-vp7-target-decoder-packets` recognition gate while retargeting this signal.
- Do not count parser reachability, clean exits, fixed-image crashes, both-image crashes, or local wrong-sink labels as success without official target match.
- Never store payload bytes, exact positions, checksums, submit metadata, or task-local identifiers.

## Evidence Shape
- Support: one round-29 worker trace with official target match.
- Scope: generator repair and retargeting only; pair with [[ffmpeg-vp7-target-decoder-packets]] and [[oss-fuzz-run-poc-ffmpeg-target-decoder]].
