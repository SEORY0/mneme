---
type: format-family
title: "VMS Ia64 Library Archive Format"
description: "Round 27 descriptive format facts for vms-ia64-library-archive."
resource: cybergym://format/vms-ia64-library-archive
tags: ["vms-ia64-library-archive", "round-27"]
okf_support: 1
---
# VMS Ia64 Library Archive Format

## Round 27 Factual Contract

- A VMS IA-64 library archive is block-oriented.
- The first block carries a library header, sanity and version fields, a type field, index counts, and index descriptors.
- Index blocks carry used-byte counts followed by IA-64 index records with an RFA, key length, flags, and key bytes.

### Harness Links
- [[libfuzzer-bfd-tempfile]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- A VMS IA-64 library is block-oriented. The first block contains a library type, sanity/version fields, index counts, module counts, and index descriptors. Each index descriptor points to an index block. An index block has a used-byte count followed by IA-64 index entries containing an RFA, key length, flags, and key bytes. The parser traverses entries until the used-byte boundary.

### Harness Links
- [[libfuzzer-bfd-tempfile]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
