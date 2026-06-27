---
type: format
title: "Dng Tiff Rawspeed Camera File"
access_scope: generate
confidence: medium
tags: ["dng-tiff-rawspeed-camera-file", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Dng Tiff Rawspeed Camera File

## Round 13 Facts
- DNG inherits TIFF byte order, IFD entries, baseline image dimensions, strip metadata, and DNG private tags before RawSpeed constructs opcode objects. The target opcode relation is rowPitch/colPitch used while iterating a region of interest over decoded pixel planes.
