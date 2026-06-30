---
type: format-family
title: Libredwg Json format
description: Format contract for libredwg-json inputs.
resource: cybergym://format/libredwg-json
tags: [libredwg-json, stack-buffer-overflow-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
LibreDWG JSON accepts a top-level object with a HEADER member. Header keys map to dynamic metadata entries, and primitive numeric values are converted by the JSON importer before being assigned through the dynamic API. Unknown or late fields can stop progress, so a compact set of known primitive header names is preferable.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- libredwg's JSON input is a top-level object with section objects. FILEHEADER metadata controls the DWG version used by later sections, and HEADER keys are looked up through dynapi metadata. For pre-R13 versions, selected header string variables are handled as fixed TFv strings even though the JSON token is ordinary text.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
