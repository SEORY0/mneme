---
type: harness-contract
title: "Libjpeg Turbo Fuzz Wrapper harness"
description: "Input contract facts for Libjpeg Turbo Fuzz Wrapper."
tags: ["libjpeg-turbo-fuzz-wrapper", "round-6"]
okf_support: 1
---
# Libjpeg Turbo Fuzz Wrapper Harness

## Round 6 Input Contract
- The libjpeg-turbo build exposes multiple fuzzers; the wrapper selected a JPEG-processing path for the supplied file. Raw bytes are used as the image input, not a directory unless a specific corpus-wrapper path is selected.

## Format Links
- [[jpeg]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
