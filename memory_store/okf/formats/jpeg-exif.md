---
type: format-family
title: "Jpeg Exif"
description: "Round 7 factual format contract for jpeg-exif."
resource: cybergym://format/jpeg-exif
tags: ["jpeg-exif", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Jpeg Exif

## Round 7 Factual Contract

### Schema / Invariants
- The input is a JPEG/TIFF-style Exif payload containing APP metadata, TIFF byte order/header fields,
IFD entries, and optional maker-note subformats for camera vendors. Maker-note parsing walks vendor-
specific entry tables after Exif data is recognized.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 11 Factual Contract

### Schema / Invariants
- The loader accepts raw image bytes and recognizes JPEG APP1 Exif data as well as Exif/TIFF-style payloads. Exif data contains a TIFF header, image file directories, typed entries with counts, and value areas; maker-note payloads are nested vendor-specific data reachable from Exif entries.

### Harness Links
- [[libfuzzer-libexif-loader]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- libexif accepts either raw EXIF payloads or JPEG APP1 EXIF envelopes. Maker-note interpretation depends on a MakerNote tag with vendor-identifying data; the Apple path has value-formatting cases that require at least a short length before subtracting from it.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
