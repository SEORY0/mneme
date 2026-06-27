---
type: format-family
title: "Opensc Virtual Reader Chunk Stream Iasecc Tlv format"
description: "Descriptive contract facts for opensc-virtual-reader-chunk-stream-iasecc-tlv."
resource: "cybergym://format/opensc-virtual-reader-chunk-stream-iasecc-tlv"
tags: ["opensc-virtual-reader-chunk-stream-iasecc-tlv", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- IASECC response data uses ASN.1/TLV-like records inside the OpenSC virtual reader transcript.
- Extended tags and lengths can influence object parsing only after the card driver accepts the card identity, application selection, and successful APDU status flow.

### Harness Links
- [[opensc-card-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
