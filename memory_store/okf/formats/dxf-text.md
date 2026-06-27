---
type: format-family
title: "dxf-text format"
description: "Structure and reachability facts for DXF text."
resource: cybergym://format/dxf-text
tags: ["dxf-text"]
okf_support: 1
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
