---
type: format-family
title: rawspeed-ljpeg-decompressor-envelope format
description: Structure and reachability facts for rawspeed-ljpeg-decompressor-envelope inputs.
tags: [rawspeed-ljpeg-decompressor-envelope]
okf_support: 0
---
# Rawspeed Ljpeg Decompressor Envelope Format

## Round 10 Factual Contract

### Schema / Invariants
- The direct decompressor envelope begins with little-endian scalar RawImage metadata, followed by tile offsets/flags and then a lossless JPEG byte stream. The JPEG stream must satisfy SOI, DHT, SOF3, and SOS gates before decoded samples are written into the RawImage buffer.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
