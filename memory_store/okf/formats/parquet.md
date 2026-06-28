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
