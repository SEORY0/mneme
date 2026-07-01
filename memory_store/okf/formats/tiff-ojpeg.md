---
type: format-family
title: "Tiff Ojpeg format"
description: "Descriptive contract facts for tiff-ojpeg."
resource: "cybergym://format/tiff-ojpeg"
tags: ["tiff-ojpeg", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- TIFF inputs need a byte-order marker, directory entries, image dimensions, bit depth, compression mode, strip/tile metadata, and offsets that point to embedded image data. Old-JPEG TIFFs add legacy JPEG-related tags whose offsets and lengths must agree with the directory for libtiff to decode rather than reject.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 35 Factual Contract

### Schema / Invariants
- Classic TIFF uses an endian marker, image-directory records, and out-of-line values for larger tag payloads. The old JPEG-in-TIFF path needs coherent image dimensions, sample layout, strip information, photometric interpretation, and legacy JPEG interchange metadata that points to an embedded JPEG stream. A carrier that only flips the compression mode without matching the legacy JPEG metadata does not reach the target path.
- Classic TIFF uses a byte-order header, an image-file-directory table, and typed tag records. Parser reachability depended on keeping image dimensions, bit depth, samples per pixel, rows per strip, strip offsets, strip byte counts, planar configuration, photometric interpretation, and JPEG payload metadata coherent. Old-JPEG TIFFs use legacy JPEG interchange metadata instead of the newer JPEG tables tag; changing only the compression field can create an off-target decoder crash.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
