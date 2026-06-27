---
type: harness-contract
title: "Afl Wrapper harness"
description: "Input contract facts for afl-wrapper."
tags: ["afl-wrapper"]
okf_support: 0
---
# Afl Wrapper Harness

## Round 10 Input Contract
- The verifier output indicated a required directory path instead of a normal libFuzzer single input file. No FuzzedDataProvider layout was observed; the blocker was the wrapper invocation contract.
- Source extraction required skipping an absolute symlink before runner metadata could be recovered. The active verifier binary read raw input through fuzzshark configured for the UDP dissector in the ip.proto table, not a direct IEEE1905 dissector or Ethernet ethertype wrapper.

## Round 10 Format Links
- [[file-magic-corpus-directory]]
- [[wireshark-fuzzshark-udp-payload]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
