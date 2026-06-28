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
