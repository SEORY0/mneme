---
type: harness-contract
title: "Libfuzzer Mupdf Document Renderer harness"
description: "Round 23 input contract facts for libfuzzer-mupdf-document-renderer."
tags: ["libfuzzer-mupdf-document-renderer", "round-23"]
okf_support: 1
train_only: true
---
# Libfuzzer Mupdf Document Renderer Harness

## Round 23 Input Contract
- The active binary is named as a PDF fuzzer but MuPDF's document/content recognition can route raw BMP input through the image/CBZ image path and render it as a page. PDF embedding attempts were unnecessary once direct BMP content sniffing reached the decoder.

## Round 23 Format Links
- [[bmp]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
