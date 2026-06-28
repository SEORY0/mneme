---
type: format-family
title: Opcua Json Variant format
description: Format contract for opcua-json-variant.
resource: cybergym://format/opcua-json-variant
tags: [opcua-json-variant]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The fuzzer decodes raw JSON as an OPC UA Variant. To reach ExtensionObject handling, the top-level object needs a Variant type selector and a body containing an ExtensionObject-like object with a type identifier, optional encoding marker, and a nested Body value. Unknown body types are stored as encoded JSON and skipped by a recursive token walker.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
