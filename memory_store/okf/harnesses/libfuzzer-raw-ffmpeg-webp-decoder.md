---
type: harness-contract
title: "Libfuzzer Raw Ffmpeg Webp Decoder harness"
description: "Input contract facts for Libfuzzer Raw Ffmpeg Webp Decoder."
tags: ["libfuzzer-raw-ffmpeg-webp-decoder", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Ffmpeg Webp Decoder Harness

## Round 21 Input Contract (webp)

- The fuzzer passes raw bytes as a packet to FFmpeg's WebP decoder under MemorySanitizer. There is no FuzzedDataProvider layout or external file wrapper; parser reachability depends entirely on the RIFF/WebP chunk structure.

## Round 21 Format Links (webp)
- [[webp]]

## Round 21 Notes (webp)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
