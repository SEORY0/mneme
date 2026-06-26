---
type: harness-contract
title: "Libfuzzer Mongoose Fuzz Wrapper harness"
description: "Input contract facts for Libfuzzer Mongoose Fuzz Wrapper."
tags: ["libfuzzer-mongoose-fuzz-wrapper", "round-6"]
okf_support: 1
---
# Libfuzzer Mongoose Fuzz Wrapper Harness

## Round 6 Input Contract
- The selected Mongoose fuzz wrapper runs many parsers, then initializes a MIP interface and calls `mip_rx` on the raw input bytes. There is no pcap envelope; the bytes must match the MIP packet parser’s raw Ethernet/IP expectations.

## Format Links
- [[mongoose-mip-raw-packet]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
