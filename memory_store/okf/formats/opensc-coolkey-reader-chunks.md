---
type: format-family
title: "OPENSC Coolkey Reader Chunks Format"
description: "Round 26 descriptive structure and invariant facts for opensc-coolkey-reader-chunks."
tags: ["opensc-coolkey-reader-chunks", "round-26"]
okf_support: 1
train_only: true
---
# OPENSC Coolkey Reader Chunks Format

## Round 26 Factual Contract

### Schema / Invariants
- The reader input is a sequence of little-endian length-prefixed chunks. The first chunk is ATR data. Later APDU response chunks use trailing status bytes and optional response data before the status. Coolkey initialization can use a LIST_OBJECTS response for a combined object; that object contains a combined header, an uncompressed decompressed-object area with a token-name header, and embedded V1 Coolkey object records. Embedded private-key records need class, key type, id, usage booleans, and RSA public modulus/exponent attributes to pass PKCS#15 algorithm selection.

### Harness Links
- [[libfuzzer-pkcs15-reader]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
