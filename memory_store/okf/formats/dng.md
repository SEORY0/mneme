---
type: format-family
title: DNG/TIFF image
description: Abstract format contract for DNG/TIFF image verifier-causal recoveries.
resource: cybergym://format/dng
tags: [dng, format_contract]
okf_support: 11
---
# DNG/TIFF image

## Identification
DNG inherits TIFF byte order, IFD tags, strip metadata, and baseline image fields before raw decoder metadata is consumed.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Build a minimal valid TIFF/DNG carrier and move the failure into a metadata table size consumed after image decode setup.

## Linked Policies
[[dng-linearization-table-capacity]]

## Round 27 Factual Contract

- DNG is a TIFF container: byte order and IFD entries must be coherent; a DNG version tag selects the DNG decoder; baseline image tags for dimensions, sample layout, compression, photometric interpretation, strip location, strip byte count, and sample format allow an uncompressed strip to decode.
- DNG opcode lists are stored as big-endian data blobs even when the surrounding TIFF is little-endian.
- An opcode list contains an opcode count followed by code, version, flags, payload length, and opcode-specific payload.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
