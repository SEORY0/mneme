---
type: format-family
title: webp format
description: Structure, build skeleton, and bug-prone areas of the webp input format.
resource: cybergym://format/webp
tags: ["webp", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-raw-ffmpeg-webp-decoder)

### Schema / Invariants
- WebP inputs are RIFF containers containing VP8, VP8L, animation, and related chunks. The target is in FFmpeg's WebP decoder path, so the envelope must be valid enough for chunk dispatch and frame decode before malformed reference metadata can matter.

### Harness Links
- [[libfuzzer-raw-ffmpeg-webp-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
