---
type: format
title: "Postscript Pdf Font"
input_format: postscript-pdf-font
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Postscript Pdf Font

## Schema
- Ghostscript accepts PostScript and PDF inputs and can route embedded or declared fonts through FreeType. The described bug depends on a glyph rendering path where a fallback return code is ignored and partially initialized glyph bitmap data is later consumed.
