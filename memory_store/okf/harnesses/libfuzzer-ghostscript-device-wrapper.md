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
