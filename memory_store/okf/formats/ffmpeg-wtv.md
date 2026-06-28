---
type: format-family
title: Ffmpeg Wtv format
description: Format contract for ffmpeg-wtv.
resource: cybergym://format/ffmpeg-wtv
tags: [ffmpeg-wtv]
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
- WTV files are parsed through FFmpeg's WTV demuxer. The descriptor path is reached from WTV event entries associated with streams; descriptor bytes are copied into a local buffer and then parsed as MPEG-2 descriptors with tag and length fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
