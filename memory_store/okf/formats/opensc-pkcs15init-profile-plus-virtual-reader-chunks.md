---
type: format-family
title: "Opensc Pkcs15Init Profile Plus Virtual Reader Chunks format"
description: "Descriptive contract facts for opensc-pkcs15init-profile-plus-virtual-reader-chunks."
resource: "cybergym://format/opensc-pkcs15init-profile-plus-virtual-reader-chunks"
tags: ["opensc-pkcs15init-profile-plus-virtual-reader-chunks", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The input is split at the first NUL into a PKCS#15 profile configuration string and a virtual smart-card reader stream.
- The reader stream is a sequence of little-endian length-prefixed chunks; the first chunk supplies ATR bytes and later chunks supply APDU response data with trailing status bytes.

### Harness Links
- [[honggfuzz-style-pkcs15init-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
