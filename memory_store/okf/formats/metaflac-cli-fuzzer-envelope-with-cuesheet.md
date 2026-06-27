---
type: format
title: "Metaflac Cli Fuzzer Envelope With Cuesheet"
input_format: metaflac-cli-fuzzer-envelope-with-cuesheet
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Metaflac Cli Fuzzer Envelope With Cuesheet

## Schema
- The underlying cuesheet parser accepts CATALOG, FILE, TRACK, and INDEX lines. Non-CDDA cuesheets may use MM:SS.SS or raw sample offsets, while CDDA requires MM:SS:FF. The described parser bug is around malformed or fractional INDEX offsets, especially a minute/colon prefix that can advance past a string terminator.
