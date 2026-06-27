---
type: format-family
title: "zip-archive format"
description: "Descriptive format contract facts for zip-archive."
tags: ["zip-archive", "round-18"]
okf_support: 1
train_only: true
---
# ZIP Archive Format

## Round 18 Factual Contract

### Schema / Invariants
- ZIP local and central records can preserve member order and can contain a zero-length file whose path is also a prefix of a later member path. KArchive interprets path prefixes as directories during archive tree construction even if an earlier member used that prefix as a file.

### Harness Links
- [[afl-style-file-fuzzer-for-kimgio-karchive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
