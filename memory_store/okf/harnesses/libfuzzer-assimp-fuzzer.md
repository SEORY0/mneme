---
type: harness-contract
title: "Libfuzzer Assimp Fuzzer harness"
description: "Input contract facts for Libfuzzer Assimp Fuzzer."
tags: ["libfuzzer-assimp-fuzzer", "round-6"]
okf_support: 1
---
# Libfuzzer Assimp Fuzzer Harness

## Round 6 Input Contract
- The harness feeds the entire PoC as a model file to Assimp, runs importer detection, imports the scene, and applies post-processing. There is no outer fuzzer selector byte or pcap-like envelope.

## Format Links
- [[assimp-model]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
