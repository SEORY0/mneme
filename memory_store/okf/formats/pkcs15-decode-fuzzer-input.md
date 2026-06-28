---
type: format-family
title: "pkcs15-decode-fuzzer-input format"
description: "Structure and invariants for the pkcs15-decode-fuzzer-input input format."
tags: ["pkcs15-decode-fuzzer-input", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The decode fuzzer input is split into an initial length-delimited PKCS#15/ASN.1 test buffer followed by simulated reader/APDU data. The target tries several PKCS#15 directory-entry decoders, then decodes public keys for multiple algorithms, tokeninfo, and unused-space structures from the test buffer.

### Harness Links
- [[honggfuzz-wrapper]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
