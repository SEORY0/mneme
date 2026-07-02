---
type: harness-contract
title: "libfuzzer-bfd-archive harness"
description: "Descriptive harness contract facts for libfuzzer-bfd-archive."
tags: ["libfuzzer-bfd-archive", "round-18"]
okf_support: 9
train_only: true
---
# Libfuzzer BFD Archive Harness

## Round 18 Input Contract

### Schema / Invariants
- The libFuzzer harness writes the raw input bytes to a temporary file and opens it with BFD. There is no fuzzer-side length prefix or field carving; all structure must be present in the raw archive bytes.

### Format Links
- [[alpha-ecoff-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 27 Input Contract
- libFuzzer bytes are written unchanged to a temporary file and opened with BFD using automatic target detection.
- The harness calls the archive format checker directly; there is no FuzzedDataProvider carving, mode byte, checksum wrapper, or file-name-controlled format selection.

## Round 27 Format Links
- [[ecoff-ar-archive]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 35 Input Contract

### Input Contract
- The libFuzzer harness writes the raw input bytes unchanged to a temporary file, opens that file with BFD automatic target detection, and calls the archive format checker. There is no mode byte, FuzzedDataProvider split, checksum wrapper, or filename-controlled target selection.

### Format Links
- [[alpha-ecoff-archive]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
