---
type: format-family
title: "Ffmpeg Vp7 Decoder Packet Stream format"
description: "Descriptive contract facts for ffmpeg-vp7-decoder-packet-stream."
resource: "cybergym://format/ffmpeg-vp7-decoder-packet-stream"
tags: ["ffmpeg-vp7-decoder-packet-stream", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The FFmpeg target decoder fuzzer consumes raw packet data and can split multiple packets using its built-in packet separator and optional context trailer.
- In this generated target the active decoder is VP7; clean candidates reached decoding and produced pixels without crashing.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
