---
type: harness-contract
title: "Libfuzzer Rawspeed Pef Decoder harness"
description: "Input contract facts for libfuzzer RawSpeed PEF decoder."
tags: ["libfuzzer-rawspeed-pef-decoder", "round-16"]
okf_support: 1
---
# Libfuzzer Rawspeed Pef Decoder Harness

## Round 16 Input Contract
- The selected wrapper runs the PEF TIFF decoder fuzzer directly on raw bytes. It parses the TIFF structure, constructs a PEF decoder, disables crop and unknown-failure strictness, then calls raw decode and metadata decode inside exception handling.

## Round 16 Format Links
- [[tiff-pef-raw-image]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 38 Factual Contract

### Input Contract
- The fuzz target passes the entire input file as raw bytes into RawSpeed's TIFF parser, calls the PEF decoder appropriateness check, constructs the PEF decoder, disables crop and strict unknown-camera failure, then calls decodeRaw and decodeMetaData inside a RawspeedException catch. There is no FuzzedDataProvider layout, selector byte, checksum gate, or carved prefix.

### Format Links
- [[tiff-pef-raw-image]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
