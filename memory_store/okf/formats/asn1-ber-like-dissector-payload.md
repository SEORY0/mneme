---
type: format-family
title: "Asn1 Ber Like Dissector Payload format"
description: "Descriptive contract facts for asn1-ber-like dissector payload."
resource: "cybergym://format/asn1-ber-like-dissector-payload"
tags: ["asn1-ber-like-dissector-payload", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- BER-style ASN.1 data is tag-length-value encoded.
- Constructed values can nest child objects, and long or indefinite length forms can drive buffer-pointer advancement only after the containing protocol has selected the ASN.1 decoder.

### Harness Links
- [[libfuzzer-fuzzshark]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
