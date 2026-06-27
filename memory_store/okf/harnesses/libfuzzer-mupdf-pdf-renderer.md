---
type: harness-contract
title: "Libfuzzer Mupdf Pdf Renderer harness"
description: "Input contract facts for libfuzzer-mupdf-pdf-renderer."
tags: ["libfuzzer-mupdf-pdf-renderer", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Mupdf Pdf Renderer Harness

## Round 11 Input Contract
- The MuPDF fuzzer feeds the entire raw buffer as a PDF memory stream, opens it with the PDF handler, counts pages, and renders each page to an RGB pixmap. There is no prefix carving or mode selector.

## Format Links
- [[pdf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
