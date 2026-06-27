---
type: format
title: "Zstd Simple Compress Fuzzer Bytes"
input_format: zstd-simple-compress-fuzzer-bytes
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Zstd Simple Compress Fuzzer Bytes

## Schema
- The input is not a zstd frame. The fuzzer treats a prefix of the raw bytes as source data to compress and consumes suffix bytes as parameter data. Repetitive source prefixes are valid inputs; zstd magic or compressed frames have no special meaning to this target except as ordinary source bytes.
