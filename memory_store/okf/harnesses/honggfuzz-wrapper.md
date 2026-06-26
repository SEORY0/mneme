---
type: harness-contract
title: "Honggfuzz Wrapper harness"
description: "Input contract facts for Honggfuzz Wrapper."
tags: ["honggfuzz-wrapper", "round-6"]
okf_support: 3
---
# Honggfuzz Wrapper Harness

## Round 6 Input Contract
- The observed binary was a honggfuzz-style fuzzer that reported an input path and usage requirements instead of consuming the single file as libFuzzer input. The run did not expose a mode selector or FuzzedDataProvider-style byte contract.
- The observed nm fuzzer is honggfuzz-style: it writes or receives a candidate file and then asks BFD/nm to identify and display symbols. There is no byte-level mode selector; parser reachability depends on BFD recognizing the object format.
- The observed binary reported that a required input directory was missing. It did not behave like a single-file libFuzzer harness and did not consume the raw candidate bytes directly through the runner path.

## Format Links
- [[disk-or-filesystem-image]]
- [[ecoff-bfd-object]]
- [[gml-graph-text]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
