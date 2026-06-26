---
type: format-family
title: "Postscript Pfb Font Stream format"
description: "Descriptive contract facts for Postscript Pfb Font Stream."
resource: "cybergym://format/postscript-pfb-font-stream"
tags: ["postscript-pfb-font-stream", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- PFB font data is a segmented Type 1 font representation with marker records, length-delimited ASCII or binary sections, and an end marker. Ghostscript can also reach PFB parsing through PostScript filters or font-loading operators rather than only by raw PFB bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
