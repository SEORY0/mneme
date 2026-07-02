---
type: format-family
title: "Bfd Archive format"
description: "Round 34 factual contract for bfd-archive."
tags: ["bfd-archive", "round-34"]
okf_support: 1
train_only: true
---
# Bfd Archive format

## Round 34 Factual Contract

### Schema / Invariants
- BFD archive inputs are raw archive files. SysV ar archives have a global archive marker followed by fixed-format member headers and member bodies. BSD/COFF/ECOFF archive maps are represented as special first members; ECOFF map names encode header and object endianness, and their bodies contain a symbol count, map entries, and a string area. XCOFF archives use old or big archive headers with decimal file-position fields before member records.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
