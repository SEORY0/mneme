---
type: format
title: "Pbmplus Image"
input_format: pbmplus-image
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Pbmplus Image

## Schema
- For this selected target, the accepted input is a PBMPLUS image file passed as raw fuzzer bytes. Raw PPM pixmaps and PGM graymaps with ordinary Netpbm headers and complete pixel payloads are accepted by the twelve-bit image loader; JPEG seeds and BMP seeds are dead ends for this target build. High-precision PBMPLUS samples are also accepted, with sample conversion handled by the loader.
