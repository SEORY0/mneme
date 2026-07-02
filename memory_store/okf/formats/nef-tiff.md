---
type: format-family
title: nef-tiff format
description: "Round 23 descriptive structure and invariant facts for nef-tiff."
resource: cybergym://format/nef-tiff
tags: ["nef-tiff", "round-23"]
okf_support: 12
train_only: true
---
# Nef Tiff Format

## Round 23 Factual Contract

### Schema / Invariants
- NEF rides on TIFF-style endian magic, an image-file directory, typed tag entries, out-of-line values for strings or arrays, and strip offset/byte-count metadata. RawSpeed uses the compression tag, dimensions, bits per sample, CFA metadata, and maker metadata to choose the Nikon compressed raw decoder.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 24 Factual Contract

### Schema / Invariants
- A NEF file is TIFF-like: byte order and TIFF magic lead to an IFD table. The Nikon decoder is selected from Make/Model metadata. The compressed path requires a CFA-bearing IFD with compression set to Nikon compressed raw, one strip offset/count pair, image width and height, bits per sample, and Nikon metadata entries used by the decompressor.

### Harness Links
- [[libfuzzer-rawspeed-tiffdecoderfuzzer-nefdecoder]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- RawSpeed reaches the NEF decoder through standard TIFF header and IFD parsing.
- The sNEF path depends on make/model identity, image dimensions, bit depth, compression, CFA-pattern presence, strip offset/count metadata, and white-balance rationals.
- The strip byte count is used to classify the expected image payload independently of the actual remaining bytes in the file.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
