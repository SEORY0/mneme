---
type: format-family
title: "Mpeg Video Elementary Or Program Stream"
description: "Round 7 factual format contract for mpeg-video-elementary-or-program-stream."
resource: cybergym://format/mpeg-video-elementary-or-program-stream
tags: ["mpeg-video-elementary-or-program-stream", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Mpeg Video Elementary Or Program Stream

## Round 7 Factual Contract

### Schema / Invariants
- GPAC's MPEG video reframer recognizes MPEG-1/2 and MPEG-4 Visual start-code streams. The decoder-
config cleanup path scans collected header bytes for start-code prefixes and checks user-data-like
payloads for packed-bitstream markers.

### Harness Links
- [[libfuzzer-gpac-probe-analyze]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
