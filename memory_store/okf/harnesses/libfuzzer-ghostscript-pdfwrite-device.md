---
type: harness-contract
title: "Libfuzzer Ghostscript Pdfwrite Device harness"
description: "Input contract facts for libfuzzer ghostscript pdfwrite device."
tags: ["libfuzzer-ghostscript-pdfwrite-device", "round-17"]
okf_support: 2
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

## Round 18 Input Contract

### Schema / Invariants
- The pdfwrite device fuzzer passes raw document bytes into Ghostscript with pdfwrite as the output device. There is no mode selector or checksum gate; reachability depends on constructing a valid document with an embedded font program.

### Format Links
- [[postscript-or-pdf-with-type2-charstring-font]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
