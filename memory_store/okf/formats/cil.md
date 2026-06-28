---
type: format-family
title: "Cil"
description: "Round 12 factual format contract for cil."
resource: cybergym://format/cil
tags: ["cil", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Cil

## Round 12 Factual Contract

### Schema / Invariants
- CIL is an S-expression policy language. A compilable policy needs baseline declarations for classes, ordering, identities, roles, types, categories, sensitivities, contexts, and allows. Blocks and optional containers are nested S-expression scopes; blockinherit references a block symbol.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- CIL policies are S-expression text. A compilable policy needs the usual class, type, role, user, category, sensitivity, context, and file-context declarations before post-processing sorts and normalizes file-context path patterns.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
