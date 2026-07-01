---
type: causal-policy
title: "Ffmpeg AAC Decoder Packet Stream Construct No Crash Clean Exit Undefined Behavior Invalid Pointer Intermediate Negative Memory"
description: "Negative memory for ffmpeg-aac-decoder-packet-stream candidates that ended in no_crash with verifier signal clean_exit."
failure_class: "no_crash"
verifier_signal: "clean_exit"
candidate_family: "construct"
input_format: "ffmpeg-aac-decoder-packet-stream"
harness_convention: "libfuzzer"
vuln_class: "undefined-behavior-invalid-pointer-intermediate"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "clean-exit", "ffmpeg-aac-decoder-packet-stream", "libfuzzer", "construct", "undefined-behavior-invalid-pointer-intermediate", "negative-memory", "round-32"]
match_keys: ["no-crash", "clean-exit", "ffmpeg-aac-decoder-packet-stream", "libfuzzer", "construct", "undefined-behavior-invalid-pointer-intermediate", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 32
---
# Ffmpeg AAC Decoder Packet Stream Construct No Crash Clean Exit Undefined Behavior Invalid Pointer Intermediate Negative Memory

- key: `no_crash x clean_exit`
- outcome: persistent diagnosed failure
- success_count: 0
- related format facts: [[ffmpeg-aac-decoder-packet-stream]]
- related harness facts: [[libfuzzer]]

## Policy
Treat `no_crash x clean_exit` for `[[ffmpeg-aac-decoder-packet-stream]]` under `[[libfuzzer]]` as a dead-end basin until new evidence changes the verifier signal. Preserve only parser-recognition facts, then change the missing relation named by the diagnosis.

## Procedure
1. Keep any envelope property that reached the parser or clean execution, but stop repeating the same carrier shape.
2. Avoid the observed dead end: Constructed AAC carriers opened the FFmpeg AAC fuzzer but exited cleanly. ADTS-like frames, raw AAC element packets, tag-split packet streams, a structured single-channel element followed by fill/SBR-extension bytes, LOAS-like framing, and a large context-tail input did not synthesize the SBR plus Parametric Stereo state needed for ff_ps_apply. The missing relation is a coherent AAC/SBR frame sequence that both initializes SBR/PS and drives the invalid top-band pointer arithmetic during PS application.
3. Rebuild around `[[ffmpeg-aac-decoder-packet-stream]]` and `[[libfuzzer]]`, targeting the missing gate or state relation rather than padding, broad corruption, or unrelated seed churn.
4. Submit only after local verification produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Format Contract
- The fuzzer input is not a full media container. It is a packet stream for FFmpeg's target decoder fuzzer. Packet boundaries are marked by a fixed internal tag when present; bytes before each tag become one AVPacket. If the total input is large enough, the last block of bytes is consumed as decoder-context fields before packet decoding and is not part of the packet payload. AAC data still must be coherent enough for channel configuration, raw data block parsing, SBR extension parsing, and PS application.

## Harness Contract
- The libFuzzer target initializes the FFmpeg AAC decoder once, allocates an AVCodecContext, optionally derives context fields from the tail of large inputs, opens the decoder, then repeatedly feeds AVPackets split by the fixed tag. Without the tag, the entire remaining front region is one packet. There is no FuzzedDataProvider; integers are not consumed from the back except for the harness-specific large-input context tail.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one diagnosed Round 32 failed solve attempt.
- Attempts observed: 13.
