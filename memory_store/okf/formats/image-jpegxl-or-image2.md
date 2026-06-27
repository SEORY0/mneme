---
type: format-family
title: image-jpegxl-or-image2 format
description: Structure and reachability facts for image-jpegxl-or-image2 inputs.
tags: [image-jpegxl-or-image2]
okf_support: 0
---
# Image Jpegxl Or Image2 Format

## Round 10 Factual Contract

### Schema / Invariants
- JPEG XL samples begin as valid still or animated image codestream/container data. The selected image2 demuxer can also be influenced by the generic demux fuzzer metadata trailer that controls buffering, seekability, virtual filesize, and filename/extension hints.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
