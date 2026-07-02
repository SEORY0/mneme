---
type: format-family
title: "sas7bdat format"
description: "Structure and invariants observed for sas7bdat."
resource: "cybergym://format/sas7bdat"
tags: ["sas7bdat", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- SAS7BDAT files start with a fixed magic header that selects endian, 32-bit versus 64-bit layout, encoding, header size, page size, and page count. Pages follow the file header; 32-bit pages use a smaller page header and subheader pointer entries than 64-bit pages. Metadata pages store the page type and subheader count in the page header, then a pointer table. Each pointer gives a subheader offset, length, compression mode, and a data/compressed flag. Subheaders begin with recognized signatures for row size, column size, column text, column names, column attributes, column formats, or related column-list records.

### Harness Links
- [[afl]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
