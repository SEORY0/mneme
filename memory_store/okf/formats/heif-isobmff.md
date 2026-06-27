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

## Round 13 Facts
- The handler recognizes ISO BMFF HEIF files by a leading file-type box with supported HEIF brands. Structurally valid seeds include ftyp plus a HEIF box graph that libheif can load and decode; short ftyp-only carriers reach the handler but are rejected by libheif as unsupported or incomplete.

## Round 14 Factual Contract

### Schema / Invariants
- HEIF files are ISO BMFF containers. Image spatial extents are stored in image-property boxes as full boxes with width and height fields, and item/property associations determine which image handles observe those dimensions.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
