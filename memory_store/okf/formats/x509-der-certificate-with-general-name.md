---
type: format
title: "X509 Der Certificate With General Name"
access_scope: generate
confidence: medium
tags: ["x509-der-certificate-with-general-name", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# X509 Der Certificate With General Name

## Round 13 Facts
- The relevant structure is an X.509 DER certificate containing a subjectAltName extension with an otherName GeneralName. OtherName contains an object identifier and an explicitly tagged ASN.1 value; the vulnerable printers choose the expected value type from the object identifier rather than from the parsed ASN1_TYPE tag.
