---
type: format-family
title: Som Library Archive format
description: Format contract for som-library-archive inputs.
resource: cybergym://format/som-library-archive
tags: [som-library-archive, heap-buffer-overflow-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
SOM library archives use a Unix archive envelope. The special archive-map member stores a library-symbol-table header, hash buckets that point at symbol records, a dictionary of member locations, symbol records with name references and module indices, and a string area for symbol names.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-tempfile-bfd]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
