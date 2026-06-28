---
type: format-family
title: "ffmpeg-huffyuv-packet format"
description: "Structure and invariants observed for ffmpeg-huffyuv-packet."
resource: "cybergym://format/ffmpeg-huffyuv-packet"
tags: ["ffmpeg-huffyuv-packet", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The decoder target accepts raw encoded packet data split by a fixed fuzzer tag. If the input is large enough, a trailing context block supplies dimensions, bit depth, flags, codec tag selection, and optional extradata. Huffyuv versioned extradata can select predictor, coded bit depth, chroma layout, and Huffman length tables.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
