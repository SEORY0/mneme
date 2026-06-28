---
type: format-family
title: "ffmpeg-notchlc-packet format"
description: "Descriptive format contract facts for ffmpeg-notchlc-packet."
tags: ["ffmpeg-notchlc-packet", "round-18"]
okf_support: 1
train_only: true
---
# Ffmpeg Notchlc Packet Format

## Round 18 Factual Contract

### Schema / Invariants
- The NotchLC decoder accepts raw packets beginning with a codec tag, uncompressed size, compressed size, and format selector. Uncompressed block data then describes texture dimensions, control-data positions, data ranges, luma row data, optional alpha controls, and UV sub-blocks. The risky reads are in sub-block decoding where branch selectors determine how many following bytes are consumed.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
