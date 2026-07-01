---
type: format-family
title: "H264 Annex B Format"
description: "Round 26 descriptive structure and invariant facts for h264-annex-b."
tags: ["h264-annex-b", "round-26"]
okf_support: 2
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

## Round 33 Factual Contract

### Schema / Invariants
- The input is a raw Annex-B elementary H.264 stream made of start-code-delimited NAL units. Parser reachability depended on coherent SPS and PPS records before an IDR slice; the PPS must select CAVLC entropy coding, and the slice residual syntax is interpreted only after macroblock prediction, coded-block-pattern, and quantizer-delta fields are consistent enough for residual decode.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
