---
type: format-family
title: "gdal-isce-xml format"
description: "Structure and invariants observed for gdal-isce-xml."
resource: "cybergym://format/gdal-isce-xml"
tags: ["gdal-isce-xml", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- GDAL ISCE datasets use an XML sidecar describing raster dimensions, data type, interleaving, byte order, and a companion raster data file. Many fields are nested property/value records rather than flat attributes.

### Harness Links
- [[libfuzzer-gdal-isce-fuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
