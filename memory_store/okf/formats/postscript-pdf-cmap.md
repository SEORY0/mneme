---
type: format-family
title: "Postscript PDF Cmap format"
description: "Structure and invariants for the postscript-pdf-cmap input format."
tags: ["postscript-pdf-cmap", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- CMap resources define CIDSystemInfo, CMapName, CMapType, codespace ranges, and mapping sections such as bfchar, bfrange, cidchar, and cidrange. PDF files can also carry CMap syntax inside ToUnicode streams attached to composite fonts.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
