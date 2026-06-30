---
type: harness-contract
title: "Libfuzzer Config Random Harness"
description: "Input contract facts for libfuzzer-config-random."
tags: ["libfuzzer-config-random", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Config Random Harness

## Round 30 Input Contract

### Input Contract
- The active libFuzzer target writes the raw input bytes to a temporary file, initializes a Fluent Bit config object, calls flb_parser_conf_file on that file, then tears down parser and config state. It does not use FuzzedDataProvider, mode bytes, pcap/file wrappers, or a CLI argument parser.

### Format Links
- [[fluent-bit-parser-config]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
