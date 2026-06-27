---
type: format-family
title: "postscript-or-xps-for-ghostscript-xpswrite format"
description: "Structure and reachability facts for postscript-or-xps-for-ghostscript-xpswrite."
resource: cybergym://format/postscript-or-xps-for-ghostscript-xpswrite
tags: ["postscript-or-xps-for-ghostscript-xpswrite"]
okf_support: 1
---
# Postscript Or XPS For Ghostscript Xpswrite Format

## Round 9 Factual Contract

### Schema / Invariants
- The relevant bitmap relation is width bytes versus padded raster bytes across multiple scanlines:
  a non-byte-aligned or otherwise padded small bitmap can have an allocation computed from unpadded
  final-line width while the copier uses full raster lines.
- Ghostscript can reach bitmap output through XPS/PDF/PostScript rendering depending on the device
  wrapper.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
