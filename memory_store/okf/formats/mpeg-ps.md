---
type: format-family
title: "Mpeg Ps Format"
description: "Input contract facts for mpeg-ps."
tags: ["mpeg-ps", "round-30"]
okf_support: 0
train_only: true
---
# Mpeg Ps Format

## Round 30 Factual Contract

### Schema / Invariants
- MPEG-PS packets are found by start-code prefixes, followed by a packet length and PES header fields. A video stream id routes to the video stream creation path. For MPEG-2-style PES headers, the header byte, flags byte, and header-data-length field reduce the remaining packet length before payload sniffing.

### Harness Links
- [[libfuzzer-ffmpeg-demuxer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
