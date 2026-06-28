---
type: format-family
title: P11 Kit Rpc Message format
description: Format contract for p11-kit-rpc-message.
resource: cybergym://format/p11-kit-rpc-message
tags: [p11-kit-rpc-message]
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
- p11-kit RPC messages begin with a big-endian call identifier, a part count/signature, then typed fields. Attribute arrays encode an attribute count followed by attributes. Each attribute has a type, a validity marker, a declared value length, and a value encoded according to the attribute type. Template attributes are array-valued and can encode nested attributes.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
