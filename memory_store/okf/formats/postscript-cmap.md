---
type: format-family
title: "Postscript Cmap format"
description: "Descriptive contract facts for Postscript Cmap."
resource: "cybergym://format/postscript-cmap"
tags: ["postscript-cmap", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- Ghostscript CMap data is PostScript resource syntax with dictionaries, code-space ranges, and mapping operators such as character, range, and CID mappings. Valid begin/end operator pairing is needed before mapping arrays are interpreted.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
