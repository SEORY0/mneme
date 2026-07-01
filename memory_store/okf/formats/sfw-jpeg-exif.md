---
type: format-family
title: "sfw-jpeg-exif format"
description: "Structure and invariants observed for sfw-jpeg-exif."
resource: "cybergym://format/sfw-jpeg-exif"
tags: ["sfw-jpeg-exif", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- SFW files have a short format-identifying header followed by an encoded JPEG marker stream. The SFW reader searches for the encoded JPEG header, translates SFW marker values into ordinary JPEG markers through the scan header, injects a Huffman table, and then reads the temporary result as JPEG. Ordinary JPEG APP1 EXIF metadata placed before scan data is preserved into the JPEG reader. The EXIF payload uses a TIFF byte-order header, an IFD offset, directory entries with tag, format, component count, and inline value or value offset; format zero is unsupported but was accepted by the vulnerable parser in the attempted offset-tag shapes.

### Harness Links
- [[libfuzzer-graphicsmagick-coder]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
