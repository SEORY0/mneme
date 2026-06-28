---
type: harness-contract
title: "Oss Fuzz Libfuzzer Demuxer harness"
description: "Input contract facts for oss-fuzz-libfuzzer-demuxer."
tags: ["oss-fuzz-libfuzzer-demuxer", "round-24"]
okf_support: 1
---
# Oss Fuzz Libfuzzer Demuxer Harness

## Round 24 Factual Contract

### Input Contract
- Raw bytes are supplied through the OSS-Fuzz FFmpeg demuxer harness with the IPMovie demuxer forced by environment/configuration. The harness opens the bytes as an AVIO-backed input and calls the demuxer header path directly.

### Format Links
- [[ffmpeg-ipmovie]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
