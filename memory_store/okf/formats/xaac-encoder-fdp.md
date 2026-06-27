---
type: format-family
title: "Xaac Encoder Fdp format"
description: "Round 8 descriptive format facts for xaac-encoder-fdp."
resource: cybergym://format/xaac-encoder-fdp
tags: ["xaac-encoder-fdp", "round-8"]
okf_support: 1
---
# Xaac Encoder Fdp Format

## Round 8 Factual Contract

### Schema / Invariants
- The target is not a conventional AAC bitstream parser; it is an encoder configuration plus synthetic PCM/input data stream. Relevant fields include bitrate, channel count, sample rate, frame length, audio object type, SBR/eSBR/USAC and DRC-related switches, followed by remaining bytes used as encoder input.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.


## Round 13 Facts
- The logical input is not an AAC file. Front-loaded FuzzedDataProvider fields choose encoder parameters such as sample rate, channel mode, bit-rate, audio object type, SBR/USAC/DRC flags, and then supply synthetic PCM frame bytes or fill values.
