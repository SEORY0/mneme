---
type: format-family
title: "Ffmpeg Target Decoder Packet Stream format"
description: "Structure and invariants for the ffmpeg-target-decoder-packet-stream input format."
tags: ["ffmpeg-target-decoder-packet-stream", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- FFmpeg target decoder fuzz inputs are raw packet streams for a compiled decoder target rather than complete media containers. Some targets accept packet splits or trailing codec context data, but the bytes must still resemble packets for the chosen codec family to reach slice/frame reconstruction.

### Harness Links
- [[oss-fuzz-run-poc]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
