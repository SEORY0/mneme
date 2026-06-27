---
type: harness-contract
title: "Libfuzzer Poppler Qt Pdf harness"
description: "Input contract facts for libfuzzer-poppler-qt-pdf."
tags: ["libfuzzer-poppler-qt-pdf", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Poppler Qt Pdf Harness

## Round 11 Input Contract
- The libFuzzer target passes the raw input as PDF bytes to the Qt Poppler loading path and then exercises document/page operations. There is no front selector byte and no FuzzedDataProvider layout; the full file must be a PDF container.

## Format Links
- [[pdf-with-embedded-truetype-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
