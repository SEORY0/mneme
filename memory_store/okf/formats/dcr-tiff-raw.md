---
type: format-family
title: "Dcr Tiff Raw format"
description: "Descriptive contract facts for Dcr Tiff Raw."
resource: "cybergym://format/dcr-tiff-raw"
tags: ["dcr-tiff-raw", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- DCR inputs follow TIFF-like byte-order, magic, IFD offset, directory-entry, and tag/value conventions. Decoder-specific reachability depends on both the container tags and enough raw-image metadata to enter DcrDecoder raw decoding.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
