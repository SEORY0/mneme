---
type: format-family
title: "PNG Format"
description: "Round 27 descriptive format facts for png."
resource: cybergym://format/png
tags: ["png", "round-27"]
okf_support: 1
---
# PNG Format

## Round 27 Factual Contract

- PNG is a chunk stream with a fixed signature, an image header chunk before image data, and zlib-wrapped DEFLATE bytes in image-data chunks.
- Chunk framing is big-endian length, type, data, and checksum; the decoder reaches the DEFLATE path when the image header is coherent and image dimensions remain within the harness limit.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
