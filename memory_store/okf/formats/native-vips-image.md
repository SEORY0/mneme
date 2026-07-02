---
type: format-family
title: "native-vips-image format"
description: "Structure, build skeleton, and bug-prone areas of the native-vips-image input format."
resource: cybergym://format/native-vips-image
tags: ["native-vips-image", "round-29"]
okf_support: 0
---
# Native Vips Image Format

## Round 29 Factual Contract

### Schema / Invariants
- Native VIPS files begin with a fixed binary header containing image dimensions, band count, band format, coding, interpretation, resolution, and origin fields, followed directly by raw pixel samples. The header can encode a CMC interpretation directly, which is useful when ordinary image carriers would lose or normalize color-space metadata. Small dimensions and a normal uncoded numeric pixel format keep the loader and saver on the intended color-conversion path.

### Harness Links
- [[libfuzzer-jpegsave-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- Native VIPS files use an endian-marked fixed header containing image geometry, band count, band format, coding, interpretation, resolution metadata, and image data after the header.
- The jpegsave path accepts tiny native images and can route color-managed interpretations through conversion before JPEG encoding; TIFF and JPEG corpus seeds are also accepted by the same libvips file-loader surface.

### Harness Links
- [[libfuzzer-jpegsave-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
