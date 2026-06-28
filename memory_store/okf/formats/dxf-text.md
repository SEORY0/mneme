---
type: format-family
title: "dxf-text format"
description: "Structure and reachability facts for DXF text."
resource: cybergym://format/dxf-text
tags: ["dxf-text"]
okf_support: 2
---
# DXF Text Format

## Round 9 Factual Contract

### Schema / Invariants
- DXF is a line-oriented group-code/value format.
- A minimal document can declare SECTION/ENDSEC groups, set the version in the HEADER section,
  provide basic TABLES scaffolding, and define OBJECTS entries such as dictionaries and index
  objects.
- Object references are represented by handle-valued group pairs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- DXF text is line-oriented group-code/value data. Useful documents may include HEADER, TABLES, OBJECTS, handles, dictionaries, and EOF markers; non-DWG and non-JSON raw inputs dispatch to the DXF reader.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- DXF is a line-oriented group-code/value format. For SPATIAL_FILTER, group codes can set a clip vertex count and 2D clip vertex coordinates; matrix-like fields also use repeated scalar group codes. LibreDWG's DXF reader dispatches object fields through dynapi metadata.

### Harness Links
- [[honggfuzz-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- DXF is a line-oriented group-code/value format with SECTION and ENDSEC delimiters. OBJECTS sections can contain dictionaries and index-like objects referenced by handle-valued group pairs.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
