---
type: format-family
title: ffmpeg-raw-decoder-packet format
description: Structure, build skeleton, and bug-prone areas of the ffmpeg-raw-decoder-packet input format.
resource: cybergym://format/ffmpeg-raw-decoder-packet
tags: [ffmpeg-raw-decoder-packet, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The target decoder fuzzer feeds raw codec packets directly to a compile-time selected decoder. There is no media container. The harness may parse, send packets, receive frames, and flush according to internal parser state and a fuzz tag used by the generic decoder fuzzer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
