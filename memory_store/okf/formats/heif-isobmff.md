---
type: format-family
title: "Heif Isobmff format"
description: "Descriptive contract facts for Heif Isobmff."
resource: "cybergym://format/heif-isobmff"
tags: ["heif-isobmff", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- HEIF inputs are ISO BMFF box trees beginning with a brand box, then metadata boxes that describe image items, locations, properties, and auxiliary alpha relationships. Reaching alpha-plane copying requires consistent item locations/properties, not just alpha-related box names.

### Harness Links
- [[afl-libfuzzer-libheif-file-fuzzer-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
