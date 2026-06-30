---
type: harness-contract
title: "Libfuzzer Mupdf Pdf Renderer harness"
description: "Input contract facts for libfuzzer-mupdf-pdf-renderer."
tags: ["libfuzzer-mupdf-pdf-renderer", "round-11", "round-16"]
okf_support: 10
train_only: true
---
# Libfuzzer Mupdf Pdf Renderer Harness

## Round 11 Input Contract
- The MuPDF fuzzer feeds the entire raw buffer as a PDF memory stream, opens it with the PDF handler, counts pages, and renders each page to an RGB pixmap. There is no prefix carving or mode selector.

## Format Links
- [[pdf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 14 Input Contract
- The MuPDF fuzzer opens the raw bytes as a PDF stream, counts pages, and rasterizes each page to an RGB pixmap under a capped allocator. It catches MuPDF exceptions, so only native sanitizer faults count as crashes.

## Round 14 Format Links
- [[pdf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 16 Input Contract
- The MuPDF fuzzer opens the entire input buffer as a PDF memory stream, counts pages, and rasterizes each page to an RGB pixmap. There is no prefix carving or mode selector; MuPDF exceptions are caught, so only process-level sanitizer faults are meaningful.

## Round 16 Format Links
- [[pdf]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 17 Input Contract
- libFuzzer passes the raw byte buffer directly to MuPDF as a PDF memory stream; there is no outer fuzzer envelope.
- A syntactically plausible PDF header, objects, xref or xref stream, start marker, and EOF marker are needed to reach document loading and page rendering.

## Round 17 Format Links
- [[pdf-xref-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[pdf-xref-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 27 Input Contract
- The MuPDF libFuzzer target opens the input bytes directly as an in-memory PDF and then exercises page counting/rendering under the fuzzer allocator.
- There is no outer archive, no mode selector, and no FuzzedDataProvider layout; parser exceptions are caught unless a sanitizer-visible memory error occurs.

## Round 27 Format Links
- [[pdf-xref-stream]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
