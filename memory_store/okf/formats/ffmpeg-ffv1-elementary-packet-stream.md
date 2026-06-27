---
type: format-family
title: "Ffmpeg Ffv1 Elementary Packet Stream format"
description: "Structure and invariants for the ffmpeg-ffv1-elementary-packet-stream input format."
tags: ["ffmpeg-ffv1-elementary-packet-stream", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- FFV1 packets carry range-coded or Golomb-coded frame data with version-dependent headers, quantization tables, slice count/grid metadata, and per-slice payloads. The vulnerability is about missing slices retaining unpredictable content in allocated frame buffers, so a valid frame with declared multi-slice structure and absent/truncated slice data is needed.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
