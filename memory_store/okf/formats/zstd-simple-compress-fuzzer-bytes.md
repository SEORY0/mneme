---
type: format
title: "Zstd Simple Compress Fuzzer Bytes"
access_scope: generate
confidence: medium
tags: ["zstd-simple-compress-fuzzer-bytes", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Zstd Simple Compress Fuzzer Bytes

## Round 13 Facts
- The input is not a zstd frame. The fuzzer treats a prefix of the raw bytes as source data to compress and consumes suffix bytes as parameter data. Repetitive source prefixes are valid inputs; zstd magic or compressed frames have no special meaning to this target except as ordinary source bytes.
