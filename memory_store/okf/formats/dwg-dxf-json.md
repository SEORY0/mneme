---
type: format-family
title: "DWG DXF JSON Format"
description: "Round 26 descriptive structure and invariant facts for dwg-dxf-json."
tags: ["dwg-dxf-json", "round-26"]
okf_support: 1
train_only: true
---
# DWG DXF JSON Format

## Round 26 Factual Contract

### Schema / Invariants
- DWG inputs are binary drawings with a release marker at the beginning. DXF inputs are text group-code/value streams organized into sections such as HEADER and OBJECTS. JSON import starts from an object-shaped text stream. The fuzz target selects the parser family from the input prefix rather than from a file extension.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
