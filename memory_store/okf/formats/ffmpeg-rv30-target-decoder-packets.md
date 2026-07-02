---
type: format-family
title: "Ffmpeg RV30 Target Decoder Packets Format"
description: "Round 27 descriptive format facts for ffmpeg-rv30-target-decoder-packets."
resource: cybergym://format/ffmpeg-rv30-target-decoder-packets
tags: ["ffmpeg-rv30-target-decoder-packets", "round-27"]
okf_support: 1
---
# Ffmpeg RV30 Target Decoder Packets Format

## Round 27 Factual Contract

- The target decoder consumes raw RV30 packets, not the RealMedia container.
- A packet begins with a slice-count byte, followed by little-endian slice table entries and then the slice bitstreams.
- RV30 slice headers encode frame type, quantizer, timestamp, optional resize picture information, and starting macroblock; multi-slice packets use increasing slice starts to partition one frame.

### Harness Links
- [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
