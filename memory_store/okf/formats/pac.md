---
type: format-family
title: pac format
description: Structure, build skeleton, and bug-prone areas of the pac input format.
resource: cybergym://format/pac
tags: [pac, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- PAC data starts with little-endian buffer count and version fields followed by fixed-size buffer descriptors. Each descriptor carries a type, a size, and an aligned payload position. The parser has both minimum and maximum overall size gates, so the useful trigger is in the arithmetic relationship between the count-derived descriptor area and the available input, not in making a huge file.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
