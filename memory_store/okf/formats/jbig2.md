---
type: format-family
title: "Jbig2 format"
description: "Structure and invariants for the jbig2 input format."
tags: ["jbig2", "round-20"]
okf_support: 2
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

## Round 33 Factual Contract

### Schema / Invariants
- JBIG2 files have a file signature, file flags, and optional page count, then sequential segment records. Segment records carry a segment number, type flags, referred-segment metadata, page association, declared data length, and segment body. Page information establishes the page before page-associated regions. Pattern dictionary bodies include MMR/template flags, pattern cell dimensions, a maximum gray value, and coded collective-bitmap data. Halftone region bodies include region placement, halftone flags, grid dimensions, grid origin and vectors, followed by coded gray-scale bitplane data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
