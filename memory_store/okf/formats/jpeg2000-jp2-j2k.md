---
type: format-family
title: "Jpeg2000 Jp2 J2k format"
description: "Descriptive contract facts for jpeg2000-jp2-j2k."
resource: "cybergym://format/jpeg2000-jp2-j2k"
tags: ["jpeg2000-jp2-j2k", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The wrapper accepts raw JPEG 2000 codestreams and JP2 containers. J2K codestreams are selected by their codestream marker prefix, while JP2 files are selected by their signature box layout. Tile, progression-order-change, coding-style, and packet header marker segments control the iterator state that later packet decoding consumes.

### Harness Links
- [[afl-file-openjpeg-decompress]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
