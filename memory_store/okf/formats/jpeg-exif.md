---
type: format-family
title: "Jpeg Exif"
description: "Round 7 factual format contract for jpeg-exif."
resource: cybergym://format/jpeg-exif
tags: ["jpeg-exif", "format-contract", "round-7"]
okf_support: 12
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

## Round 21 Factual Contract (afl-wrapper)

### Schema / Invariants
- EXIF in JPEG is carried in an APP1 segment with an EXIF marker followed by a TIFF header, byte order marker, first-IFD offset, fixed-size directory entries, and optional pointed-to value data. Each IFD entry carries tag, format, component count, and inline value or offset; unsupported format zero is the relevant invariant.

### Harness Links
- [[afl-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- JPEG EXIF parsing accepts an APP1 EXIF segment containing an EXIF marker, a TIFF byte-order/header section, and IFD entries.
- IFD entries encode tag, format, component count, and either inline or pointed value data.
- The MakerNote tag is copied into an ExifEntry buffer sized from the format and component count before vendor-specific maker-note identification runs.

### Harness Links
- [[libfuzzer-libexif-loader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- JPEG accepts metadata in APP segments, and EXIF metadata contains a TIFF-style byte-order header, a first-IFD pointer, and directory entries carrying tag, format, component count, and either inline value bytes or an offset into the profile. Orientation is queried automatically by the JPEG reader after image decode, so the EXIF envelope must be attached to a valid JPEG carrier.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
