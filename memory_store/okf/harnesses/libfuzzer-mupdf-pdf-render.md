---
type: harness-contract
title: "Libfuzzer Mupdf Pdf Render harness"
description: "Input contract facts for libfuzzer-mupdf-pdf-render."
tags: ["libfuzzer-mupdf-pdf-render", "round-33"]
okf_support: 1
---
# Libfuzzer Mupdf Pdf Render Harness

## Round 33 Input Contract

### Input Contract
- The libFuzzer input is used directly as PDF bytes in memory. The harness opens the document and renders pages; there is no leading mode byte, carved section, checksum wrapper, or FuzzedDataProvider layout.

### Format Links
- [[pdf]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
