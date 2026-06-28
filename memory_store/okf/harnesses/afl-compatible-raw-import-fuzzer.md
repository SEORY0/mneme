---
type: harness-contract
title: "Afl Compatible Raw Import Fuzzer harness"
description: "Input contract facts for afl-compatible raw import fuzzer."
tags: ["afl-compatible-raw-import-fuzzer", "round-22"]
okf_support: 1
---
# Afl Compatible Raw Import Fuzzer Harness

## Round 22 Input Contract
- The fuzzer passes raw bytes to Assimp ReadFileFromMemory with no extension hint. Format auto-detection must recognize the LightWave marker before the LWS importer runs; no FuzzedDataProvider fields or external container are used.

## Format Links
- [[lightwave-scene]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
