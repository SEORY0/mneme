---
type: format-family
title: "Libvips Thumbnail Image Buffer Format"
description: "Round 27 descriptive format facts for libvips-thumbnail-image-buffer."
resource: cybergym://format/libvips-thumbnail-image-buffer
tags: ["libvips-thumbnail-image-buffer", "round-27"]
okf_support: 1
---
# Libvips Thumbnail Image Buffer Format

## Round 27 Factual Contract

- The active libvips input is a raw image file buffer, not a command-line archive operation.
- The fuzzer calls image loading from memory, rejects images above small dimension and band-count limits, thumbnails the accepted image, computes an average over the output, and releases the images.
- In-repo corpus and test-suite seeds include TIFF, GIF, BMP, WebP, PNG, JPEG, and HEIF-like image carriers; structurally valid seeds can reach the loader and thumbnail path without a sanitizer signal.

### Harness Links
- [[honggfuzz-libfuzzer-standalone]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
