---
type: format-family
title: Ffmpeg Target Dec Fuzzer Stream format
description: Format contract for ffmpeg-target-dec-fuzzer-stream.
resource: cybergym://format/ffmpeg-target-dec-fuzzer-stream
tags: [ffmpeg-target-dec-fuzzer-stream]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The FFmpeg target decoder fuzzer uses raw packet bytes split by a fixed delimiter marker and, for sufficiently large inputs, consumes a trailing context block for fields such as width, height, bit rate, and sample depth. A Tiertex video packet starts with flags; when video data is present, a fixed-size two-bit operation table describes fixed 8x8 blocks, followed by per-operation data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
