---
type: format-family
title: "ffmpeg-target-decoder-packets-vp9 format"
description: "Descriptive format contract facts for ffmpeg-target-decoder-packets-vp9."
tags: ["ffmpeg-target-decoder-packets-vp9", "round-18"]
okf_support: 1
train_only: true
---
# Ffmpeg Target Decoder Packets VP9 Format

## Round 18 Factual Contract

### Schema / Invariants
- The target decoder fuzzer does not demux container files. Its front input is a sequence of raw codec packets separated by a fixed tag. For VP9, packet payloads need to be decoder-ready VP9 frame data, not a WebM container. A large trailing configuration block can set dimensions, parser use, strictness, error-recognition flags, keyframe flags, flush pattern, and optional extradata.

### Harness Links
- [[libfuzzer-ffmpeg-target-decoder]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
