---
type: format
title: "Heif Isobmff"
input_format: heif-isobmff
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Heif Isobmff

## Schema
- The handler recognizes ISO BMFF HEIF files by a leading file-type box with supported HEIF brands. Structurally valid seeds include ftyp plus a HEIF box graph that libheif can load and decode; short ftyp-only carriers reach the handler but are rejected by libheif as unsupported or incomplete.
