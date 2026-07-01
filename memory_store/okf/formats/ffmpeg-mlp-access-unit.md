---
type: format-family
title: "Ffmpeg MLP Access Unit Format"
description: "Round 27 descriptive format facts for ffmpeg-mlp-access-unit."
resource: cybergym://format/ffmpeg-mlp-access-unit
tags: ["ffmpeg-mlp-access-unit", "round-27"]
okf_support: 2
---
# Ffmpeg MLP Access Unit Format

## Round 27 Factual Contract

- MLP decoder input is an access-unit packet with an access-unit header, optional major-sync header, substream header, restart header, decoding parameters, and residual sample bits.
- Restart headers establish channel bounds and defaults; decoding-parameter blocks can update primitive matrix metadata independently from sample data.
- Valid framing requires internally consistent lengths, parity, and MLP checksum fields.

### Harness Links
- [[libfuzzer-ffmpeg-target-dec-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- MLP decoder input is a raw access-unit packet with a length-bearing access-unit header, optional major-sync header, substream header, restart header, decoding-parameter blocks, residual sample bits, and optional parity/check bytes. Restart headers establish channel bounds and default decoding parameters; later decoding-parameter blocks can update matrix metadata independently. Valid reachability depends on consistent access-unit length, major-sync checksum, restart framing, substream length, and packet parity.

### Harness Links
- [[libfuzzer-ffmpeg-target-dec-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
