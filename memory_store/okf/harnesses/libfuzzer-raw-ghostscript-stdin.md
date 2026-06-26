---
type: harness-contract
title: "Libfuzzer Raw Ghostscript Stdin Harness"
description: "Round 7 input contract facts for libfuzzer-raw-ghostscript-stdin."
tags: ["libfuzzer-raw-ghostscript-stdin", "harness-contract", "round-7"]
okf_support: 2
train_only: true
---
# Libfuzzer Raw Ghostscript Stdin Harness

## Round 7 Input Contract
- The fuzzer provides raw bytes through Ghostscript stdin to a cups raster-oriented invocation with
memory-related command-line limits. There is no FuzzedDataProvider layout; the bytes are interpreted
as whatever Ghostscript language the front end detects.
- Ghostscript reads raw stdin through the gstoraster-style fuzzer invocation. The harness does not
carve fields; parser selection is based on the document syntax supplied in the input bytes.

## Round {ROUND} Format Links
- [[pdf-or-postscript]]
- [[postscript-or-pdf]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
