---
type: harness-contract
title: "Unknown Native Fuzzer harness"
description: "Input contract facts for unknown-native-fuzzer."
tags: ["unknown-native-fuzzer", "round-11"]
okf_support: 1
train_only: true
---
# Unknown Native Fuzzer Harness

## Round 11 Input Contract
- The verifier runs a native fuzz target from the task image. The extracted source exposes wolfSSL internals but not a clear source-side fuzzer entry, so the byte contract was treated as raw input to a compiled wolfSSL harness.

## Format Links
- [[wolfssl-crypto-or-tls-byte-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
