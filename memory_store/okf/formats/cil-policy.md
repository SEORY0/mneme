---
type: format-family
title: "CIL Policy format"
description: "Descriptive contract facts for CIL Policy."
resource: "cybergym://format/cil-policy"
tags: ["cil-policy", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The input format is CIL policy text. The relevant structure involves class, permission, classmapping, and map-permission constructs where classperm lists are attached during resolution and must be destroyed during AST reset.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
