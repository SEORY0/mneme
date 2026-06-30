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

## Round 28 Factual Contract

### Schema / Invariants
- DXF is parsed as code/value line pairs. TABLEGEOMETRY uses scalar groups for row count, column count, and cell count, followed by repeated cell groups with a cell-start marker, dimensions, handles, geometry count, and optional geometry subrecords. Duplicate scalar groups can update object fields later in the same object.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- DXF inputs are line-oriented group-code/value pairs. A parser-reaching sample keeps the normal HEADER, CLASSES, OBJECTS, and section terminator structure, with object records introduced by a type group and carrying handle and owner fields plus object-specific flags. Object-context-data records can include optional scale-related fields whose concrete storage type varies by object class.

### Harness Links
- [[libfuzzer-libredwg-llvmfuzz]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
