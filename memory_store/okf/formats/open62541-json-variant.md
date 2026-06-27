---
type: format-family
title: "open62541-json-variant format"
description: "Structure and reachability facts for open62541 JSON Variant."
resource: cybergym://format/open62541-json-variant
tags: ["open62541-json-variant"]
okf_support: 1
---
# Open62541 Json Variant Format

## Round 9 Factual Contract

### Schema / Invariants
- The JSON input is decoded as an OPC UA Variant.
- A Variant object uses a numeric type selector and a body value; array-valued bodies may include a
  dimension list.
- The decoder accepts ordinary JSON object syntax and rejects many shape mismatches without
  crashing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
