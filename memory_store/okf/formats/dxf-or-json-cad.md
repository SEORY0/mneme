---
type: format
title: "Dxf Or Json Cad"
access_scope: generate
confidence: medium
tags: ["dxf-or-json-cad", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Dxf Or Json Cad

## Round 13 Facts
- The fuzzer sniffs DWG by an AC prefix, JSON by an opening brace, and otherwise treats input as DXF text. DXF is group-code text with SECTION records such as HEADER, CLASSES, ENTITIES, and OBJECTS; object type names and subclass markers are carried as string-valued group pairs and become dxfname-related fields during import.
