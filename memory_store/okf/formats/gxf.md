---
type: format-family
title: "Gxf format"
description: "Descriptive contract facts for gxf."
resource: "cybergym://format/gxf"
tags: ["gxf", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- GXF is an ASCII grid format with section tags for point count, row count, optional transform parameters, compression digit width, and a grid section. In compressed grids, the digit-width value controls how many characters are consumed per encoded numeric token while scanlines are expanded.

### Harness Links
- [[libfuzzer-filesystem-gdal-raster-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
