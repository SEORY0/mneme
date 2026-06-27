---
type: format
title: "Rollei Raw Text Header"
input_format: rollei-raw-text-header
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Rollei Raw Text Header

## Schema
- The Rollei path is selected by a textual raw-camera signature near the start of the file. The parser then reads newline-delimited ASCII-style metadata records with optional key/value delimiters and an end-of-header marker. Recognized keys set geometry and thumbnail offsets, but this bug can be reached during metadata parsing before a complete image payload is needed.
