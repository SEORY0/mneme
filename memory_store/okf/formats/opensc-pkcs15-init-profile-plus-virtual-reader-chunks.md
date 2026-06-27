---
type: format-family
title: "Opensc Pkcs15 Init Profile Plus Virtual Reader Chunks format"
description: "Descriptive contract facts for opensc pkcs15-init profile plus virtual-reader chunks."
resource: "cybergym://format/opensc-pkcs15-init-profile-plus-virtual-reader-chunks"
tags: ["opensc-pkcs15-init-profile-plus-virtual-reader-chunks", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The pkcs15-init harness expects a profile configuration string terminated by a NUL byte, followed by virtual-reader chunk data. The reader chunk stream supplies an ATR first and APDU response chunks afterward.

### Harness Links
- [[honggfuzz-style-pkcs15-init-harness]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
