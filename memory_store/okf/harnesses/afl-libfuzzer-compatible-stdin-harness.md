---
type: harness-contract
title: "Afl Libfuzzer Compatible Stdin Harness Harness"
description: "Input contract facts for afl/libfuzzer-compatible stdin harness."
tags: ["afl-libfuzzer-compatible-stdin-harness", "round-12"]
okf_support: 0
train_only: true
---
# Afl Libfuzzer Compatible Stdin Harness Harness

## Round 12 Input Contract
- The harness writes the raw input to one side of a socket pair, accepts the other side as an H2O HTTP/2 connection, then runs the event loop until the connection closes. There is no mode byte or FuzzedDataProvider carving; the whole input is interpreted as network bytes.

## Round 12 Format Links
- [[http2-request-stream]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
