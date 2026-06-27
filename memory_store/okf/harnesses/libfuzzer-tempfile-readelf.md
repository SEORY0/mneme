---
type: harness-contract
title: "Libfuzzer Tempfile Readelf harness"
description: "Input contract facts for libfuzzer-tempfile-readelf."
tags: ["libfuzzer-tempfile-readelf", "round-15"]
okf_support: 1
---
# Libfuzzer Tempfile Readelf Harness

## Round 15 Input Contract
- The libFuzzer input is written to a temporary file and processed by the readelf fuzzer with header,
  section, relocation, and unwind processing enabled. There is no mode selector and no
  FuzzedDataProvider layout.

## Format Links
- [[elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
