---
type: format
title: "Postscript Pdf Truetype"
input_format: postscript-pdf-truetype
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Postscript Pdf Truetype

## Schema
- The vulnerable path is Ghostscript's bundled FreeType TrueType interpreter. Reaching it requires a document-level font object or Type 42 font that is valid enough to load a TrueType program and execute glyph bytecode.
