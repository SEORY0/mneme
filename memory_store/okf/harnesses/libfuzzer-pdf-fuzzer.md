---
type: harness-contract
title: "Libfuzzer Pdf Fuzzer Harness"
description: "Input contract facts for libfuzzer-pdf-fuzzer."
tags: ["libfuzzer-pdf-fuzzer", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Pdf Fuzzer Harness

## Round 30 Input Contract

### Input Contract
- The harness feeds raw input bytes to an in-memory MuPDF stream opened as a PDF, registers document handlers, counts pages, and renders each page to an RGB pixmap. There is no prefix, mode selector, side-channel validation field, or FuzzedDataProvider layout. The outer harness catches normal MuPDF exceptions and returns cleanly, so parser warnings, missing resources, and handled syntax errors are not successes; only sanitizer-visible corruption or an uncaught process failure that reproduces against the official vulnerable image counts.

### Format Links
- [[pdf]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
