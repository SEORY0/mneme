---
type: format-family
title: "Opensc Smart Card Response Stream Asn 1 format"
description: "Descriptive contract facts for Opensc Smart Card Response Stream Asn 1."
resource: "cybergym://format/opensc-smart-card-response-stream-asn-1"
tags: ["opensc-smart-card-response-stream-asn-1", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The reader harness consumes a sequence of little-endian chunk lengths followed by chunk payloads. The first chunk becomes the ATR, and later chunks are returned as APDU responses with status bytes taken from the tail of each response. The OpenPGP code parses algorithm-attribute data objects where the first byte selects RSA or EC and later bytes may be copied into an object identifier representation.

### Harness Links
- [[honggfuzz-libfuzzer-file-input-to-pkcs15-reader]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
