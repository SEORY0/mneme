---
type: format-family
title: "h264 annex-b stream format"
description: "Descriptive format contract facts for h264 annex-b stream."
tags: ["h264-annex-b-stream", "round-18"]
okf_support: 1
train_only: true
---
# H264 Annex B Stream Format

## Round 18 Factual Contract

### Schema / Invariants
- The useful input is a raw Annex-B H.264 byte stream with start-code-delimited parameter sets and slice NAL units. Parameter sets must remain coherent enough for the decoder to allocate frames before missing or under-specified slices can matter.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
