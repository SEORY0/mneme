---
type: harness-contract
title: "libfuzzer-ffmpeg-demuxer harness"
description: "Descriptive harness contract facts for libfuzzer-ffmpeg-demuxer."
tags: ["libfuzzer-ffmpeg-demuxer", "round-18"]
okf_support: 1
train_only: true
---
# Libfuzzer Ffmpeg Demuxer Harness

## Round 18 Input Contract

### Schema / Invariants
- The FFmpeg demuxer fuzzer feeds raw bytes through an AVIO buffer and lets probing select the demuxer from the stream signature when no filename tail is used. There is no FuzzedDataProvider split for this compact input; the whole file is the demuxer byte stream.

### Format Links
- [[vqf-twinvq]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
