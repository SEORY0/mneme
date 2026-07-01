---
type: format-family
title: "alpha-ecoff-archive format"
description: "Descriptive format contract facts for alpha-ecoff-archive."
tags: ["alpha-ecoff-archive", "round-18"]
okf_support: 1
train_only: true
---
# Alpha ECOFF Archive Format

## Round 18 Factual Contract

### Schema / Invariants
- The format is a SysV-style archive with a global archive signature followed by fixed-width member headers. Alpha ECOFF accepts a compressed-member terminator distinct from ordinary archive members; such members begin with a dummy ECOFF file header, then an advertised uncompressed size, then compressed stream metadata and dictionary-coded payload.

### Harness Links
- [[libfuzzer-bfd-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- Alpha ECOFF archives use the ar global signature and fixed-width member headers. A target-specific ECOFF archive map member selects the Alpha ECOFF archive handling path during BFD archive probing. Compressed archive members use a distinct member terminator and contain a dummy ECOFF file header, an advertised uncompressed-size field, an auxiliary field, and a dictionary-coded stream whose control bits decide whether output bytes are copied from the dictionary or read literally from the member.

### Harness Links
- [[libfuzzer-bfd-archive]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
