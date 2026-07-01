---
type: format-family
title: "Pkcs12 Der"
description: "Round 7 factual format contract for pkcs12-der."
resource: cybergym://format/pkcs12-der
tags: ["pkcs12-der", "format-contract", "round-7"]
okf_support: 2
train_only: true
---
# Pkcs12 Der

## Round 7 Factual Contract

### Schema / Invariants
- PKCS#12 DER inputs are ASN.1 containers holding authenticated safe bags. The target parser imports
the whole DER blob, verifies or ignores the MAC, decrypts encrypted bags with the harness password,
then searches bags for a private key, matching certificate chain, extra certificates, and optional
CRL.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- PKCS#12 DER is an ASN.1 container with authenticated safe contents and nested bags for private keys, certificates, and optional CRLs. Valid encrypted-safe structure can be retained while perturbing decrypted bag contents enough to make one imported object fail after its output has been initialized.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
