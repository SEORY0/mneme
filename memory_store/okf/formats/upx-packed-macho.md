---
type: format-family
title: upx-packed-macho format
description: "Round 23 descriptive structure and invariant facts for upx-packed-macho."
resource: cybergym://format/upx-packed-macho
tags: ["upx-packed-macho", "round-23"]
okf_support: 1
train_only: true
---
# Upx Packed Macho Format

## Round 23 Factual Contract

### Schema / Invariants
- UPX Mach-O decompression expects both a valid Mach-O envelope and UPX packing metadata such as loader and packed-data structures. Plain Mach-O stubs can pass initial format recognition but are rejected before unpacking if they lack UPX markers and packed block layout.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
