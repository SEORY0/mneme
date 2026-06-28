---
type: format-family
title: "Dxf format"
description: "Descriptive contract facts for Dxf."
resource: "cybergym://format/dxf"
tags: ["dxf", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The libredwg harness treats inputs beginning with the DWG signature as DWG, inputs beginning with JSON syntax as JSON, and otherwise dispatches to the DXF text reader. DXF records are group-code/value pairs, and complete versioned seed files contain the headers and section ordering needed to reach entity parsing.

### Harness Links
- [[libfuzzer-raw-dwg-dxf-json-dispatcher]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- DXF is a line-oriented group-code/value format. The relevant GDAL path parses entities such as LEADER and computes BSpline control points from data points, degree, and tangent information; an environment/config limit bounds the maximum generated control points.

### Harness Links
- [[libfuzzer-vsimem-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- DXF is parsed as group-code/value records. Header variables live in a HEADER section; summary metadata can include custom property tags and values, where a tag allocates a property slot and a later value initializes the paired value field.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
