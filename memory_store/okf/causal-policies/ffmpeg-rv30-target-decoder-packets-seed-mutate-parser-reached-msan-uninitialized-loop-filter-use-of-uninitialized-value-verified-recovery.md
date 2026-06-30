---
type: causal-policy
title: "Ffmpeg RV30 Target Decoder Packets Seed Mutate Parser Reached Msan Uninitialized Loop Filter Use Of Uninitialized Value Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_msan_uninitialized_loop_filter."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_msan_uninitialized_loop_filter"
candidate_family: "seed_mutate"
input_format: "ffmpeg-rv30-target-decoder-packets"
harness_convention: "oss-fuzz-run-poc-ffmpeg-target-decoder"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-msan-uninitialized-loop-filter", "ffmpeg-rv30-target-decoder-packets", "oss-fuzz-run-poc-ffmpeg-target-decoder", "seed-mutate", "use-of-uninitialized-value", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_msan_uninitialized_loop_filter", "ffmpeg-rv30-target-decoder-packets", "oss-fuzz-run-poc-ffmpeg-target-decoder", "use-of-uninitialized-value", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Ffmpeg RV30 Target Decoder Packets Seed Mutate Parser Reached Msan Uninitialized Loop Filter Use Of Uninitialized Value Verified Recovery

## Policy
For `wrong_sink x parser_reached_msan_uninitialized_loop_filter`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Start from real RV30 decoder packets recovered from a sample container, preserve the target-decoder control footer with matching dimensions and extradata, and keep enough packet sequence context for inter-frame/reference state.
2. Mutate one key multi-slice frame by retaining only an early coherent subset of its slice table and slice bodies.
3. The later missing macroblocks leave fuzzer-allocated frame data uninitialized, and subsequent RV30 loop filtering reads that data in the vulnerable build.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The target decoder consumes raw RV30 packets, not the RealMedia container.
- A packet begins with a slice-count byte, followed by little-endian slice table entries and then the slice bitstreams.
- RV30 slice headers encode frame type, quantizer, timestamp, optional resize picture information, and starting macroblock; multi-slice packets use increasing slice starts to partition one frame.
- Harness [[oss-fuzz-run-poc-ffmpeg-target-decoder]]:
  - The run_poc wrapper invokes the generated FFmpeg RV30 target-decoder fuzzer.
  - The input is a sequence of raw decoder packets separated by the target fuzzer's fixed packet tag, followed by decoder extradata and a final control footer for context fields.
  - The footer supplies dimensions, parser selection, keyframe flags, flush behavior, and extradata; there is no archive envelope and no FuzzedDataProvider front/back layout.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ffmpeg-rv30-target-decoder-packets]] and [[oss-fuzz-run-poc-ffmpeg-target-decoder]].
