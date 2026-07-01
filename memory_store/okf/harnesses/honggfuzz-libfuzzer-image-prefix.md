---
type: harness-contract
title: "honggfuzz-libfuzzer-image-prefix harness"
description: "Input contract facts for honggfuzz-libfuzzer-image-prefix."
tags: ["honggfuzz-libfuzzer-image-prefix", "round-35"]
okf_support: 1
train_only: true
---
# honggfuzz-libfuzzer-image-prefix Harness

## Round 35 Input Contract
### Input Contract
- The active pix_rotate_shear fuzzer consumes three leading little-endian signed control fields for rotation parameters, then treats the remaining bytes as an image buffer. It rejects very short image payloads and PNM inputs, detects the image format from the remaining raw bytes, and calls pixReadMem, which dispatches TIFF inputs into pixReadMemTiff and pixReadFromTiffStream. There is no checksum or FuzzedDataProvider layout.

### Format Links
- [[tiff]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
