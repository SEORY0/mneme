---
type: format-family
title: "dxf-text format"
description: "Structure and reachability facts for DXF text."
resource: cybergym://format/dxf-text
tags: ["dxf-text"]
okf_support: 2
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

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- DXF text is line-oriented group-code/value data. Useful documents may include HEADER, TABLES, OBJECTS, handles, dictionaries, and EOF markers; non-DWG and non-JSON raw inputs dispatch to the DXF reader.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- DXF is a line-oriented group-code/value format. For SPATIAL_FILTER, group codes can set a clip vertex count and 2D clip vertex coordinates; matrix-like fields also use repeated scalar group codes. LibreDWG's DXF reader dispatches object fields through dynapi metadata.

### Harness Links
- [[honggfuzz-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- DXF is a line-oriented group-code/value format with SECTION and ENDSEC delimiters. OBJECTS sections can contain dictionaries and index-like objects referenced by handle-valued group pairs.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 38 Factual Contract

### Schema / Invariants
- DXF text is parsed as alternating group-code and value records. Non-DWG and non-JSON inputs dispatch to the DXF reader. Some numeric point-valued records route through the generic pair reader and then through floating-point conversion, causing whitespace handling to occur in more than one layer for the same value.
- DXF text is a line-oriented group-code/value format. Sections such as HEADER, CLASSES, TABLES, BLOCKS, ENTITIES, and OBJECTS are introduced by code/value records, and entities or objects begin with a type record followed by handles, common fields, subclass markers, and type-specific fields. Point triples are represented by related coordinate group families, where an x-code establishes or allocates a point and y/z continuation codes complete it. Some newer entities use class records and subclass names before their type-specific fields are accepted. Count fields and vector fields must agree for vector parsing to reach the vulnerable path.
- LibreDWG text DXF inputs are line-oriented group-code/value records organized into sections such as HEADER, CLASSES, TABLES, BLOCKS, ENTITIES, and OBJECTS. Real parser reachability is much better from bundled DXF seeds than from minimal handcrafted objects because class declarations, owner handles, and section scaffolding influence object construction. IMAGE and WIPEOUT entities carry raster-image fields followed by a clipping mode/count and repeated 2D clip vertices. Underlay entities infer their clipping polygon from repeated 2D coordinate records and may optionally carry inverted clipping vertices. SPATIAL_FILTER is an OBJECTS-section record with a clip count, clip vertices, extrusion/origin fields, clipping flags, and transform matrices.
- DXF text is a line-oriented sequence of group-code and value pairs. A minimal parser-reaching document uses SECTION records, a HEADER section selected by a section-name pair, and header variables introduced by name/value group pairs. LibreDWG maps summary fields from HEADER variables; custom-property tags allocate entries in the summaryinfo property array, while custom-property values fill the latest entry's value member.
- DXF is a line-oriented group-code/value format with SECTION and ENDSEC structure. The harness accepts full drawings with CLASSES, ENTITIES, and OBJECTS sections. WIPEOUT entities carry a boundary type, a clip-vertex count, and repeated 2D clip coordinate pairs; SPATIAL_FILTER objects carry a clip-vertex count, clip coordinate pairs, extrusion/origin data, clipping fields, and transform-related data. Full in-repo seeds provide much better reachability than minimal standalone records.

### Harness Links
- [[libfuzzer]]
- [[libfuzzer-libredwg-llvmfuzz]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
