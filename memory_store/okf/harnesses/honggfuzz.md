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

## Round 17 Input Contract
- The generated OpenSC target runs the PKCS#15 reader fuzzer on raw file bytes.
- The harness is not a FuzzedDataProvider layout; the bytes are parsed as an encoded card/PKCS#15 object stream by the reader.

## Round 17 Format Links
- [[opensc-pkcs15-asn1]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[opensc-pkcs15-asn1]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 36 Input Contract
- The fuzzer installs a virtual reader over the raw chunk stream, connects a card from the first ATR, binds PKCS#15, then consumes more chunks for operation inputs and APDU responses. The local binary is honggfuzz-style and direct verify prints usage text, so official submit was used for the scoring result.

## Round 36 Format Links
- [[opensc-pkcs15-reader-chunk-stream]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
