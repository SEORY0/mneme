---
type: harness-contract
title: "Afl Libfuzzer Raw Graphicsmagick MVG Coder harness"
description: "Input contract facts for afl-libfuzzer-raw-graphicsmagick-mvg-coder."
tags: ["afl-libfuzzer-raw-graphicsmagick-mvg-coder", "round-32"]
okf_support: 1
---
# Afl Libfuzzer Raw Graphicsmagick MVG Coder Harness

## Round 32 Input Contract
- The GraphicsMagick coder harness fixes the coder to MVG and passes the entire PoC as a Magick blob. There is no mode selector, length prefix, checksum, or FuzzedDataProvider split; the raw bytes must be accepted as a complete MVG drawing.

## Round 32 Format Links
- [[mvg]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
