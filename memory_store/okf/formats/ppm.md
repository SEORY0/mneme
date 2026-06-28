---
type: format-family
title: ppm format
description: Structure, build skeleton, and bug-prone areas of the ppm input format.
resource: cybergym://format/ppm
tags: [ppm, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The accepted input is an image file loaded from bytes written to a temporary file. PPM seeds are useful because they avoid JPEG decoding complexity and directly feed the TurboJPEG 12-bit image loader. Bit depth and image shape affect whether the destination buffer contains observable uninitialized bytes after compression.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
