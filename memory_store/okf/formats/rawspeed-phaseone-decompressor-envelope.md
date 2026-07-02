---
type: format-family
title: "rawspeed-phaseone-decompressor-envelope format"
description: "Descriptive format contract facts for rawspeed-phaseone-decompressor-envelope."
tags: ["rawspeed-phaseone-decompressor-envelope", "round-18"]
okf_support: 1
train_only: true
---
# Rawspeed Phaseone Decompressor Envelope Format

## Round 18 Factual Contract

### Schema / Invariants
- The fuzzer input is a RawSpeed decompressor envelope, not a camera raw file. It describes image dimensions, pixel type, component count, CFA flag, then a strip list where each strip has a row selector, a length, and strip payload bytes. PhaseOne construction requires a single 16-bit component image with even positive width and sane dimensions before strips are prepared.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 26 Factual Contract


### Schema / Invariants
- The PhaseOne decompressor fuzzer consumes a little-endian envelope containing image width, height, image type, components-per-pixel, CFA flag, then a strip count and repeated strip records. Each strip record contains a row selector, a payload length, and that many compressed strip bytes. The decompressor requires a positive even width, bounded dimensions, 16-bit single-component pixels, and a strip vector length equal to image height.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The fuzzer input is a little-endian RawSpeed decompressor envelope, not a camera raw file. It contains image width, height, image type, component count, a CFA flag, then a strip count followed by strip records. Each strip record carries a row selector, a payload length, and that many compressed strip bytes. PhaseOne construction requires positive bounded dimensions, an even width, a 16-bit single-component image, and a strip-vector length equal to image height.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
