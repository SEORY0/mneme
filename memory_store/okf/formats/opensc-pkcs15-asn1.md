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

## Round 26 Factual Contract


### Schema / Invariants
- The direct PKCS#15 decoder accepts a top-level constructed private-key choice. The object body contains common object attributes, common key attributes with an identifier and usage bit field, an optional private-key subclass section carrying a subject-name sequence, and a required type-specific key-attribute section such as RSA path and size data. Definite-length DER-like constructed fields are enough; a full smart-card transcript is not required for this harness.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
