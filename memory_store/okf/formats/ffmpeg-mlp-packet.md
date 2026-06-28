---
type: format-family
title: "ffmpeg-mlp-packet format"
description: "Structure and invariants observed for ffmpeg-mlp-packet."
resource: "cybergym://format/ffmpeg-mlp-packet"
tags: ["ffmpeg-mlp-packet", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- MLP/TrueHD decoding expects access units with sync/header structure, substream headers, restart information, parity/checksum fields, and optional decoding-parameter blocks containing matrix parameters. Matrix counts are bit-packed and only meaningful after earlier stream headers initialize channel/substream state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
