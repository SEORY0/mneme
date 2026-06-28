---
type: format-family
title: ffmpeg-apac-decoder-packet format
description: Structure, build skeleton, and bug-prone areas of the ffmpeg-apac-decoder-packet input format.
resource: cybergym://format/ffmpeg-apac-decoder-packet
tags: [ffmpeg-apac-decoder-packet, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The APAC decoder consumes elementary packet bytes rather than the APAC demuxer container in this harness. The decoder has per-channel state for bit length, block length, prior sample, and prior delta. A leading bit-control code can adjust bit length or block length before coded deltas are read from a most-significant-bit bitstream.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
