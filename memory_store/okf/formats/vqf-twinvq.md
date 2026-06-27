---
type: format-family
title: "vqf/twinvq format"
description: "Descriptive format contract facts for vqf/twinvq."
tags: ["vqf-twinvq", "round-18"]
okf_support: 1
train_only: true
---
# Vqf Twinvq Format

## Round 18 Factual Contract

### Schema / Invariants
- A VQF stream starts with the TwinVQ magic and version string, followed by a big-endian header-size field. Header chunks are four-byte tags plus big-endian lengths. A COMM chunk supplies channel count, bitrate, and rate flag; the demuxer requires a supported rate/bitrate combination before finalizing stream parameters. Non-special chunk tags are treated as metadata strings with the declared chunk length.

### Harness Links
- [[libfuzzer-ffmpeg-demuxer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
