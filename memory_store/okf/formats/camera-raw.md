---
type: format-family
title: camera-raw format
description: Structure and reachability facts for camera-raw inputs.
tags: [camera-raw]
okf_support: 0
---
# Camera Raw Format

## Round 10 Factual Contract

### Schema / Invariants
- LibRaw accepts complete camera RAW files such as TIFF-derived NEF/CR2 and RAF containers. The harness requires metadata and image payloads that pass open-buffer and unpack before postprocessing is attempted.

### Harness Links
- [[afl-libfuzzer-compatible-raw-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
