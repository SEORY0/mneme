---
type: format-family
title: "Cryptofuzz Wolfssl Dh Operation format"
description: "Structure and invariants for the cryptofuzz-wolfssl-dh-operation input format."
tags: ["cryptofuzz-wolfssl-dh-operation", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The vulnerable library path concerns Diffie-Hellman SP math and key-size support, not a certificate parser. Reaching it likely requires an operation record containing a DH operation selector plus bignum fields for group parameters and peer/private values. Raw DER DH parameters are useful seeds only when the harness actually imports ASN.1, which this task did not show.

### Harness Links
- [[cryptofuzz-or-wolfssl-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
