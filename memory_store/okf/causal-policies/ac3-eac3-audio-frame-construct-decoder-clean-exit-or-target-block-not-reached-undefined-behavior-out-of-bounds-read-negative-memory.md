---
type: negative-memory
title: "AC3 EAC3 Audio Frame Construct Decoder Clean Exit Or Target Block Not Reached Undefined Behavior Out Of Bounds Read Negative Memory"
description: "Round 29 negative memory for no_crash with verifier signal decoder_clean_exit_or_target_block_not_reached."
failure_class: "no_crash"
verifier_signal: "decoder_clean_exit_or_target_block_not_reached"
candidate_family: "construct"
input_format: "ac3-eac3-audio-frame"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "undefined-behavior-out-of-bounds-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "decoder-clean-exit-or-target-block-not-reached", "ac3-eac3-audio-frame", "libfuzzer-ffmpeg-target-decoder", "construct", "undefined-behavior-out-of-bounds-read", "negative-memory", "round-29"]
match_keys: ["no_crash", "decoder_clean_exit_or_target_block_not_reached", "ac3-eac3-audio-frame", "libfuzzer-ffmpeg-target-decoder", "undefined-behavior-out-of-bounds-read", "no-crash", "decoder-clean-exit-or-target-block-not-reached", "ac3-eac3-audio-frame", "libfuzzer-ffmpeg-target-decoder", "undefined-behavior-out-of-bounds-read", "negative_memory", "construct", "construct"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 29
---
# AC3 EAC3 Audio Frame Construct Decoder Clean Exit Or Target Block Not Reached Undefined Behavior Out Of Bounds Read Negative Memory

- key: `no_crash x decoder_clean_exit_or_target_block_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ac3-eac3-audio-frame]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
Constructed raw AC3 and E-AC3 frames satisfied the intended dual-mono plus low-frequency-channel relation and the FFmpeg packet-stream contract, but the decoder exited cleanly. The likely missing gate was complete, internally consistent audio-block syntax deep enough to reach the dynamic-range scaling loop; no usable in-tree AC3 seed was found to mutate.

## Policy
Treat `no_crash x decoder_clean_exit_or_target_block_not_reached` on `ac3-eac3-audio-frame` for `undefined-behavior-out-of-bounds-read` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `decoder_clean_exit_or_target_block_not_reached` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_clean_exit_or_target_block_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
AC3/E-AC3 decoder inputs are raw compressed audio frames, not media containers. The frame header carries sync information, sample-rate and frame-size selectors, bitstream mode/version fields, channel mode, optional dual-mono dynamic-range fields, and a low-frequency-channel flag. Audio blocks then carry block-switching, dither, coupling, exponent, bit-allocation, SNR, delta-bit-allocation, skip, and mantissa data; malformed block syntax can be rejected before sample scaling.

## Harness Contract
The FFmpeg target decoder fuzzer feeds the selected decoder with raw packet bytes. The input may contain an optional fixed delimiter that splits multiple packets, but no demux container is parsed. Very large inputs may also provide trailing codec-context fields; ordinary small inputs are treated as direct packet data.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 29 after 6 attempts.
- Scope: generator repair and basin avoidance only.
