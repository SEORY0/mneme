---
type: format-family
title: "Uk NTF In GDAL Fuzzer Friendly Archive Format"
description: "Round 26 descriptive structure and invariant facts for uk-ntf-in-gdal-fuzzer-friendly-archive."
tags: ["uk-ntf-in-gdal-fuzzer-friendly-archive", "round-26"]
okf_support: 1
train_only: true
---
# Uk NTF In GDAL Fuzzer Friendly Archive Format

## Round 26 Factual Contract

### Schema / Invariants
- UK NTF is line-oriented: records begin with a two-digit record type and end with a continuation/final marker plus a percent terminator. A volume header precedes database metadata and a section header; the section header supplies coordinate widths, coordinate scale factors, origins, tile dimensions, and Z-coordinate width. After the section header, feature groups are anchored by feature records such as points or lines and can include geometry or 3D geometry records; a volume-termination record ends the scan.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
