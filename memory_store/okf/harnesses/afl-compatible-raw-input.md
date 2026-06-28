---
type: harness-contract
title: "Afl Compatible Raw Input harness"
description: "Input contract facts for afl-compatible-raw-input."
tags: ["afl-compatible-raw-input", "round-22"]
okf_support: 1
---
# Afl Compatible Raw Input Harness

## Round 22 Input Contract
- The AFL-compatible harness reads the raw file bytes and passes them directly to the hoedown document renderer with many Markdown extensions enabled. There is no file container, integrity side channel, selector byte, or FuzzedDataProvider carving.

## Format Links
- [[markdown]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
