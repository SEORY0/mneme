---
type: format
title: "X509 Der Certificate With General Name"
access_scope: generate
confidence: medium
tags: ["x509-der-certificate-with-general-name", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
okf_support: 1
---
# X509 Der Certificate With General Name

## Round 13 Facts
- The relevant structure is an X.509 DER certificate containing a subjectAltName extension with an otherName GeneralName. OtherName contains an object identifier and an explicitly tagged ASN.1 value; the vulnerable printers choose the expected value type from the object identifier rather than from the parsed ASN1_TYPE tag.

## Round 33 Factual Contract

### Schema / Invariants
- The selected input is a DER X.509 certificate. X.509 extensions are carried as OCTET STRING-wrapped DER payloads. subjectAltName decodes as a sequence of GeneralName values. The otherName choice is context-tagged and contains an object identifier plus an explicitly tagged ASN1_ANY value. OpenSSL maps some recognized otherName identifiers to expected UTF8String or IA5String values during printing instead of checking the parsed ASN1_TYPE tag.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
