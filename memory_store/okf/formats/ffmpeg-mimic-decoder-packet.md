---
type: format-family
title: "ffmpeg-mimic-decoder-packet format"
description: "Structure and invariants observed for ffmpeg-mimic-decoder-packet."
resource: "cybergym://format/ffmpeg-mimic-decoder-packet"
tags: ["ffmpeg-mimic-decoder-packet", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- Mimic packets for this decoder start with decoder-local numeric frame fields such as quality, dimensions, prediction mode, and coefficient count, followed by a compressed coefficient bitstream. The body is byte-swapped in word-sized chunks before MSB-first bit parsing. VLC symbols encode both run-position movement and how many residual bits are consumed for the next lookup.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
