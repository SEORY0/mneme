---
type: harness-contract
title: "Honggfuzz Libfuzzer Compat Harness"
description: "Input contract facts for honggfuzz-libfuzzer-compat."
tags: ["honggfuzz-libfuzzer-compat", "round-27"]
okf_support: 1
---
# Honggfuzz Libfuzzer Compat Harness

## Round 27 Input Contract
- The harness writes the raw input bytes to a temporary MIB file and calls read_mib on that path.
- read_mib reads the first label as the module name, registers the module, reopens the same file, and parses it.
- There is no mode byte, prefix, checksum, or FuzzedDataProvider splitting.

## Round 27 Format Links
- [[snmp-mib-text]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
