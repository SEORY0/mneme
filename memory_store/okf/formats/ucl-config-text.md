---
type: format-family
title: Ucl Config Text format
description: Format contract for ucl-config-text.
resource: cybergym://format/ucl-config-text
tags: [ucl-config-text]
okf_support: 10
train_only: true
---
# Schema
## Structure
Round 25 introduced descriptive facts for this carrier.

## Invariants
- Preserve parser recognition before mutating vulnerable invariants.

## Round 25 Factual Contract

### Schema / Invariants
- The harness accepts raw UCL configuration text. A simple key-value assignment with a quoted string value is enough to reach value parsing. Dollar-braced variable references inside strings are expanded when parser variables are registered; unknown or malformed braced variables can be preserved as literal text.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 27 Factual Contract

- UCL configuration text accepts dot-prefixed built-in macros.
- Macro arguments are parsed as UCL option objects, and macro bodies can be unquoted atom text, quoted text, or braced text.
- The include-family macros pass their body bytes and explicit body length to include handling; URL handling is controlled by a boolean macro option.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
