---
type: format-family
title: "PNG Format"
description: "Round 27 descriptive format facts for png."
resource: cybergym://format/png
tags: ["png", "round-27"]
okf_support: 2
---
# PNG Format

## Round 27 Factual Contract

- PNG is a chunk stream with a fixed signature, an image header chunk before image data, and zlib-wrapped DEFLATE bytes in image-data chunks.
- Chunk framing is big-endian length, type, data, and checksum; the decoder reaches the DEFLATE path when the image header is coherent and image dimensions remain within the harness limit.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 33 Factual Contract

### Schema / Invariants
- PNG files start with a fixed signature and are a sequence of length, type, data, and CRC chunks. IHDR must appear first, IDAT carries compressed image data, and IEND terminates the file. eXIf is an ancillary chunk whose payload should contain at least an EXIF/TIFF byte-order header. CRCs are checked by this harness, so any mutation that changes chunk type or data must recompute the chunk CRC. Placing an ancillary chunk after IDAT exercises a different validation path than placing the same chunk before IDAT.

### Harness Links
- [[libfuzzer-spng-read]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
