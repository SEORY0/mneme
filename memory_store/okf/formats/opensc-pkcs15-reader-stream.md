---
type: format-family
title: "Opensc Pkcs15 Reader Stream"
description: "Round 19 factual format contract for opensc-pkcs15-reader-stream."
resource: cybergym://format/opensc-pkcs15-reader-stream
tags: ["opensc-pkcs15-reader-stream", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Opensc Pkcs15 Reader Stream

## Round 19 Factual Contract

- The input is a synthetic smart-card reader stream made of repeated two-byte little-endian chunk lengths followed by response chunks. APDU transmit responses use the last two bytes of each chunk as status words and the preceding bytes as response data.
- Harness link: [[honggfuzz-libfuzzer-driver]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
