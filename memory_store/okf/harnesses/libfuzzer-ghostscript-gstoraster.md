---
type: harness-contract
title: "libfuzzer-ghostscript-gstoraster harness"
description: "Descriptive harness contract facts for libfuzzer-ghostscript-gstoraster."
tags: ["libfuzzer-ghostscript-gstoraster", "round-18"]
okf_support: 3
train_only: true
---
# Libfuzzer Ghostscript Gstoraster Harness

## Round 18 Input Contract

### Schema / Invariants
- The gstoraster harness feeds the raw input as Ghostscript standard input using the cups raster device and fixed device options. There is no fuzzer envelope; the document bytes themselves must select the PostScript features and rendering state.
- The Ghostscript raster harness consumes raw PostScript/PDF bytes from standard input under fixed raster-device arguments. Some Ghostscript fuzzers carve an initial color-scheme byte, but this run's observed target executes through the raw gstoraster path.

### Format Links
- [[postscript-raster-document]]
- [[postscript-sampled-function]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 20 Input Contract
- The gstoraster fuzzer feeds raw input as interpreter stdin with CUPS raster style device arguments. There is no separate filename or container wrapper supplied by the harness, so inputs must either be directly interpretable or use PostScript operators available from stdin.
- The Ghostscript gstoraster harness runs the supplied bytes as a single document. The bytes are raw PDF/PostScript input to the interpreter; there is no fuzzer-side prefix or field carving.

## Round 20 Format Links
- [[pdf]]
- [[postscript-or-pdf-interpreter-input]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 24 Factual Contract

### Input Contract
- The gstoraster fuzz target feeds the raw input bytes to Ghostscript as a document stream with no fuzzer prefix or carving.

### Format Links
- [[pdf]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
