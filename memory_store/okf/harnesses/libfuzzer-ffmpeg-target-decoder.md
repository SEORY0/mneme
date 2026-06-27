---
type: harness-contract
title: "Libfuzzer Ffmpeg Target Decoder harness"
description: "Input contract facts for libfuzzer-ffmpeg-target-decoder."
tags: ["libfuzzer-ffmpeg-target-decoder", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Ffmpeg Target Decoder Harness

## Round 11 Input Contract
- The libFuzzer target receives raw bytes and routes them to the target decoder for the selected codec. No file container is required, and no front mode byte is used for this task; optional context configuration is taken from the tail of sufficiently large inputs.

## Format Links
- [[ffmpeg-hevc-target-decoder-frame]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 13 Facts
- The FFmpeg targeted decoder harness passes raw bytes to the H.264 decoder as one or more packets. A fixed internal separator can split multiple packets. If the input is large enough, the tail is consumed as codec-context configuration and removed from packet data before decoding.
- The FFmpeg target decoder fuzzer runs a fixed decoder on the raw input file, optionally through FFmpeg parser logic, with no outer container required and no FuzzedDataProvider fields in front of the codec bytes.
