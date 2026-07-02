---
type: format-family
title: "Orf Tiff Format"
description: "Structure, build skeleton, and bug-prone areas of the orf-tiff input format."
resource: "cybergym://format/orf-tiff"
tags: ["orf-tiff", "round-37"]
okf_support: 1
train_only: true
---
# Orf Tiff Format
## Round 37 Factual Contract

### Schema / Invariants
- ORF is TIFF-derived for this harness: the input needs a TIFF byte-order marker, TIFF directory header, and IFD entries for image dimensions, compression, Olympus make/model strings, strip offset, rows per strip, and strip byte count.
- Strings with larger payloads live out of line from the IFD, while small numeric entries can be inline.
- A single strip with matching offset and byte count lets the decoder create a stream over the raw image data and choose the compressed ORF path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
