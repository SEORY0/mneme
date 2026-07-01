---
type: format-family
title: Coap Udp Pdu format
description: Format contract for coap-udp-pdu.
resource: cybergym://format/coap-udp-pdu
tags: [coap-udp-pdu]
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
- A UDP CoAP PDU begins with a compact fixed header, optional token bytes, then option encodings. Each option header encodes delta and length nibbles, with special nibble values indicating that extra bytes carry the extended value.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 27 Factual Contract

- A UDP CoAP PDU begins with a compact fixed header containing version, type, token-length, code, and message-id fields.
- Optional token bytes are followed by option encodings.
- Each option encodes a delta and length nibble, with extended forms for larger values, and options continue until a payload marker or the end of the message.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- A UDP CoAP PDU has a compact fixed header carrying version, type, token length, code, and message id, followed by an optional token and then option records. Each option record encodes option delta and value length in header nibbles; selected nibble values require additional extension bytes before the option value. A payload marker terminates the option stream, and bytes after it are payload rather than options.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
