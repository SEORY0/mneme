---
type: format
title: "Dng Tiff Rawspeed Camera File"
input_format: dng-tiff-rawspeed-camera-file
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Dng Tiff Rawspeed Camera File

## Schema
- DNG inherits TIFF byte order, IFD entries, baseline image dimensions, strip metadata, and DNG private tags before RawSpeed constructs opcode objects. The target opcode relation is rowPitch/colPitch used while iterating a region of interest over decoded pixel planes.
