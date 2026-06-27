---
type: format
title: "Postscript Pdf Font"
access_scope: generate
confidence: medium
tags: ["postscript-pdf-font", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Postscript Pdf Font

## Round 13 Facts
- Ghostscript accepts PostScript and PDF inputs and can route embedded or declared fonts through FreeType. The described bug depends on a glyph rendering path where a fallback return code is ignored and partially initialized glyph bitmap data is later consumed.
