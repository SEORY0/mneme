---
type: harness-contract
title: "libfuzzer-gstoraster-stdin harness"
description: "Descriptive harness contract facts for libfuzzer-gstoraster-stdin."
tags: ["libfuzzer-gstoraster-stdin", "round-18"]
okf_support: 2
train_only: true
---
# Libfuzzer Gstoraster Stdin Harness

## Round 18 Input Contract

### Schema / Invariants
- The gstoraster fuzzer passes the raw input to Ghostscript as stdin with raster-device arguments. The document must be accepted far enough for the embedded font to be interpreted; there is no selector byte or FuzzedDataProvider carving.

### Format Links
- [[postscript-type1-font-carrier]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 24 Factual Contract

### Input Contract
- The gstoraster fuzzer runs Ghostscript with raster-device arguments and feeds the candidate as PostScript input. There is no custom byte carving before the interpreter sees the program.

### Format Links
- [[postscript]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 26 Factual Contract


### Input Contract
- The gstoraster fuzzer passes raw stdin bytes to Ghostscript with CUPS raster-device arguments. There is no fuzzer-side prefix, sidecar file, archive mode selector, checksum field, or FuzzedDataProvider layout. Ghostscript chooses the document parser from the input syntax; XPS package samples were not accepted by this target, while a renderable PDF drove the PDF font-loading path.

### Format Links
- [[pdf-opentype-cff-font]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 29 Input Contract

- The gstoraster libFuzzer target feeds the entire PoC as Ghostscript stdin with fixed CUPS raster output arguments. There is no mode byte, archive wrapper, or FuzzedDataProvider layout; the harness continues into exit/delete cleanup after init returns an error.

## Round 29 Format Links
- [[postscript]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
