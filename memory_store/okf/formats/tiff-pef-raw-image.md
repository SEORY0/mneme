---
type: format-family
title: "Tiff Pef Raw Image format"
description: "Descriptive contract facts for tiff/pef raw image."
resource: "cybergym://format/tiff-pef-raw-image"
tags: ["tiff-pef-raw-image", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The RawSpeed TIFF parser expects a TIFF header, an IFD table, and tags for dimensions, strip offsets, strip byte counts, rows per strip, samples per pixel, compression, and bits per sample. The uncompressed decoder derives input pitch and white point from these fields.

### Harness Links
- [[libfuzzer-rawspeed-pef-decoder]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- The PEF path consumes a raw TIFF byte stream: endian marker, TIFF magic, IFD entries, and strip payload bytes. Relevant reachability tags include image dimensions, BitsPerSample, Compression selecting uncompressed decode, Make/Model identification accepted by the PEF wrapper, StripOffsets, StripByteCounts, RowsPerStrip, and SamplesPerPixel. Multi-value strip tables are stored out-of-line when they do not fit in the TIFF value slot. For this decoder, the uncompressed path derives decoded slice height from ImageLength and RowsPerStrip, validates strip byte ranges against the whole file buffer, allocates the RawImage after accumulating strip row counts, and then checks initialized output rows after decode.

### Harness Links
- [[libfuzzer-rawspeed-pef-decoder]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
