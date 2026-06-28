---
type: format-family
title: "Jpeg Card But Qpdf Runtime format"
description: "Descriptive contract facts for Jpeg Card But Qpdf Runtime."
resource: "cybergym://format/jpeg-card-but-qpdf-runtime"
tags: ["jpeg-card-but-qpdf-runtime", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The described bug requires a progressive JPEG with a valid scan sequence that leaves chroma progressive-state entries uninitialized before smoothing a later row. The observed runtime instead consumed qpdf/PDF-style inputs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
