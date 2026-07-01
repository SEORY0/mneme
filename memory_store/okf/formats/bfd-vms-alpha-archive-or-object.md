---
type: format-family
title: "bfd-vms-alpha-archive-or-object format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/bfd-vms-alpha-archive-or-object"
tags: ["bfd-vms-alpha-archive-or-object", "round-35"]
okf_support: 1
train_only: true
---
# bfd-vms-alpha-archive-or-object Format

## Round 35 Factual Contract
### Schema / Invariants
- Alpha VMS object modules are record-based: module-header records carry repeated record sizing, subtype, structure level, architecture and record-size fields, counted module/version strings, and an end-of-module record terminates the stream. Alpha VMS libraries use a fixed library header with type, sanity id, major version, index counts, module counts, index descriptors, and variable-length ASCII index blocks; module and symbol indexes point to VMS data blocks containing member records.

### Harness Links
- [[libfuzzer-bfd-archive-only]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
