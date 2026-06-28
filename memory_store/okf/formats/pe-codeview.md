---
type: format-family
title: Pe Codeview format
description: Format contract for pe-codeview.
resource: cybergym://format/pe-codeview
tags: [pe-codeview]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- A PE CodeView input needs a DOS stub, PE signature, COFF file header, optional header with debug data-directory entry, and a section whose virtual address maps the debug directory. The debug directory entry carries type, data size, data RVA, and raw file pointer for CodeView data.

### Harness Links
- [[libfuzzer-file-command-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
