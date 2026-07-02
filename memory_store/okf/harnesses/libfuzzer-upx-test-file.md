---
type: harness-contract
title: "Libfuzzer Upx Test File harness"
description: "Input contract facts for libfuzzer-upx-test-file."
tags: ["libfuzzer-upx-test-file", "round-15"]
okf_support: 1
---
# Libfuzzer Upx Test File Harness

## Round 15 Input Contract
- The harness writes raw input bytes to a temporary file and invokes UPX in test mode on that file.
  The input is not length-prefixed and has no argv selector or FuzzedDataProvider layout, but it must
  pass UPX's packed-file recognition before the Linux ELF unpacker dynamic-table code is reached.

## Format Links
- [[upx-packed-elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 26 Factual Contract


### Input Contract
- The libFuzzer target writes the raw input bytes to a temporary file and invokes UPX test mode on that file through the normal command path. There is no fuzzer-side prefix, selector, length trailer, or FuzzedDataProvider layout; parser reachability requires a complete packed executable recognized by UPX.

### Format Links
- [[upx-packed-elf]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 28 Input Contract

- The libFuzzer harness writes the input bytes verbatim to a temporary file and invokes UPX test mode on that path. There is no mode byte, FuzzedDataProvider split, checksum wrapper, or length prefix outside the file itself; the bytes must be a complete UPX-packed file that passes packed-file recognition before unpack-time ELF logic is reached.

## Round 28 Format Links
- [[upx-packed-elf]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
