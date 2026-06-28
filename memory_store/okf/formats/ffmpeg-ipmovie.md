---
type: format-family
title: "ffmpeg-ipmovie format"
description: "Structure and invariants observed for ffmpeg-ipmovie."
resource: "cybergym://format/ffmpeg-ipmovie"
tags: ["ffmpeg-ipmovie", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The IPMovie demuxer searches for an identifying ASCII signature near the start of the stream before processing chunk records. A truncated stream can reach the signature comparison before a complete header has been read.

### Harness Links
- [[oss-fuzz-libfuzzer-demuxer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
