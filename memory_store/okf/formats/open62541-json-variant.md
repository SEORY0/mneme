---
type: format-family
title: "open62541-json-variant format"
description: "Structure and reachability facts for open62541 JSON Variant."
resource: cybergym://format/open62541-json-variant
tags: ["open62541-json-variant"]
okf_support: 2
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

## Round 29 Factual Contract

### Schema / Invariants
- open62541 JSON Variant values are JSON objects with a numeric type selector and a body field. A body encoded as a JSON array makes the Variant an array value, and optional dimensions are represented by a separate dimension field. Builtin types are decoded directly; non-builtin values are wrapped through ExtensionObject handling. Variant arrays may contain Variant elements, which creates a valid recursive carrier while preserving the top-level Variant schema.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- The input is raw JSON decoded as an OPC UA Variant. A Variant is an object with a numeric type selector and Body value; array-valued bodies make the Variant an array, and an optional Dimension array describes multidimensional values. Builtin bodies are decoded directly. ExtensionObject bodies carry a type identifier, optional encoding marker, and nested Body; unknown structure-encoded bodies can be stored or skipped by recursive token walking. ByteString bodies are base64 text before being stored as bytes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
