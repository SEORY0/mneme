---
type: format-family
title: "CIL Policy Text format"
description: "Descriptive contract facts for CIL Policy Text."
resource: "cybergym://format/cil-policy-text"
tags: ["cil-policy-text", "round-6", "round-16"]
okf_support: 2
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

## Round 16 Factual Contract

### Schema / Invariants
- CIL policy text is S-expression based. Classpermissions must be declared before classpermissionset definitions. A classpermissionset accepts either a direct class/permissions pair or a single named classpermission/classpermissionset reference, not a nested list of named references. Optional blocks are removed when they contain unresolved references.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- CIL policies require enough global scaffolding for classorder, sidorder, user/role/type declarations, and allow rules before compilation continues into reset logic.
- Optional blocks may be removed when unresolved symbols remain inside them.
- A classcommon association links a class to a common permission set and survives as semantic state beyond simple text parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
