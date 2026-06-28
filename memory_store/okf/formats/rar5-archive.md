---
type: format-family
title: "Rar5 Archive"
description: "Round 19 factual format contract for rar5-archive."
resource: cybergym://format/rar5-archive
tags: ["rar5-archive", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Rar5 Archive

## Round 19 Factual Contract

- RAR5 archives start with a marker and then a sequence of variable-length, CRC-protected block headers. File blocks carry flags, packed and unpacked sizes, names, and optional compression metadata. Mutating arbitrary bytes in a real archive often preserves recognition but either cleanly reports damaged content or skips the deep compressed-data decoder.
- Harness link: [[afl-libfuzzer-file]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 25 Factual Contract

### Schema / Invariants
- RAR5 archives start with a signature and then CRC-protected variable-length block headers. File blocks carry flags, optional extra/data size fields, host and compression metadata, and a variable-length filename field.

### Harness Links
- [[libfuzzer-libarchive-reader]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
