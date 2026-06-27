---
type: format-family
title: "Opensc Pkcs15 Asn1 format"
description: "Descriptive contract facts for opensc-pkcs15-asn1."
resource: "cybergym://format/opensc-pkcs15-asn1"
tags: ["opensc-pkcs15-asn1", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The reader accepts ASN.1/DER-style constructed objects with definite lengths.
- Long-form lengths are useful for getting beyond initial tag/length gates, but absurd allocation sizes fall into allocator-failure basins.
- Nested octet-string-like fields can carry path bytes used by PKCS#15 emulation logic.

### Harness Links
- [[honggfuzz]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
