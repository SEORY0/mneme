---
type: harness-contract
title: "Libfuzzer Typefind Harness"
description: "Round 26 input contract facts for libfuzzer-typefind."
tags: ["libfuzzer-typefind", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Typefind Harness

## Round 26 Factual Contract

### Input Contract
- The fuzz target feeds the file bytes directly to GStreamer typefinding through an appsrc-style path. There is no mode selector or FuzzedDataProvider carving; the typefinder peeks an initial text window and passes NUL-terminated text to subtitle autodetection.

### Format Links
- [[subtitle-text]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
