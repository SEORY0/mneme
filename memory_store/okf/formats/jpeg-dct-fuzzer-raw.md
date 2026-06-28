---
type: format-family
title: jpeg-dct-fuzzer-raw format
description: Structure, build skeleton, and bug-prone areas of the jpeg-dct-fuzzer-raw input format.
resource: cybergym://format/jpeg-dct-fuzzer-raw
tags: [jpeg-dct-fuzzer-raw, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- Normal JPEG files are not the best abstraction for the executed binary; the wrapper uses a raw DCT fuzzer corpus contract. The source tree also contains standard JPEG and BMP test images, but replaying those as the single input file did not reach the described decompression-smoothing sink.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
