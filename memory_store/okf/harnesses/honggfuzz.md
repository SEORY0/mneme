---
type: harness-contract
title: "Honggfuzz harness"
description: "Input contract facts for honggfuzz."
tags: ["honggfuzz", "round-15"]
okf_support: 1
---
# Honggfuzz Harness

## Round 15 Input Contract
- The honggfuzz target copies the leading option block into a struct, decodes the rest as an image,
  rotates a second copy, calls vips_mosaic with the carved coordinates, and then forces evaluation
  with a max operation. There is no external file requirement.

## Format Links
- [[libvips-image-with-mosaic-options]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
