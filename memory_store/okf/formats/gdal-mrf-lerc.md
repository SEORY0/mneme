---
type: format-family
title: gdal-mrf-lerc format
description: Structure, build skeleton, and bug-prone areas of the gdal-mrf-lerc input format.
resource: cybergym://format/gdal-mrf-lerc
tags: ["gdal-mrf-lerc", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- MRF LERC datasets use XML metadata plus index and data tile storage. The LERC decompressor reads tile bytes into a padded buffer and chooses LERC1 or LERC2 by header inspection before bit-stuffer decoding.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
