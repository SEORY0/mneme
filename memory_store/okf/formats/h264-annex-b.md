---
type: format-family
title: "H264 Annex B Format"
description: "Round 26 descriptive structure and invariant facts for h264-annex-b."
tags: ["h264-annex-b", "round-26"]
okf_support: 1
train_only: true
---
# H264 Annex B Format

## Round 26 Factual Contract

### Schema / Invariants
- The input is a raw H.264 Annex-B byte stream, not a media container. The parser expects start-code-delimited NAL units; SPS and PPS must select CAVLC rather than CABAC, define a small frame, and make the slice header fields consistent with frame number and picture-order widths. Residual syntax follows macroblock prediction, coded-block-pattern, and quantizer-delta fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
