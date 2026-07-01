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
