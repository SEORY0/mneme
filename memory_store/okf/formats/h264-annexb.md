---
type: format-family
title: "H264 Annexb"
description: "Round 7 factual format contract for h264-annexb."
resource: cybergym://format/h264-annexb
tags: ["h264-annexb", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# H264 Annexb

## Round 7 Factual Contract

### Schema / Invariants
- H.264 decoder seeds are byte streams with NAL units and start-code style framing. The encoder fuzzer
source, although not built here, would instead consume a fixed configuration prefix followed by raw
YUV frame bytes.

### Harness Links
- [[libfuzzer-wrapper-mismatch]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
