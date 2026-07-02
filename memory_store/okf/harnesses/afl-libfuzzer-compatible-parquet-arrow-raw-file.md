---
type: harness-contract
title: "Afl Libfuzzer Compatible Parquet Arrow Raw File"
description: "Round 36 factual harness contract for afl-libfuzzer-compatible-parquet-arrow-raw-file."
tags: ["afl-libfuzzer-compatible-parquet-arrow-raw-file", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Afl Libfuzzer Compatible Parquet Arrow Raw File

## Round 36 Input Contract
- The harness feeds the entire input buffer directly to parquet::arrow::internal::FuzzReader. There is no FuzzedDataProvider layout, selector byte, or carved prefix. The target opens a BufferReader, builds a Parquet Arrow FileReader, iterates row groups with ReadRowGroup, then validates the resulting Arrow table.

## Round 36 Format Links
- [[parquet]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
