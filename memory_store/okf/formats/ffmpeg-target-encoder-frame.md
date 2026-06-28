---
type: format-family
title: ffmpeg-target-encoder-frame format
description: Format contract for ffmpeg-target-encoder-frame.
resource: cybergym://format/ffmpeg-target-encoder-frame
tags: [ffmpeg-target-encoder-frame]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ffmpeg-target-encoder-frame` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The FFmpeg encoder fuzzer treats the leading bytes as frame-plane data. When the input is large
  enough, a fixed-size trailing configuration block supplies width, height, timing, compliance flags,
  and a pixel-format selector before encoder initialization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
