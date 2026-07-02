---
type: harness-contract
title: "Libfuzzer Graphicsmagick PTIF Coder Writeback harness"
description: "Input contract facts for libfuzzer-graphicsmagick-ptif-coder-writeback."
tags: ["libfuzzer-graphicsmagick-ptif-coder-writeback", "round-32"]
okf_support: 1
---
# Libfuzzer Graphicsmagick PTIF Coder Writeback Harness

## Round 32 Input Contract
- The GraphicsMagick coder fuzzer passes the raw file blob to Magick++ with the coder fixed to PTIF and no prefix, mode byte, or FuzzedDataProvider. In this build the writable coder path is enabled, so successful reads are followed by PTIF writeback through GraphicsMagick image processing.

## Round 32 Format Links
- [[ptif-tiff]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
