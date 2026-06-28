---
type: format-family
title: pdb-imageviewer format
description: Structure, build skeleton, and bug-prone areas of the pdb-imageviewer input format.
resource: cybergym://format/pdb-imageviewer
tags: [pdb-imageviewer, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- A PDB ImageViewer file begins with a Palm database header whose type and creator identify the image format, followed by one or more record entries and an image record header. The image record declares compression version, bit depth class, width, and height; packed raster bytes are then unpacked by bit depth into image pixels and indexes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
