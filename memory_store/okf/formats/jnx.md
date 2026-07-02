---
type: format-family
title: "JNX format"
description: "Descriptive contract facts for jnx."
resource: "cybergym://format/jnx"
tags: ["jnx", "round-16"]
okf_support: 2
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- JNX is a little-endian tiled raster container with a fixed header, a bounded level table, per-level tile records, and tile payloads addressed by size and file position. Version-three level records are compact fixed-size records; tile records carry bounds, dimensions, payload size, and payload position. The reader prepends a JPEG start marker before handing each tile blob to the generic image loader.

### Harness Links
- [[libfuzzer-graphicsmagick-coder]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- JNX uses a little-endian container header, a level table, and per-level tile records containing geographic bounds, dimensions, payload length, and payload pointer. JNX tile payloads omit the leading JPEG marker because the reader injects it before passing the tile blob onward. GraphicsMagick DICOM detection uses a preamble marker, and DICOM elements can use explicit VR headers with short lengths for character fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
