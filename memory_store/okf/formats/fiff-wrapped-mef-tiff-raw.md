---
type: format-family
title: "FIFF Wrapped Mef TIFF RAW Format"
description: "Round 26 descriptive structure and invariant facts for fiff-wrapped-mef-tiff-raw."
tags: ["fiff-wrapped-mef-tiff-raw", "round-26"]
okf_support: 1
train_only: true
---
# FIFF Wrapped Mef TIFF RAW Format

## Round 26 Factual Contract

### Schema / Invariants
- The FIFF parser reads fixed big-endian header pointers and treats the first pointer as an embedded TIFF root after applying its internal base adjustment. TIFF string tags can select the decoder by camera make/model. The MEF path uses the root TIFF image-width, image-length, strip-offset, and strip-byte-count tags, then decodes the strip as big-endian packed 12-bit raw samples. Strip offsets used by the decoder are relative to the whole input file, while TIFF metadata offsets inside the embedded root are relative to that TIFF view.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
