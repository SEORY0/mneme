---
type: format-family
title: "CIL Policy Text format"
description: "Descriptive contract facts for CIL Policy Text."
resource: "cybergym://format/cil-policy-text"
tags: ["cil-policy-text", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- CIL policy text uses parenthesized declarations. A classpermission declaration can be populated by classpermissionset rules, and classpermissionset bodies name class/permission pairs. Optional blocks can be disabled during resolution when a contained declaration or rule fails to resolve.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
