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

## Round 19 Factual Contract

- DWG begins with an AutoCAD version marker that selects the binary decoder generation. R13/R2000-era files contain section metadata, class records, object tables, handles, and bit-packed object streams; class count and type ranges must remain coherent enough to reach object dispatch.
- Harness link: [[libfuzzer-raw-dwg-dxf-json-dispatcher]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 29 Factual Contract

### Schema / Invariants
- The harness accepts DWG, JSON, or DXF based on the first bytes: DWG begins with the standard ASCII release marker, JSON begins with an object marker, and other inputs are treated as DXF. DXF header codepage parsing updates the DWG header, but the JSON writer's conversion uses the bit-chain codepage copied from the input chain. Native DWG decoding carries the legacy codepage into that chain, so DWG is the reliable family for this sink. Legacy TV strings are byte strings interpreted through the drawing codepage, then quoted as UTF-8 for JSON output.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- R13/R2000 DWG inputs start with an AutoCAD version marker and contain section locator records for header variables, classes, and handles/object map. The classes section stores bit-coded class records with number, proxy flags, application name, C++ name, DXF name, zombie flag, and an entity/object class marker. The object map then points to bit-coded object streams whose type may reference a dynamic class by subtracting the dynamic-class base.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
