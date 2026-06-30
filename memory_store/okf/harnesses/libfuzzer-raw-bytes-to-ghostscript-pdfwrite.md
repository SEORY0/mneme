---
type: harness-contract
title: "Libfuzzer Raw Bytes To Ghostscript Pdfwrite Harness"
description: "Input contract facts for libfuzzer-raw-bytes-to-ghostscript-pdfwrite."
tags: ["libfuzzer-raw-bytes-to-ghostscript-pdfwrite", "round-27"]
okf_support: 1
---
# Libfuzzer Raw Bytes To Ghostscript Pdfwrite Harness

## Round 27 Input Contract
- The libFuzzer target passes the raw input buffer to Ghostscript as stdin and selects the pdfwrite device with a null output file.
- There is no FuzzedDataProvider layout, leading mode selector, or external file container; the bytes must be a complete PostScript or PDF program accepted by Ghostscript.

## Round 27 Format Links
- [[postscript-pdfwrite-transparency]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
