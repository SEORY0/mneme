---
type: format-family
title: ffmpeg-demuxer-fuzzer-carved-stream format
description: Structure, build skeleton, and bug-prone areas of the ffmpeg-demuxer-fuzzer-carved-stream input format.
resource: cybergym://format/ffmpeg-demuxer-fuzzer-carved-stream
tags: [ffmpeg-demuxer-fuzzer-carved-stream, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The effective stream payload is the leading portion of the file. The APETAGEX parser expects a tag marker and length/version fields near tag metadata, but demuxer selection and seeking behavior determine whether that metadata is inspected.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
