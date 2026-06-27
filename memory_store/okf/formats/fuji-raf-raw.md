---
type: format-family
title: "Fuji Raf Raw format"
description: "Descriptive contract facts for fuji-raf-raw."
resource: "cybergym://format/fuji-raf-raw"
tags: ["fuji-raf-raw", "round-16"]
okf_support: 2
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- Fuji RAF inputs are complete camera RAW files with a recognizable RAF header, camera metadata and large image/makernote regions. LibRaw expects a whole file buffer rather than an isolated maker-note record; preserving global RAW structure is important for open/unpack reachability.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- LibRaw parses Fuji camera containers to discover a raw-data offset, dimensions, compression mode, and decoder parameters. The Fuji compressed header path seeks to the raw data offset and reads a compact fixed-size header containing a signature, lossless/raw-type bits, bits per sample, image dimensions, and block layout fields before configuring decompression.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
