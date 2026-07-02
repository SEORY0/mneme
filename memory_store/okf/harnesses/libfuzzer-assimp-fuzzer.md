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

## Round 36 Input Contract
- The libFuzzer harness passes the entire PoC as raw bytes to Assimp Importer::ReadFileFromMemory with no outer selector or FuzzedDataProvider carving. Assimp's memory IO exposes the submitted buffer under an internal memory filename, so importer selection and any secondary-file resolution are controlled by model syntax inside the same raw buffer.

## Round 36 Format Links
- [[wavefront-obj-with-mtl]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
