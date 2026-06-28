---
type: format-family
title: libvips-image-with-mosaic-options format
description: Format contract for libvips-image-with-mosaic-options.
resource: cybergym://format/libvips-image-with-mosaic-options
tags: [libvips-image-with-mosaic-options]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `libvips-image-with-mosaic-options` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The fuzzer input is a packed mosaic option block followed by a complete image file that libvips can
  load from memory. The option block supplies a direction flag and four small reference coordinates;
  the remaining bytes must be a decodable image with constrained dimensions and band count.

### Harness Links
- [[honggfuzz]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
