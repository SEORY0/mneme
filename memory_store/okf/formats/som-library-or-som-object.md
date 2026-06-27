---
type: format-family
title: "Som Library Or Som Object format"
description: "Descriptive contract facts for som-library-or-som-object."
resource: "cybergym://format/som-library-or-som-object"
tags: ["som-library-or-som-object", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- SOM object fields are big-endian.
- The header points to space records, subspace records, and a shared string table.
- Space names are checked against the string-table size, while the vulnerable subspace-name path is later used as an index into the same table.
- SOM library archives use a SOM library header and directory entries pointing to embedded SOM objects.

### Harness Links
- [[libfuzzer-tempfile-bfd]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
