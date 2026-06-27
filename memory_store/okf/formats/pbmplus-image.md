---
type: format
title: "Pbmplus Image"
access_scope: generate
confidence: medium
tags: ["pbmplus-image", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Pbmplus Image

## Round 13 Facts
- For this selected target, the accepted input is a PBMPLUS image file passed as raw fuzzer bytes. Raw PPM pixmaps and PGM graymaps with ordinary Netpbm headers and complete pixel payloads are accepted by the twelve-bit image loader; JPEG seeds and BMP seeds are dead ends for this target build. High-precision PBMPLUS samples are also accepted, with sample conversion handled by the loader.
