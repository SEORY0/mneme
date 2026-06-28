---
type: format-family
title: ffmpeg-ivr-realmedia-demuxer format
description: Structure, build skeleton, and bug-prone areas of the ffmpeg-ivr-realmedia-demuxer input format.
resource: cybergym://format/ffmpeg-ivr-realmedia-demuxer
tags: ["ffmpeg-ivr-realmedia-demuxer", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer-ffmpeg-demuxer)

### Schema / Invariants
- IVR data begins with a REC/R1M-style header, metadata entries such as stream count, per-stream OpaqueData parsed by RealMedia codec-data logic, then opcodes carrying stream index, timestamp, advertised packet size, and packet payload. The vulnerable relation is an advertised packet or subpacket length larger than available bytes.

### Harness Links
- [[libfuzzer-ffmpeg-demuxer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
