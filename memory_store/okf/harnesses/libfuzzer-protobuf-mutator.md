---
type: harness-contract
title: "libfuzzer-protobuf-mutator harness"
description: "Input contract facts for libfuzzer-protobuf-mutator."
tags: ["libfuzzer-protobuf-mutator", "round-14"]
okf_support: 1
---
# Libfuzzer Protobuf Mutator Harness

## Round 14 Input Contract
- The nginx harness initializes a synthetic nginx cycle, creates fake client and upstream connections, feeds the request string through a custom recv handler, and feeds the reply string after the proxy path starts. It does not consume raw network bytes directly.

## Round 14 Format Links
- [[text-format-protobuf-http-request]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
