---
type: harness-contract
title: "Honggfuzz Packet Fuzzer harness"
description: "Input contract facts for honggfuzz packet fuzzer."
tags: ["honggfuzz-packet-fuzzer", "round-22"]
okf_support: 1
---
# Honggfuzz Packet Fuzzer Harness

## Round 22 Input Contract
- The packet fuzzer first validates the magic-delimited FuzzBuffer, then initializes each chunk as a DLT_RAW packet and passes it to Zeek packet analysis. Supplying a bare Ethernet frame without the FuzzBuffer envelope does not reach packet processing.

## Format Links
- [[zeek-fuzzbuffer-packet-chunks]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
