---
type: format-family
title: "tiff-or-orf-raw-camera-file format"
description: "Structure and invariants observed for tiff-or-orf-raw-camera-file."
resource: "cybergym://format/tiff-or-orf-raw-camera-file"
tags: ["tiff-or-orf-raw-camera-file", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- ORF is TIFF-derived. The decoder expects an IFD carrying image width, image length, compression, strip offsets, and strip byte counts; the compressed path is taken when a single strip is present and the referenced strip region is valid in the file buffer.

### Harness Links
- [[libfuzzer-raw-bytes]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
