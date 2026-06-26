---
type: format-family
title: "Ecoff Bfd Object format"
description: "Descriptive contract facts for Ecoff Bfd Object."
resource: "cybergym://format/ecoff-bfd-object"
tags: ["ecoff-bfd-object", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- ECOFF object parsing requires a recognizable file header, optional/a.out header fields, section headers, and symbol/string table metadata consistent enough for BFD to accept the file. The vulnerable invariant concerns symbol string indexes being checked against the available string table.

### Harness Links
- [[honggfuzz-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 7 Factual Contract

### Schema / Invariants
- ECOFF/BFD parsing requires a recognizable object header, optional header fields, section metadata,
and coherent debug symbol-table metadata. The target relation involves a file descriptor record
whose symbol count is inconsistent with the remaining external symbol table.

### Harness Links
- [[honggfuzz-raw-tempfile]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
