---
type: format-family
title: "Rawspeed Dng Tiff Raw Container format"
description: "Structure and invariants for the rawspeed-dng-tiff-raw-container input format."
tags: ["rawspeed-dng-tiff-raw-container", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- RawSpeed LJpeg payloads may need valid JPEG-style compressed frame structure, but when the fuzzer target is a DNG decoder that payload must be embedded behind TIFF/DNG tags and raw strip/tile metadata. Bare decompressor envelopes are format-mismatched for DNG entry points.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
