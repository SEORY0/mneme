---
type: format-family
title: rawspeed-ljpeg-fuzzer-struct format
description: Structure, build skeleton, and bug-prone areas of the rawspeed-ljpeg-fuzzer-struct input format.
resource: cybergym://format/rawspeed-ljpeg-fuzzer-struct
tags: [rawspeed-ljpeg-fuzzer-struct, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The active input is a binary fuzzer struct, not a camera file. It starts with little-endian image width, height, raw image type, components-per-pixel, and CFA flag. The harness then reads little-endian X offset, Y offset, and a DNG-bug flag before treating the remaining bytes as an LJpeg stream.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 28 Factual Contract

### Schema / Invariants
- The fuzzer input begins with little-endian RawImage metadata: dimensions, image type, components per pixel, CFA flag, followed by little-endian tile X/Y offsets and a compatibility flag. The remaining bytes are parsed by the LJpeg decompressor after it switches the stream to big-endian. The LJpeg stream must start with SOI and include coherent DHT, SOF3, and SOS marker segments; SOF component descriptors and SOS table selectors must agree so decodeN selects the intended component count.

### Harness Links
- [[afl-libfuzzer-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
