---
type: format-family
title: "ehdr-tar format"
description: "Structure and invariants for the ehdr-tar input format."
tags: ["ehdr-tar", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The specialized EHdr fuzzer expects a tar archive containing a raw data file and matching sidecar header. The header needs NROWS, NCOLS, NBANDS, NBITS, byte order, and layout fields; NBITS below one byte selects the custom bit-unpacking path.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
