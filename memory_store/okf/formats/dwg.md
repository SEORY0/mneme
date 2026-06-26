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
