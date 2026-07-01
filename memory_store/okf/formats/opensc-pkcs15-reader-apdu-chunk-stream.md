---
type: format-family
title: "Opensc Pkcs15 Reader Apdu Chunk Stream"
description: "Round 36 factual format contract for opensc-pkcs15-reader-apdu-chunk-stream."
tags: ["opensc-pkcs15-reader-apdu-chunk-stream", "round-36", "format-contract"]
okf_support: 1
train_only: true
---
# Opensc Pkcs15 Reader Apdu Chunk Stream

## Round 36 Factual Contract

### Schema / Invariants
- The harness input is an OpenSC fuzz reader transcript, not a standalone card file. It is a sequence of native little-endian length-prefixed chunks. The first chunk becomes the card ATR. Later chunks model APDU responses: the final two bytes are status words and any preceding body is copied into the APDU response buffer when the caller requested response data. Oberthur transparent files are selected through FCI/FCP-style TLVs that describe DF versus transparent EF type, file identity, size, and ACL bytes; file content is returned by a separate read response. Oberthur container metadata is parsed as records beginning with a record marker and record length, followed by multiple object identifiers and a UUID-like field.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- The OpenSC PKCS#15 reader fuzz input is a stream of native little-endian length-prefixed chunks.
- The first chunk is copied as the ATR.
- Each later APDU response chunk places its status word in the final two bytes and any preceding body is copied into the APDU response buffer when the caller expects data.
- TCOS synthetic binding needs ISO7816-style FCI responses for selected files, an ICCSN-bearing serial file read, and TCOS password/key metadata records shaped as record bodies with a record tag, declared length, and embedded short TLVs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
