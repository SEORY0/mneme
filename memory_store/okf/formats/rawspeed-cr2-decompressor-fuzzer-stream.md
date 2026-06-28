---
type: format-family
title: Rawspeed Cr2 Decompressor Fuzzer Stream format
description: Format contract for rawspeed-cr2-decompressor-fuzzer-stream.
resource: cybergym://format/rawspeed-cr2-decompressor-fuzzer-stream
tags: [rawspeed-cr2-decompressor-fuzzer-stream]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The direct fuzzer input begins with little-endian raw-image fields: width, height, raw image type, components per pixel, and CFA flag. It then reads a little-endian slice count and signed slice widths, followed by a lossless JPEG stream with SOI, DHT, SOF3, SOS, and entropy-coded scan data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
