---
type: format-family
title: "Curl Websocket Fuzzer Input"
description: "Round 12 factual format contract for curl websocket fuzzer input."
resource: cybergym://format/curl-websocket-fuzzer-input
tags: ["curl-websocket-fuzzer-input", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Curl Websocket Fuzzer Input

## Round 12 Factual Contract

### Schema / Invariants
- The vulnerable curl option expects an AWS SigV4 provider string and related request headers, while websocket traffic uses HTTP upgrade messages and WebSocket frames. Those are distinct input families, and the observed fuzzer did not expose the CLI option surface directly.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
