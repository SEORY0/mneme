---
type: format-family
title: "dwg-dxf format"
description: "Structure and reachability facts for dwg/dxf."
resource: cybergym://format/dwg-dxf
tags: ["dwg-dxf"]
okf_support: 1
---
# Dwg DXF Format

## Round 9 Factual Contract

### Schema / Invariants
- DXF is line-oriented group-code/value text with sections ending in EOF; DWG is binary and
  versioned.
- The libredwg corpus includes both valid CAD drawings and known-error examples, but valid samples
  tend to complete normally.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
