---
type: harness-contract
title: "Libfuzzer Raw Memory harness"
description: "Input contract facts for libfuzzer-raw-memory."
tags: ["libfuzzer-raw-memory", "round-28"]
okf_support: 0
---
# Libfuzzer Raw Memory Harness

## Round 28 Input Contract

- The libFuzzer input is used directly as an in-memory PDF stream. The harness registers MuPDF document handlers, opens the stream explicitly as a PDF, renders every page to an RGB pixmap with an identity transform, drops the pixmap, and suppresses MuPDF exceptions. There is no mode byte, stdin/file-path contract, or FuzzedDataProvider front/back split.

## Round 28 Format Links
- [[pdf]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
