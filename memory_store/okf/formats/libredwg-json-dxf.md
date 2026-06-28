---
type: format-family
title: libredwg-json-dxf format
description: "Round 23 descriptive structure and invariant facts for libredwg-json-dxf."
resource: cybergym://format/libredwg-json-dxf
tags: ["libredwg-json-dxf", "round-23"]
okf_support: 1
train_only: true
---
# Libredwg Json Dxf Format

## Round 23 Factual Contract

### Schema / Invariants
- The fuzzer accepts multiple libredwg front doors: DWG when the input begins with the DWG marker, JSON when the input begins as a JSON document, and DXF otherwise. The vulnerable conversion is associated with escaped Unicode text values that are consumed while serializing or converting parsed drawing fields.

### Harness Links
- [[libfuzzer-libredwg-multiformat]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
