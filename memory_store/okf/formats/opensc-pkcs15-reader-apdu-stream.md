---
type: format-family
title: "Opensc Pkcs15 Reader Apdu Stream"
description: "Round 19 factual format contract for opensc-pkcs15-reader-apdu-stream."
resource: cybergym://format/opensc-pkcs15-reader-apdu-stream
tags: ["opensc-pkcs15-reader-apdu-stream", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Opensc Pkcs15 Reader Apdu Stream

## Round 19 Factual Contract

- The fuzz input is a sequence of little-endian length-prefixed chunks. The first chunk is used as ATR data for virtual card connection, while later chunks model APDU response data with status bytes at the end. For this bug, the relevant response is a TCOS password-description record encoded as TLV-like bytes read during PIN metadata insertion.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
