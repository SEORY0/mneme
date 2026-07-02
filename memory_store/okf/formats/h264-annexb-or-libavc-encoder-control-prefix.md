---
type: format-family
title: "H264 Annexb Or Libavc Encoder Control Prefix Format"
description: "Structure, build skeleton, and bug-prone areas of the h264-annexb-or-libavc-encoder-control-prefix input format."
resource: "cybergym://format/h264-annexb-or-libavc-encoder-control-prefix"
tags: ["h264-annexb-or-libavc-encoder-control-prefix", "round-37"]
okf_support: 1
train_only: true
---
# H264 Annexb Or Libavc Encoder Control Prefix Format
## Round 37 Factual Contract

### Schema / Invariants
- The source tree contains both a libavc encoder fuzzer format and an H.264 decoder corpus.
- The encoder fuzzer format is a fixed front-loaded control region containing dimensions, color format, architecture, rate-control and other knobs, followed by raw frame bytes.
- The actual local image wrapper accepts a raw H.264 Annex-B elementary stream made of start-code-delimited NAL units; practical parser reachability needs coherent SPS/PPS before slice data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
