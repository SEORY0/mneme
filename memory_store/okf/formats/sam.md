---
type: format-family
title: "Sam format"
description: "Descriptive contract facts for sam."
resource: "cybergym://format/sam"
tags: ["sam", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- SAM text needs header records and tab-delimited alignment records to be accepted as sequence data.
- Unmapped records can carry a missing reference name while still containing sequence, quality, CIGAR-like, and coordinate fields.
- CRAM writing may auto-enable embedded references when no external reference is available.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
