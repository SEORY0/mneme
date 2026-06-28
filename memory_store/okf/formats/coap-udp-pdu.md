---
type: format-family
title: Coap Udp Pdu format
description: Format contract for coap-udp-pdu.
resource: cybergym://format/coap-udp-pdu
tags: [coap-udp-pdu]
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
- A UDP CoAP PDU begins with a compact fixed header, optional token bytes, then option encodings. Each option header encodes delta and length nibbles, with special nibble values indicating that extra bytes carry the extended value.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
