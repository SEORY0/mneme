---
type: format-family
title: "DER Ecdsa Signature format"
description: "Structure and invariants for the der-ecdsa-signature input format."
tags: ["der-ecdsa-signature", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- An ECDSA signature in this path is a DER sequence containing two INTEGER values interpreted as r and s. The converter allocates decoded integer buffers, rejects decoded components larger than half of the caller-provided output buffer, then left-pads r and s into a fixed-width R/S buffer.

### Harness Links
- [[libfuzzer-opensc-asn1-sig-value]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
