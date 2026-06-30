---
type: format-family
title: "Pkcs8 Private Key Format"
description: "Round 26 descriptive structure and invariant facts for pkcs8-private-key."
tags: ["pkcs8-private-key", "round-26"]
okf_support: 1
train_only: true
---
# Pkcs8 Private Key Format

## Round 26 Factual Contract

### Schema / Invariants
- The harness input is a PKCS#8 PrivateKeyInfo, either DER or PEM. The outer structure contains a version, an AlgorithmIdentifier, and an OCTET STRING containing the algorithm-specific private key. EC private keys use an ECPrivateKey SEQUENCE with version and private scalar, optionally carrying parameters or a public point; when the public point is absent Botan derives it from the domain base point. Explicit EC domain parameters are a SEQUENCE containing a prime-field descriptor, curve coefficients encoded as OCTET STRING values, an encoded base point, an order, and a cofactor. DH/DSA private keys use AlgorithmIdentifier parameters carrying group integers, and the private-key OCTET STRING contains a DER INTEGER scalar.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
