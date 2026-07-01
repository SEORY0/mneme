---
type: format-family
title: "Heif Isobmff format"
description: "Descriptive contract facts for Heif Isobmff."
resource: "cybergym://format/heif-isobmff"
tags: ["heif-isobmff", "round-6"]
okf_support: 2
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

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- HEIF files are ISO BMFF box graphs beginning with a file-type brand box. Image dimensions are stored in image spatial extent properties and associated to image items through property-association boxes; mutating dimensions while preserving the rest of the box graph can keep the parser gate satisfied.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- HEIF is an ISO BMFF box graph with file type, metadata, item-info, item-location, item-reference, and item-property boxes. Image items get dimensions from image-spatial-extent properties, item-property associations select hvcC/ispe/auxC properties, and auxl references attach auxiliary alpha images to a master image. Derived image item types can use item data as a small descriptor rather than coded HEVC picture data.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.

## Round 36 Factual Contract

### Schema / Invariants
- HEIF uses an ISO-BMFF-style box tree with a file type box, metadata describing image items and properties, item-location and item-info tables, item references for auxiliary alpha linkage, and media-data payload. For alpha-plane paths, the parser needs a complete image item plus a valid auxiliary-alpha relationship rather than a standalone color-conversion buffer.

### Harness Links
- [[afl-libfuzzer-file-fuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
