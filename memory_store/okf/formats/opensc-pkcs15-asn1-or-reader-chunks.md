---
type: format-family
title: "Opensc Pkcs15 ASN1 Or Reader Chunks format"
description: "Structure and invariants for the opensc-pkcs15-asn1-or-reader-chunks input format."
tags: ["opensc-pkcs15-asn1-or-reader-chunks", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The decode fuzzer accepts raw DER-like PKCS#15 records and invokes multiple object decoders repeatedly. The reader fuzzer models a smart-card reader as a front-to-back sequence of little-endian length-prefixed response chunks; the first chunk seeds the ATR, later chunks become APDU responses with status bytes at the end of each response.

### Harness Links
- [[libfuzzer-opensc-pkcs15]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
