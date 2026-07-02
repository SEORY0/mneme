---
type: format-family
title: "tiff-webp-ptif format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/tiff-webp-ptif"
tags: ["tiff-webp-ptif", "round-35"]
okf_support: 1
train_only: true
---
# tiff-webp-ptif Format

## Round 35 Factual Contract
### Schema / Invariants
- Classic TIFF is sufficient. The useful shape is a normal TIFF directory with width, height, samples-per-pixel, rows-per-strip, strip offset/count arrays, and the Compression tag set to WebP. The strip payloads must be genuine WebP-compressed image data, not uncompressed TIFF strips with only the compression tag changed. Mutating bit-depth metadata without matching the WebP decoder's expectations can make libtiff reject the image before the writer.

### Harness Links
- [[libfuzzer-graphicsmagick-coder-write]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
