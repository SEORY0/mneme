---
type: harness-contract
title: "Libfuzzer Afl Wrapper harness"
description: "Input contract facts for libfuzzer-afl-wrapper."
tags: ["libfuzzer-afl-wrapper"]
okf_support: 1
---
# Libfuzzer Afl Wrapper Harness

## Round 10 Input Contract
- The active binary was hb-subset-fuzzer under an AFL-style wrapper. It reads the raw file bytes as a font, runs several subset configurations, and may use trailing bytes as codepoints and flags. There is no front selector; valid sfnt structure is the main gate.

## Round 10 Format Links
- [[opentype-sbix-font]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (mvg)

- The harness sets the GraphicsMagick coder to MVG and passes the raw file bytes to Image.read; there is no leading selector byte and no FuzzedDataProvider carving.

## Round 21 Format Links (mvg)
- [[mvg]]

## Round 21 Notes (mvg)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
