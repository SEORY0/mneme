---
type: format-family
title: "Cr2 Tiff Raw"
description: "Round 7 factual format contract for cr2-tiff-raw."
resource: cybergym://format/cr2-tiff-raw
tags: ["cr2-tiff-raw", "format-contract", "round-7"]
okf_support: 2
train_only: true
---
# Cr2 Tiff Raw

## Round 7 Factual Contract

### Schema / Invariants
- CR2 is TIFF-based: parser reachability depends on a TIFF header, IFD entries for raw data
offsets/strips, Canon-specific tags, and data at the referenced raw offset. The vulnerable path
reads old-format dimensions from a raw-data offset and then continues after a decompressor
IOException, allowing later metadata processing to operate on a partially initialized raw image.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- CR2 is TIFF-based: parser reachability depends on a TIFF header, IFD entries, Canon-specific raw tags such as slice metadata, and data at referenced strip or raw offsets. Direct decompressor envelopes are a different fuzzer family.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
