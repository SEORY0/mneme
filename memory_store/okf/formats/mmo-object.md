---
type: format-family
title: "mmo-object format"
description: "Structure and reachability facts for mmo-object."
resource: cybergym://format/mmo-object
tags: ["mmo-object"]
okf_support: 1
---
# Mmo Object Format

## Round 9 Factual Contract

### Schema / Invariants
- MMO files are word-aligned record streams with a preamble, location records, optional special-
  section descriptors, data words, symbol-table marker, and final end record.
- The vulnerable allocator stores section-content chunks by virtual address and checks whether
  requested ranges fit existing chunks using address plus size arithmetic.

### Harness Links
- [[honggfuzz-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
