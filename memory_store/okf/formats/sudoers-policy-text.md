---
type: format-family
title: Sudoers Policy Text format
description: Format contract for sudoers-policy-text.
resource: cybergym://format/sudoers-policy-text
tags: [sudoers-policy-text]
okf_support: 0
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The active input format is sudoers policy syntax, including user specifications, aliases, and Defaults entries. It is not the sudo.conf plugin configuration format even though the described bug concerns plugin options.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
## Round 37 Factual Contract

### Schema / Invariants
- Sudoers policy text contains user specifications with host assignments, optional runas information, command tags/options, and a command list.
- Path-valued command options are parsed before a command and can be repeated in a command specification.
- Repeating an option in the same command spec exercises replacement semantics; placing options across comma-separated specs can follow a different propagation path and may not trigger the stale leak-list entry.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
