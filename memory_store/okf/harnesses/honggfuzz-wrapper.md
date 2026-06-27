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

## Round 13 Facts
- The source tree builds OpenThread fuzz targets including ip6-send, radio-receive-done, ncp-uart-received, and cli-uart-received. Local verify identified the selected target as the ip6-send honggfuzz wrapper; the wrapper printed fuzzing usage instead of consuming the supplied single PoC file as raw input.

## Round 14 Input Contract
- The selected OpenSC target was fuzz_pkcs15_decode. Its source has a libFuzzer-style entrypoint, but the observed wrapper output was the honggfuzz usage path. The source-level contract consumes a little-endian length prefix before separating parser bytes from reader-emulation bytes.

## Round 14 Format Links
- [[pkcs15-decode-fuzzer-input]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
