---
type: format-family
title: "DWG Drawing"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["dwg-drawing", "format_contract"]
okf_support: 0
---
# DWG Drawing

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- Native DWG inputs are selected by the file-version signature and carry object records through an object map. Entity and object records contain compact bit-coded sizes and types, a handle, an extended-entity-data sequence terminated by an empty size, then common entity fields and type-specific fields, with a separate handle stream near the end of each object. EED blocks carry an application handle, raw EED bytes, and decoded subrecords such as strings, shorts, longs, reals, points, binary values, and brace markers. Increasing an EED span can make the decoder consume common entity data as EED and then continue generated decoding from an object-local overflow state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
