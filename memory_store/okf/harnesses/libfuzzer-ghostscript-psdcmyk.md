---
type: harness-contract
title: "Libfuzzer Ghostscript Psdcmyk Harness"
description: "Round 26 input contract facts for libfuzzer-ghostscript-psdcmyk."
tags: ["libfuzzer-ghostscript-psdcmyk", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Psdcmyk Harness

## Round 26 Factual Contract

### Input Contract
- The selected oss-fuzz target is gs_device_psdcmyk_fuzzer. It feeds the raw input as Ghostscript stdin to the psdcmyk device with banding-oriented device options and writes output to a null file path. There is no fuzzer-side prefix, selector byte, or FuzzedDataProvider layout; parser selection is determined by PDF or PostScript syntax in the raw bytes.

### Format Links
- [[pdf-or-postscript]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
