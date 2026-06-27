---
type: harness-contract
title: "Libfuzzer Ghostscript Pdfwrite Device harness"
description: "Input contract facts for libfuzzer ghostscript pdfwrite device."
tags: ["libfuzzer-ghostscript-pdfwrite-device", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Ghostscript Pdfwrite Device Harness

## Round 17 Input Contract
- The fuzzer passes raw stdin-like document bytes to Ghostscript configured with a pdfwrite-style device wrapper.
- There is no envelope, but raw font files alone are not accepted as page-description input.

## Round 17 Format Links
- [[postscript-pdf-truetype]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[postscript-pdf-truetype]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
