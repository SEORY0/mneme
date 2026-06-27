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
