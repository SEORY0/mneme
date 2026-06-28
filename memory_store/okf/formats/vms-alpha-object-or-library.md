---
type: format-family
title: "vms-alpha-object-or-library format"
description: "Structure and invariants observed for vms-alpha-object-or-library."
resource: "cybergym://format/vms-alpha-object-or-library"
tags: ["vms-alpha-object-or-library", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The relevant parser is BFD VMS Alpha support. It expects structured VMS object or library records rather than arbitrary EVAX text; descriptor, value-specification, type-specification, and DST records are interpreted only after the BFD target accepts the file.

### Harness Links
- [[honggfuzz-libfuzzer-binutils-objdump-wrapper]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
