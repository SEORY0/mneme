---
type: negative-memory
title: "Ac3 Eac3 Audio Frame Construct No Crash Decoder Clean Exit Or Target Audio Block Not Reached Out Of Bounds Read Negative Memory"
description: "Round 33 negative memory for no_crash with verifier signal decoder_clean_exit_or_target_audio_block_not_reached."
failure_class: "no_crash"
verifier_signal: "decoder_clean_exit_or_target_audio_block_not_reached"
candidate_family: "construct"
input_format: "ac3-eac3-audio-frame"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["no-crash", "decoder-clean-exit-or-target-audio-block-not-reached", "ac3-eac3-audio-frame", "libfuzzer", "construct", "out-of-bounds-read", "negative-memory", "round-33"]
match_keys: ["no_crash", "decoder_clean_exit_or_target_audio_block_not_reached", "ac3-eac3-audio-frame", "libfuzzer", "construct", "out-of-bounds-read", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 33
---
# Ac3 Eac3 Audio Frame Construct No Crash Decoder Clean Exit Or Target Audio Block Not Reached Out Of Bounds Read Negative Memory

- key: `no_crash x decoder_clean_exit_or_target_audio_block_not_reached`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[ac3-eac3-audio-frame]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Constructed AC3 and E-AC3 frames satisfied the outer decoder packet contract but did not trigger the band-structure out-of-array condition. The attempts covered plain audio blocks, coupling-enabled blocks, spectral-extension blocks, changed band ranges with requested band-structure reuse, and tag-split multi-packet decoding; the decoder exited cleanly each time.

## Policy
Treat `no_crash x decoder_clean_exit_or_target_audio_block_not_reached` on `ac3-eac3-audio-frame` as a basin to avoid unless a new candidate changes the parser gate, state relation, sink relation, or official differential behavior described below. Do not repeat variants that only preserve the same clean-exit, off-target, post-patch-crash, both-image-crash, or target-handoff-missing signal.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one causal relation at a time and discard candidates that return to `decoder_clean_exit_or_target_audio_block_not_reached`.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed vulnerable-only target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `decoder_clean_exit_or_target_audio_block_not_reached`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, timeouts, or fixed-image crashes as success.
- Never store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[ac3-eac3-audio-frame]]. The fuzzer input is raw compressed AC3 or E-AC3 decoder packet data, not a media container. AC3/E-AC3 frames begin with a sync header, declare sample-rate and frame-size information, then carry bitstream metadata followed by one or more audio blocks. Coupling and spectral extension each have a band range plus either coded band structure bits or reuse/default semantics, followed by exponent, allocation, coordinate, and transform-coefficient data.

## Harness Contract
Use [[libfuzzer]]. The FFmpeg target decoder harness feeds raw bytes to the selected AC3 decoder. If the input is large enough, a trailing context block is consumed as codec-context fields and removed from packet data. Otherwise the packet is passed directly. A fixed delimiter can split the remaining bytes into multiple packets for repeated decode calls under one decoder context.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 33 after 7 attempts.
- Scope: generator repair and basin avoidance only.
