---
type: harness-contract
title: "Libfuzzer Afl Wrapper harness"
description: "Input contract facts for libfuzzer-afl-wrapper."
tags: ["libfuzzer-afl-wrapper"]
okf_support: 0
---
# Libfuzzer Afl Wrapper Harness

## Round 10 Input Contract
- The active binary was hb-subset-fuzzer under an AFL-style wrapper. It reads the raw file bytes as a font, runs several subset configurations, and may use trailing bytes as codepoints and flags. There is no front selector; valid sfnt structure is the main gate.

## Round 10 Format Links
- [[opentype-sbix-font]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
