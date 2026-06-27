---
type: format
title: "Dxf Or Json Cad"
input_format: dxf-or-json-cad
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Dxf Or Json Cad

## Schema
- The fuzzer sniffs DWG by an AC prefix, JSON by an opening brace, and otherwise treats input as DXF text. DXF is group-code text with SECTION records such as HEADER, CLASSES, ENTITIES, and OBJECTS; object type names and subclass markers are carried as string-valued group pairs and become dxfname-related fields during import.
