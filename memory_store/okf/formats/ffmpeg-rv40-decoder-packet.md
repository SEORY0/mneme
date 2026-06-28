---
type: format-family
title: "ffmpeg-rv40-decoder-packet format"
description: "Descriptive format contract facts for ffmpeg-rv40-decoder-packet."
tags: ["ffmpeg-rv40-decoder-packet", "round-18"]
okf_support: 1
train_only: true
---
# Ffmpeg RV40 Decoder Packet Format

## Round 18 Factual Contract

### Schema / Invariants
- The input is raw target-decoder packet data for FFmpeg's RV40 decoder, not a tar or media container. The packet must contain enough codec-appropriate header and slice structure to enter RV34/RV40 frame decoding and error-resilience completion.

### Harness Links
- [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
