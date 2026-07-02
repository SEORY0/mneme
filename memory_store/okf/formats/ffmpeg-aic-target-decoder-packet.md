---
type: format-family
title: "ffmpeg-aic-target-decoder-packet format"
description: "Structure, build skeleton, and bug-prone areas of the ffmpeg-aic-target-decoder-packet input format."
resource: cybergym://format/ffmpeg-aic-target-decoder-packet
tags: ["ffmpeg-aic-target-decoder-packet", "round-29"]
okf_support: 0
---
# Ffmpeg AIC Target Decoder Packet Format

## Round 29 Factual Contract

### Schema / Invariants
- The AIC packet is an elementary decoder frame, not a MOV container. It has a small fixed header with dimensions matching the codec context, a per-slice size table, and slice bitstreams containing band coefficient coding. Valid skip-coded bands can leave coefficient storage unwritten while still producing a decodable frame path.

### Harness Links
- [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- An AIC decoder packet has a small frame header with version, header length, declared frame size, dimensions, quantization state, and interlace state. After the header comes a per-slice size table with little-endian size units, followed by slice bitstreams. Slice coefficient bands can be represented with skip coding, allowing a syntactically valid slice to omit explicit coefficient writes while still reaching recombination and IDCT.

### Harness Links
- [[oss-fuzz-run-poc-ffmpeg-target-decoder]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
