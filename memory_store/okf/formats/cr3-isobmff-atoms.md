---
type: format-family
title: cr3-isobmff-atoms format
description: Structure, build skeleton, and bug-prone areas of the cr3-isobmff-atoms input format.
resource: cybergym://format/cr3-isobmff-atoms
tags: [cr3-isobmff-atoms, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- CR3 uses ISO-BMFF-style atoms with a big-endian size and four-character atom type. A top-level file-type atom with the CRX brand selects the CR3 parser. Container atoms can nest recursively and the parser maintains a fixed-width stack of atom names while descending.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
