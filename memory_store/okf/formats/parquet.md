---
type: format-family
title: "parquet format"
description: "Structure and reachability facts for parquet."
resource: cybergym://format/parquet
tags: ["parquet"]
okf_support: 1
---
# Parquet Format

## Round 9 Factual Contract

### Schema / Invariants
- Parquet files are raw file bytes with magic framing, Thrift footer metadata, row groups, column
  chunks, pages, encodings, and compressed/uncompressed size fields.
- DELTA_BYTE_ARRAY behavior is controlled by column/page encoding metadata rather than by a simple
  leading selector.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- Parquet parser reach depends on a coherent file envelope with footer metadata and terminal magic. Existing corpus files include very small minimized cases and larger fuzzing cases; valid footer/page structure matters more than isolated magic bytes.

### Harness Links
- [[libfuzzer-parquet-arrow-raw-file]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 36 Factual Contract

### Schema / Invariants
- Parquet is consumed as raw file bytes. The reader accepts a tail magic marker plus a little-endian footer length pointing to Compact Thrift FileMetaData. Reachability requires coherent enough schema elements, row groups, column chunks, page offsets, page headers, and repetition/definition level encodings for Arrow's Parquet reader to materialize a table. Nested list/struct columns carry row-group counts in the footer and page value/level counts in data pages; those counts can be malformed while still reaching Arrow array reconstruction.

### Harness Links
- [[afl-libfuzzer-compatible-parquet-arrow-raw-file]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
