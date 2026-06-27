---
type: harness-contract
title: "Libfuzzer Ffmpeg Demuxer IAMF harness"
description: "Input contract facts for libfuzzer-ffmpeg-demuxer-iamf."
tags: ["libfuzzer-ffmpeg-demuxer-iamf", "round-20"]
okf_support: 1
---
# Libfuzzer Ffmpeg Demuxer IAMF Harness

## Round 20 Input Contract
- The active target is the FFmpeg IAMF demuxer fuzzer. It consumes the raw file bytes as a single IAMF bitstream; there is no external container, filename requirement, or fuzzer-side field carving.

## Round 20 Format Links
- [[iamf]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
