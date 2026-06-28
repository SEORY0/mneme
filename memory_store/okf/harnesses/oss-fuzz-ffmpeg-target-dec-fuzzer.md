---
type: harness-contract
title: "Oss Fuzz Ffmpeg Target Dec Fuzzer harness"
description: "Input contract facts for oss-fuzz-ffmpeg-target-dec-fuzzer."
tags: ["oss-fuzz-ffmpeg-target-dec-fuzzer", "round-20"]
okf_support: 2
---
# Oss Fuzz Ffmpeg Target Dec Fuzzer Harness

## Round 20 Input Contract
- The target_dec fuzzer selects a compile-time decoder, optionally parses packet chunks, opens an AVCodecContext, and repeatedly feeds AVPacket data through the decoder with bounded iterations.
- The FFmpeg target_dec fuzzer uses raw packet bytes for a compile-time selected decoder, initializes the codec context once, and decodes packets through the audio/video handler under libFuzzer/OSS-Fuzz bounds.

## Round 20 Format Links
- [[ffmpeg-target-dec-packet-bytes]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
