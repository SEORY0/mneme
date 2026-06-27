---
type: format
title: "Pef Tiff Raw"
access_scope: generate
confidence: medium
tags: ["pef-tiff-raw", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Pef Tiff Raw

## Round 13 Facts
- PEF is TIFF-derived: byte order and TIFF magic lead to an IFD of typed tags, including image dimensions, compression, strip offsets, byte counts, and camera make/model metadata that influence RawSpeed decoder selection.
