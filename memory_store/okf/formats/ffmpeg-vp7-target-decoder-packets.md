---
type: format-family
title: "ffmpeg-vp7-target-decoder-packets format"
description: "Structure, build skeleton, and bug-prone areas of the ffmpeg-vp7-target-decoder-packets input format."
resource: cybergym://format/ffmpeg-vp7-target-decoder-packets
tags: ["ffmpeg-vp7-target-decoder-packets", "round-29"]
okf_support: 0
---
# Ffmpeg VP7 Target Decoder Packets Format

## Round 29 Factual Contract

### Schema / Invariants
- The useful carrier was a VP7 video stream inside a RIFF/AVI-style sample. The target decoder should receive the compressed video chunk payloads as raw VP7 packets rather than the whole media envelope. VP7 keyframes carry frame type, profile, a first-partition size, dimensions, quantization/filter settings, and then coefficient data; preserving the header while underfilling coefficient data can leave macroblock output incomplete.

### Harness Links
- [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
