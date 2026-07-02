---
type: format-family
title: "Asn1 Der RSA Key"
description: "Round 19 factual format contract for asn1-der-rsa-key."
resource: cybergym://format/asn1-der-rsa-key
tags: ["asn1-der-rsa-key", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Asn1 Der RSA Key

## Round 19 Factual Contract

- The RSA parser accepts DER sequences for PKCS#1 public/private keys and PKCS#8 public/private wrappers. PKCS#8 RSA detection is an algorithm identifier sequence containing the RSA object identifier. Public PKCS#8 then reads a BIT STRING and recursively parses the copied bit-string payload as PKCS#1 DER. DER integer decoding rejects negative or redundantly encoded integers; BIT STRING decoding requires at least the unused-bit count byte but does not validate that the count is within the content bit length.
- Harness link: [[honggfuzz-libfuzzer-entry]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 38 Factual Contract

### Schema / Invariants
- DER objects are tag-length-value records; SEQUENCE is constructed, INTEGER and BIT STRING are primitive. The RSA parser first enters a top-level sequence, then distinguishes PKCS#1 and PKCS#8 forms. PKCS#8 RSA detection expects an algorithm-identifier sequence containing the RSA object identifier. A PKCS#8 public key then reads a BIT STRING and recursively parses a copied buffer as PKCS#1 DER. DER BIT STRING content begins with an unused-bit count octet followed by the actual bit payload; the vulnerable decoder represented the bitmap size using the full content length instead of only the payload length.

### Harness Links
- [[honggfuzz-libfuzzer-compatible]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
