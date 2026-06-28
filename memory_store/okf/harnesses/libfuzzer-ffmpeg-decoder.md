---
type: harness-contract
title: "Libfuzzer Ffmpeg Decoder harness"
description: "Round 23 input contract facts for libfuzzer-ffmpeg-decoder."
tags: ["libfuzzer-ffmpeg-decoder", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Ffmpeg Decoder Harness

## Round 23 Input Contract
- Although source triage initially showed demuxer tooling, the local verifier ran an FFmpeg AAC decoder fuzzer binary. It consumes a single raw packet/stream input, reports decoded frame counters, and does not require the demuxer filename/config suffix for the observed binary.

## Round 23 Format Links
- [[aac-decoder-packet-stream]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
