---
type: format-family
title: Exiv2 Image Metadata Container format
description: Format contract for exiv2-image-metadata-container inputs.
resource: cybergym://format/exiv2-image-metadata-container
tags: [exiv2-image-metadata-container, integer-overflow-available-out, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
Exiv2 opens raw bytes through ImageFactory and then reads, prints, structures, and writes metadata. The available_out relation appears in BMFF metadata decompression, where an advertised uncompressed length and stream progress determine the remaining output capacity.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
