---
type: format-family
title: "Libredwg DWG DXF JSON"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["libredwg-dwg-dxf-json", "format_contract"]
okf_support: 0
---
# Libredwg DWG DXF JSON

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- The harness selects the binary DWG decoder from a DWG-style prefix, the JSON reader from an object-starting JSON input, and otherwise the DXF reader. DXF is line-oriented group-code/value text with SECTION records, section names, ENDSEC terminators, and EOF termination; the DXF reader allocates global DXF state and a default block header after the size and non-DWG gates. JSON is parsed in two passes with a token array and object map allocated after a syntactically valid root object; schema errors can then return critical parse status. DWG seed truncation preserves the binary decoder gate but fails during decode.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
