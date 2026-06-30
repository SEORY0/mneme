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

## Round 28 Input Contract

- The MuPDF libFuzzer target passes the raw bytes to fz_open_document_with_stream with PDF magic, but document handling first performs content sniffing on seekable streams. A BMP signature is enough for the image document handler to load the raw BMP as a page, and rendering that page calls the BMP subimage loader. There is no fuzzer prefix selector and no FuzzedDataProvider byte split.

## Round 28 Format Links
- [[bmp]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
