---
type: format-family
title: "Mat"
description: "Round 7 factual format contract for mat."
resource: cybergym://format/mat
tags: ["mat", "format-contract", "round-7"]
okf_support: 2
train_only: true
---
# Mat

## Round 7 Factual Contract

### Schema / Invariants
- MAT level-5 files use a fixed descriptive header followed by typed array records. Each array record
has a typed tag, byte count, array flags, dimensions, name, and typed data payload; readers cross-
check declared object sizes against dimensions and element size before scanline import.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- GraphicsMagick MAT handling accepts MATLAB Level-5 streams with a descriptive header, endian marker, matrix records, array flags, dimensions, a name tag, a typed raster-data tag, and column-oriented raster payload. The reader also supports older Level-4 matrices with a compact numeric header, name bytes, and column-oriented raster data. For Level-5 uncompressed objects, the object-size check includes metadata overhead, so small payload shortages can pass the top-level size relation even when later scanline reads are incomplete.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
