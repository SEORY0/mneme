---
type: format-family
title: "Jbig2 format"
description: "Structure and invariants for the jbig2 input format."
tags: ["jbig2", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- JBIG2 input is a segment stream. Segment records carry a segment type, page association, declared data length, region information for bitmap segments, and optional generic or halftone region data. Generic-region segments can select MMR coding, and MMR-decoded bitmap data maintains separate byte and bit consumption accounting.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
