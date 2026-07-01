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

## Round 35 Factual Contract

### Schema / Invariants
- SOM objects are big-endian and are accepted through fixed system id, magic, version, and table-location/count fields. A space dictionary names a parent section through a shared string table and points to subspace dictionary records. The space-name path checks the string-table bound; the subspace-name path uses the same table as a raw string pointer. For this harness, a Unix archive plus SOM library map can be required so the archive-format check opens the first SOM object member.

### Harness Links
- [[libfuzzer-tempfile-bfd]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
