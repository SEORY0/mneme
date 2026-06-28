---
type: format-family
title: Ndpi Serialization Fdp format
description: Format contract for ndpi-serialization-fdp.
resource: cybergym://format/ndpi-serialization-fdp
tags: [ndpi-serialization-fdp]
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
- The serialization harness is not a wire format; FuzzedDataProvider bytes select serializer format, initial buffer size, repeated scalar/string/binary values, block/list operations, snapshot and rollback behavior, buffer length mutation, and deserializer cloning.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
