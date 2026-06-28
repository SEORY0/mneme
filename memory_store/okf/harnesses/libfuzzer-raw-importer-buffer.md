---
type: harness-contract
title: "Libfuzzer Raw Importer Buffer harness"
description: "Input contract facts for Libfuzzer Raw Importer Buffer."
tags: ["libfuzzer-raw-importer-buffer", "round-6"]
okf_support: 1
---
# Libfuzzer Raw Importer Buffer Harness

## Round 6 Input Contract
- The Assimp fuzzer passes the entire input buffer to Importer.ReadFileFromMemory without a custom extension. Format selection is content-based, so the raw bytes must begin with a recognized format skeleton.

## Format Links
- [[ply]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
