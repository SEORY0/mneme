---
type: harness-contract
title: "Libfuzzer Ffmpeg Target Dec Fuzzer Harness"
description: "Round 26 input contract facts for libfuzzer-ffmpeg-target_dec_fuzzer."
tags: ["libfuzzer-ffmpeg-target-dec-fuzzer", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Ffmpeg Target Dec Fuzzer Harness

## Round 26 Factual Contract

### Input Contract
- FFmpeg target_dec_fuzzer treats the input prefix as decoder packet bytes for a fixed HEVC decoder. If the input is large enough, the last fixed-size context block can set parser, keyframe, flush, extradata, and codec context fields; otherwise the raw prefix is decoded directly. The harness can also split packets on its fixed separator tag, but the accepted candidate did not require a container or demuxer.

### Format Links
- [[hevc-elementary-stream]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
