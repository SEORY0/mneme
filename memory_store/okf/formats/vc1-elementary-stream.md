---
type: format-family
title: vc1-elementary-stream format
description: Format contract for vc1-elementary-stream.
resource: cybergym://format/vc1-elementary-stream
tags: [vc1-elementary-stream]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `vc1-elementary-stream` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- VC1 elementary streams are start-code-prefixed units such as sequence, entrypoint, frame, field, or
  slice payloads. The FFmpeg target also accepts a fuzzer-specific trailing control block that can
  configure dimensions, parser use, error-recognition behavior, extradata length, keyframe flags,
  packet flushing, and related decoder context fields. Packet boundaries can be introduced with the
  target's fixed tag marker.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- VC1 advanced-profile elementary streams use start-code-prefixed sequence, entrypoint, frame, field, and slice units. Slice units divide a frame into macroblock-row intervals, and their payload begins with a row-start field consumed by the decoder. For this harness, VC1 seeds that include sequence and entrypoint headers reach decoding more reliably when those prefix units are supplied as decoder extradata and the remaining frame or slice units are supplied as packet bytes.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
