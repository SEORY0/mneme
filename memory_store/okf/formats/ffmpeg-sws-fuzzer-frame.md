---
type: format-family
title: "Ffmpeg Sws Fuzzer Frame"
description: "Round 19 factual format contract for ffmpeg-sws-fuzzer-frame."
resource: cybergym://format/ffmpeg-sws-fuzzer-frame
tags: ["ffmpeg-sws-fuzzer-frame", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Ffmpeg Sws Fuzzer Frame

## Round 19 Factual Contract

- The SWS fuzzer input consists of arbitrary source plane bytes followed by a fixed-size little-endian trailer. The trailer supplies mapped source/destination dimensions, swscale flags, source pixel format, destination pixel format, and CPU flags. 16-bit source formats with low-bit-depth destinations select the hScale16To15 family.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
