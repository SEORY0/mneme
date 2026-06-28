---
type: format-family
title: "tar format"
description: "Structure and invariants observed for tar."
resource: "cybergym://format/tar"
tags: ["tar", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The harness input is a tar archive with a command text member and an input dataset member. Command text is line-oriented, one argument per line. The input dataset can be a normal GDAL-supported raster such as GeoTIFF or VRT.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
