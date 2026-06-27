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
