---
type: format-family
title: "Php Source format"
description: "Descriptive contract facts for php-source."
resource: "cybergym://format/php-source"
tags: ["php-source", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The input is PHP source text, not serialized PHP data.
- Property hooks are declared in class property syntax, lazy objects are created through ReflectionClass, and foreach over an object asks the object handler for an iterator over declared and dynamic properties.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
