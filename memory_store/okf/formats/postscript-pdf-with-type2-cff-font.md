---
type: format-family
title: "Postscript PDF With Type2 Cff Font format"
description: "Descriptive contract facts for Postscript PDF With Type2 Cff Font."
resource: "cybergym://format/postscript-pdf-with-type2-cff-font"
tags: ["postscript-pdf-with-type2-cff-font", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The target path requires Type 2 CFF charstrings and the flex/hflex operator family, where operand-stack depth is the critical invariant. Ordinary PDF text using built-in fonts does not necessarily instantiate a Type2 CFF interpreter frame.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
