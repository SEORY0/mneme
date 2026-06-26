---
type: format-family
title: "Pef Object format"
description: "Descriptive contract facts for Pef Object."
resource: "cybergym://format/pef-object"
tags: ["pef-object", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- A PEF object begins with PEF magic tags, architecture and version fields, then section headers. A code section can contain a zero marker followed by a PowerPC traceback table. The traceback table must declare both routine-name presence and traceback-offset presence before the routine name is parsed.

### Harness Links
- [[afl-file]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
