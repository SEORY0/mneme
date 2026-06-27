---
type: format
title: "Pef Tiff Raw"
input_format: pef-tiff-raw
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Pef Tiff Raw

## Schema
- PEF is TIFF-derived: byte order and TIFF magic lead to an IFD of typed tags, including image dimensions, compression, strip offsets, byte counts, and camera make/model metadata that influence RawSpeed decoder selection.
