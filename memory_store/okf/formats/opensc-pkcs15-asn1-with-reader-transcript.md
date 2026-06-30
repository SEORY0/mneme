---
type: format-family
title: "OPENSC Pkcs15 ASN1 With Reader Transcript Format"
description: "Round 26 descriptive structure and invariant facts for opensc-pkcs15-asn1-with-reader-transcript."
tags: ["opensc-pkcs15-asn1-with-reader-transcript", "round-26"]
okf_support: 1
train_only: true
---
# OPENSC Pkcs15 ASN1 With Reader Transcript Format

## Round 26 Factual Contract

### Schema / Invariants
- The parsed object is DER-style ASN.1 for OpenSC PKCS#15 public-key decoding. EC public keys carry an EC point as an OCTET STRING; the ASN.1 layer can produce an empty value for that field even though later EC-key handling expects at least one byte of point data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
