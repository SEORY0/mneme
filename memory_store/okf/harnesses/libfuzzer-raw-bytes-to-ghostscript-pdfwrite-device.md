---
type: harness-contract
title: "Libfuzzer Raw Bytes To Ghostscript Pdfwrite Device harness"
description: "Input contract facts for libfuzzer-raw-bytes-to-ghostscript-pdfwrite-device."
tags: ["libfuzzer-raw-bytes-to-ghostscript-pdfwrite-device", "round-24"]
okf_support: 1
---
# Libfuzzer Raw Bytes To Ghostscript Pdfwrite Device Harness

## Round 24 Factual Contract

### Input Contract
- Raw input bytes are passed to the Ghostscript device fuzzer configured for the pdfwrite device. The harness initializes Ghostscript on the input document and exits normally on ordinary interpreter errors.

### Format Links
- [[postscript-or-pdf-with-cff-type2-font]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
