---
type: harness-contract
title: "Afl Libfuzzer Wolfssl Server harness"
description: "Input contract facts for afl/libfuzzer wolfssl-server."
tags: ["afl-libfuzzer-wolfssl-server", "round-29"]
okf_support: 0
---
# Afl Libfuzzer Wolfssl Server Harness

## Round 29 Input Contract

- The /bin/arvo wrapper runs the wolfSSL server fuzz target on the PoC file as raw network input. The harness installs custom recv/send callbacks and feeds the raw file bytes sequentially to wolfSSL_accept, resetting the same bytes for several server protocol methods. There is no FuzzedDataProvider splitting and no leading mode byte.

## Round 29 Format Links
- [[tls-clienthello]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
