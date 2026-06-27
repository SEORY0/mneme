---
type: format-family
title: "PDF Xref Stream format"
description: "Descriptive contract facts for pdf-xref-stream."
resource: "cybergym://format/pdf-xref-stream"
tags: ["pdf-xref-stream", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- PDF xref streams are indirect stream objects with Type XRef, Size, W field-width array, optional Index, and trailer keys such as Root and Prev. The startxref marker points to the active xref stream; a Prev key chains to an older xref section or stream.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
