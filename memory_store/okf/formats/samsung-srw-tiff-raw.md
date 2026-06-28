---
type: format-family
title: samsung-srw-tiff-raw format
description: Structure, build skeleton, and bug-prone areas of the samsung-srw-tiff-raw input format.
resource: cybergym://format/samsung-srw-tiff-raw
tags: ["samsung-srw-tiff-raw", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (afl-libfuzzer-wrapper)

### Schema / Invariants
- SRW is TIFF-like: endian marker, TIFF magic, an IFD with make/model and image geometry tags, and raw strip or tile data referenced by offsets and byte counts. Samsung V2 decoding depends on camera metadata and compressed image payload layout, not just make/model tags.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
