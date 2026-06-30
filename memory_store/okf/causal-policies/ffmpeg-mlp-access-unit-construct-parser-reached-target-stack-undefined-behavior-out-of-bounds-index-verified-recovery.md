---
type: causal-policy
title: "Ffmpeg MLP Access Unit Construct Parser Reached Target Stack Undefined Behavior Out Of Bounds Index Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_target_stack."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack"
candidate_family: "construct"
input_format: "ffmpeg-mlp-access-unit"
harness_convention: "libfuzzer-ffmpeg-target-dec-fuzzer"
vuln_class: "undefined-behavior-out-of-bounds-index"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack", "ffmpeg-mlp-access-unit", "libfuzzer-ffmpeg-target-dec-fuzzer", "construct", "undefined-behavior-out-of-bounds-index", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_target_stack", "ffmpeg-mlp-access-unit", "libfuzzer-ffmpeg-target-dec-fuzzer", "undefined-behavior-out-of-bounds-index", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# Ffmpeg MLP Access Unit Construct Parser Reached Target Stack Undefined Behavior Out Of Bounds Index Verified Recovery

## Policy
For `wrong_sink x parser_reached_target_stack`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a decoder-ready MLP access unit rather than a container file.
2. Satisfy the access-unit length, major-sync, restart-header, substream, parity, and checksum gates.
3. Decode one valid subblock first so output has accumulated samples, then issue a second decoding-parameter update that sets a primitive matrix output channel outside the restart header's matrix-channel range.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- MLP decoder input is an access-unit packet with an access-unit header, optional major-sync header, substream header, restart header, decoding parameters, and residual sample bits.
- Restart headers establish channel bounds and defaults; decoding-parameter blocks can update primitive matrix metadata independently from sample data.
- Valid framing requires internally consistent lengths, parity, and MLP checksum fields.
- Harness [[libfuzzer-ffmpeg-target-dec-fuzzer]]:
  - The FFmpeg target decoder fuzzer feeds raw decoder packet bytes to the MLP decoder, not a demuxed media container.
  - It scans for a fixed separator between packets; a separator-sized trailing region is needed when a single packet should be delivered in full.
  - Inputs over the context-field threshold reserve the trailing context block for AVCodecContext fields.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[ffmpeg-mlp-access-unit]] and [[libfuzzer-ffmpeg-target-dec-fuzzer]].
