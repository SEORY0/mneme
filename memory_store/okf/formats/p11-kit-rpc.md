---
type: format-family
title: "P11 Kit Rpc"
description: "Abstract format facts observed during verifier-causal consolidation."
tags: ["p11-kit-rpc", "format_contract"]
okf_support: 0
---
# P11 Kit Rpc

## Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- p11-kit RPC messages are raw binary records beginning with a call selector and a length-prefixed ASCII signature. Arguments follow the call signature: unsigned longs are fixed-width network-order integers, and attribute arrays start with an element count followed by attributes. Each attribute carries a type, a validity byte, a declared value length, and a type-specific encoded value. Array-valued PKCS#11 attributes encode their value as another counted attribute list.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
