---
type: format
title: "Metaflac Cli Fuzzer Envelope With Cuesheet"
access_scope: generate
confidence: medium
tags: ["metaflac-cli-fuzzer-envelope-with-cuesheet", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Metaflac Cli Fuzzer Envelope With Cuesheet

## Round 13 Facts
- The underlying cuesheet parser accepts CATALOG, FILE, TRACK, and INDEX lines. Non-CDDA cuesheets may use MM:SS.SS or raw sample offsets, while CDDA requires MM:SS:FF. The described parser bug is around malformed or fractional INDEX offsets, especially a minute/colon prefix that can advance past a string terminator.
