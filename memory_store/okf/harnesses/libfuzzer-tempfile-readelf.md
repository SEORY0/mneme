---
type: harness-contract
title: "Libfuzzer Tempfile Readelf harness"
description: "Input contract facts for libfuzzer-tempfile-readelf."
tags: ["libfuzzer-tempfile-readelf", "round-15"]
okf_support: 2
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

## Round 18 Input Contract

### Schema / Invariants
- The libFuzzer input is written verbatim to a temporary file and processed by readelf with archive, section, symbol, relocation, dynamic, note, and unwind processing enabled. There is no mode byte and no FuzzedDataProvider layout.

### Format Links
- [[thin-ar-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
