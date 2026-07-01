---
type: format-family
title: "Opensc Cardos Fake Reader Apdu Format"
description: "Structure, build skeleton, and bug-prone areas of the opensc-cardos-fake-reader-apdu input format."
resource: "cybergym://format/opensc-cardos-fake-reader-apdu"
tags: ["opensc-cardos-fake-reader-apdu", "round-37"]
okf_support: 1
train_only: true
---
# Opensc Cardos Fake Reader Apdu Format
## Round 37 Factual Contract

### Schema / Invariants
- The OpenSC fake reader stream is a sequence of length-prefixed chunks.
- The first chunk is interpreted as the card ATR.
- Later chunks are APDU responses, where the status word is stored at the end of each response and the preceding body becomes the APDU response data.
- CardOS initialization issues version and package-list queries, and the package list is parsed as ASN.1 tag/length/value records.
- Long-form ASN.1 lengths consume more header bytes than the short-form case, which matters for remaining-length accounting.

### Harness Links
- [[libfuzzer-pkcs15-reader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
