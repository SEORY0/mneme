---
type: format
title: "Postscript Pdf Truetype"
access_scope: generate
confidence: medium
tags: ["postscript-pdf-truetype", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Postscript Pdf Truetype

## Round 13 Facts
- The vulnerable path is Ghostscript's bundled FreeType TrueType interpreter. Reaching it requires a document-level font object or Type 42 font that is valid enough to load a TrueType program and execute glyph bytecode.
