---
type: harness-contract
title: "Libfuzzer Graphicsmagick PTIF Coder harness"
description: "Input contract facts for libfuzzer-graphicsmagick-ptif-coder."
tags: ["libfuzzer-graphicsmagick-ptif-coder", "round-32"]
okf_support: 1
---
# Libfuzzer Graphicsmagick PTIF Coder Harness

## Round 32 Input Contract
- The generated target is the GraphicsMagick PTIF coder fuzzer. It passes the entire submitted file as a Magick blob, sets the coder name to PTIF, reads through the TIFF-family decoder, and then writes the decoded image back when the coder supports writing. There is no argv file path contract, fuzzer-side selector byte, integrity-field gate, or FuzzedDataProvider layout.

## Round 32 Format Links
- [[tiff]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
