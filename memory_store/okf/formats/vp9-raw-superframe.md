---
type: format-family
title: vp9-raw-superframe format
description: "Round 23 descriptive structure and invariant facts for vp9-raw-superframe."
resource: cybergym://format/vp9-raw-superframe
tags: ["vp9-raw-superframe", "round-23"]
okf_support: 1
train_only: true
---
# Vp9 Raw Superframe Format

## Round 23 Factual Contract

### Schema / Invariants
- The active target is the VP9 metadata bitstream filter, not the VP9 decoder fuzzer. Its input is packet data optionally split by a fixed delimiter; a VP9 raw superframe is indicated by a trailer marker that encodes frame count and per-frame size length, followed by frame size entries and a repeated marker.

### Harness Links
- [[libfuzzer-ffmpeg-vp9-metadata-bsf]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
