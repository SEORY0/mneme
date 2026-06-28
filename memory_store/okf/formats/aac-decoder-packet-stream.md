---
type: format-family
title: aac-decoder-packet-stream format
description: "Round 23 descriptive structure and invariant facts for aac-decoder-packet-stream."
resource: cybergym://format/aac-decoder-packet-stream
tags: ["aac-decoder-packet-stream", "round-23"]
okf_support: 1
train_only: true
---
# Aac Decoder Packet Stream Format

## Round 23 Factual Contract

### Schema / Invariants
- AAC decoder inputs can be raw ADTS frames or packet-like buffers. Useful high-efficiency AAC samples may carry SBR/PS signaling, while the target description points specifically at audio get_buffer memory not being zero-initialized before later AAC/USAC/SBR reads.

### Harness Links
- [[libfuzzer-ffmpeg-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
