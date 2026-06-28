---
type: format-family
title: ffmpeg-av1-obu-stream format
description: Structure, build skeleton, and bug-prone areas of the ffmpeg-av1-obu-stream input format.
resource: cybergym://format/ffmpeg-av1-obu-stream
tags: ["ffmpeg-av1-obu-stream", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- Low-overhead AV1 OBU streams begin with OBU headers carrying type, extension, has-size, and reserved bits. The demuxer probe expects a temporal delimiter with empty payload before later positive-size OBUs. OBU payload lengths are LEB128-style variable integers.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
