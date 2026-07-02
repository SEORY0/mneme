---
type: harness-contract
title: "Libfuzzer BFD Tempfile Harness"
description: "Input contract facts for libfuzzer-bfd-tempfile."
tags: ["libfuzzer-bfd-tempfile", "round-27"]
okf_support: 1
---
# Libfuzzer BFD Tempfile Harness

## Round 27 Input Contract
- libFuzzer supplies raw bytes.
- The harness writes them unchanged to a temporary file, opens that file through BFD auto-detection, and asks BFD to check archive format.
- There is no selector byte and no FuzzedDataProvider carving.

## Round 27 Format Links
- [[vms-ia64-library-archive]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 36 Input Contract
- The BFD libFuzzer harness writes the submitted bytes unchanged to a temporary file, opens it with BFD automatic target selection, and calls the archive-format checker. There is no leading mode byte, length prefix, integrity wrapper, or FuzzedDataProvider front/back split.

## Round 36 Format Links
- [[vms-ia64-library-archive]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.

## Round 38 Factual Contract

### Input Contract
- The libFuzzer BFD harness writes the raw PoC bytes unchanged to a temporary file, opens it with BFD automatic target selection, and calls archive-format checking. There is no selector byte, no filename extension dependence, no checksum layer, and no FuzzedDataProvider front/back split. The input must be a complete enough archive file for BFD to select the VMS IA-64 library backend.

### Format Links
- [[vms-ia64-library-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
