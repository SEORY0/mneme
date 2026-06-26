---
type: format-family
title: "Pkcs12 Der"
description: "Round 7 factual format contract for pkcs12-der."
resource: cybergym://format/pkcs12-der
tags: ["pkcs12-der", "format-contract", "round-7"]
okf_support: 1
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
