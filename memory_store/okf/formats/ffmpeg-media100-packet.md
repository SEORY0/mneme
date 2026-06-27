---
type: format-family
title: ffmpeg-media100-packet format
description: Structure and reachability facts for ffmpeg-media100-packet inputs.
tags: [ffmpeg-media100-packet]
okf_support: 0
---
# Ffmpeg Media100 Packet Format

## Round 10 Factual Contract

### Schema / Invariants
- The active FFmpeg input is a Media100-coded packet stream with codec parameters supplied by the fuzzer wrapper. Packets that are short but marker-shaped can pass through media100-to-MJPEGB conversion and then into MJPEG-style decode logic.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
