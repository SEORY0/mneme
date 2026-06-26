---
type: format-family
title: "Pkcs15 Encode Fuzzer Input format"
description: "Descriptive contract facts for Pkcs15 Encode Fuzzer Input."
resource: "cybergym://format/pkcs15-encode-fuzzer-input"
tags: ["pkcs15-encode-fuzzer-input", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The relevant family is PKCS#15/OpenSC data, likely ASN.1 or simulated card/profile chunks depending on the fuzzer. The bug shape requires a recognized tag and an output-size relation that exceeds a fixed local buffer while the surrounding object remains encodable.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
