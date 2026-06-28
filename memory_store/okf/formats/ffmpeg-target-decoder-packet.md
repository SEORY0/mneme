---
type: format-family
title: ffmpeg-target-decoder-packet format
description: Structure, build skeleton, and bug-prone areas of the ffmpeg-target-decoder-packet input format.
resource: cybergym://format/ffmpeg-target-decoder-packet
tags: [ffmpeg-target-decoder-packet, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The active fuzzer consumes a raw decoder packet with an optional context/options tail when the input is long enough. The tail initializes dimensions, parser-enable flags, extradata size, codec tag, keyframe pattern, flush pattern, skip mode, and related AVCodecContext fields. Packet bytes before the tail are then sent through parser and decoder loops.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
