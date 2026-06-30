---
type: harness-contract
title: "Libfuzzer Mock TCP Harness"
description: "Input contract facts for libfuzzer-mock-tcp."
tags: ["libfuzzer-mock-tcp", "round-27"]
okf_support: 1
---
# Libfuzzer Mock TCP Harness

## Round 27 Input Contract
- The libFuzzer input is sent as raw bytes through a mock TCP peer to a ZeroMQ socket.
- There is no leading mode byte, archive wrapper, checksum gate, or FuzzedDataProvider splitting; all supplied bytes become the peer's transport stream.

## Round 27 Format Links
- [[zmtp-v1]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
