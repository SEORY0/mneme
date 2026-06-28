---
type: format-family
title: Dwg Dxf Json Drawing Data format
description: Format contract for dwg/dxf/json drawing data inputs.
resource: cybergym://format/dwg-dxf-json-drawing-data
tags: [dwg-dxf-json-drawing-data, heap-buffer-overflow, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The libredwg fuzzer auto-detects DWG by the AC file signature, JSON by an object start, and otherwise treats input as DXF text. DWG decoding relies on version headers, section tables, object address/size metadata, and bit-packed object streams; arbitrary size corruption often fails early.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
