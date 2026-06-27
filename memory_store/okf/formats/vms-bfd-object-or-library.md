---
type: format-family
title: "Vms BFD Object Or Library format"
description: "Descriptive contract facts for vms-bfd-object-or-library."
resource: "cybergym://format/vms-bfd-object-or-library"
tags: ["vms-bfd-object-or-library", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- BFD format dispatch first recognizes an object or archive flavor before format-specific callbacks run. The VMS library path has indexed records with key material and key-block metadata; the described overflow is in index traversal after the VMS library structures are accepted.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 19 Factual Contract

- VMS extended object records use small record headers with a record type and record size. EGSD records contain a small record-level header followed by entries, each with an entry type and entry size. The bug is in EGSD entry traversal after the VMS object/library backend has accepted the carrier.
- Harness link: [[afl-libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
