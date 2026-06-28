---
type: format-family
title: bfd-object-or-archive format
description: "Round 23 descriptive structure and invariant facts for bfd-object-or-archive."
resource: cybergym://format/bfd-object-or-archive
tags: ["bfd-object-or-archive", "round-23"]
okf_support: 1
train_only: true
---
# Bfd Object Or Archive Format

## Round 23 Factual Contract

### Schema / Invariants
- The relevant ECOFF path needs a recognizable object with a file header, optional header, section headers, and a symbolic debug header whose counts and offsets describe external symbols and external string data. The described bug depends on string-section termination and count/offset consistency after BFD accepts the object.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
