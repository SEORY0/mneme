---
type: format-family
title: "Rawspeed Cr2 Decompressor Envelope format"
description: "Round 8 descriptive format facts for rawspeed-cr2-decompressor-envelope."
resource: cybergym://format/rawspeed-cr2-decompressor-envelope
tags: ["rawspeed-cr2-decompressor-envelope", "round-8"]
okf_support: 1
---
# Rawspeed Cr2 Decompressor Envelope Format

## Round 8 Factual Contract

### Schema / Invariants
- The fuzzer-specific RawSpeed envelope starts with little-endian raw image metadata, followed by little-endian slicing fields, then an LJpeg-compressed payload consumed by the decompressor. For the single-slice case, the last-slice width is the meaningful width for the only slice.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- The fuzzer-specific RawSpeed carrier begins with a RawImage construction envelope, then a slice count and signed slice-width table, followed by compressed LJpeg-style image data consumed by Cr2Decompressor. The slice widths must both pass image-size sanity checks and remain inconsistent enough to expose the c-p-p relation.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- This fuzzer does not consume a camera CR2 file. It expects a little-endian synthetic envelope containing raw-image width, height, image type, component count, CFA flag, slice count, regular slice width, last-slice width, then a lossless-JPEG-like compressed stream.

### Harness Links
- [[libfuzzer-rawspeed-cr2-decompressor]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
