---
type: harness-contract
title: "Libfuzzer Ghostscript Device Wrapper harness"
description: "Input contract facts for libfuzzer-ghostscript-device-wrapper."
tags: ["libfuzzer-ghostscript-device-wrapper"]
okf_support: 0
---
# Libfuzzer Ghostscript Device Wrapper Harness

## Round 10 Input Contract
- The harness calls a Ghostscript device fuzzer with the pdfwrite device selected. Raw bytes become interpreter input; no front carving or FuzzedDataProvider layout is used.

## Round 10 Format Links
- [[postscript-pdf-for-ghostscript-pdfwrite]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 14 Input Contract
- The Ghostscript fuzzer consumes raw PDF bytes and invokes a device wrapper selected by the packaged target. It is tolerant of repairable PDFs, so parser reach requires a coherent document graph rather than a standalone object stream.

## Round 14 Format Links
- [[pdf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
