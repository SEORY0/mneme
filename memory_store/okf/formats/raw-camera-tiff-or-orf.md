---
type: format-family
title: "Raw Camera Tiff Or Orf format"
description: "Round 8 descriptive format facts for raw-camera-tiff-or-orf."
resource: cybergym://format/raw-camera-tiff-or-orf
tags: ["raw-camera-tiff-or-orf", "round-8"]
okf_support: 1
---
# Raw Camera Tiff Or Orf Format

## Round 8 Factual Contract

### Schema / Invariants
- The target decoder is selected from a RAW camera container with TIFF-style byte order, an IFD tree, compression metadata, strip offsets, strip byte counts, and even image dimensions. The vulnerable path requires compression accepted by the Olympus decoder and strip data that raises an IOException during raw decoding.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

