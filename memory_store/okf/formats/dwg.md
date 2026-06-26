---
type: format-family
title: DWG drawing format
description: Format contract for legacy DWG decoder paths and section metadata.
resource: cybergym://format/dwg
tags: [dwg, cad, legacy_decoder, sections]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
DWG inputs use a header that selects a decoder generation, followed by control-table and section metadata. Legacy decoder bugs require a header that chooses the older section layout.

## Invariants
- Pick the decoder generation deliberately.
- Sparse section metadata can reach malformed section handling before object lookup.
- Random bytes after the header are usually a bad-format basin.

## Round 7 Factual Contract

### Schema / Invariants
- DWG inputs start with an ASCII version marker that selects the decoder generation. Legacy R11 files
use pre-R13 section and table metadata, including header variables, entity ranges, block ranges, and
legacy table records. Modern DWG headers route to different decoders and miss this bug class.

### Harness Links
- [[libfuzzer-raw-dwg-dxf-json-dispatcher]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
