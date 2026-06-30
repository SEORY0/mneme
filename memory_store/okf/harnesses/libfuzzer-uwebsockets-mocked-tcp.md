---
type: harness-contract
title: "Libfuzzer Uwebsockets Mocked Tcp Harness"
description: "Round 26 input contract facts for libfuzzer-uwebsockets-mocked-tcp."
tags: ["libfuzzer-uwebsockets-mocked-tcp", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Uwebsockets Mocked Tcp Harness

## Round 26 Factual Contract

### Input Contract
- libFuzzer feeds raw bytes to a uSockets mock. The mock repeatedly consumes a chunk-length byte and then delivers that many bytes to the server callback. The active binary is the mocked echo server with compression enabled and a small max-payload setting; no FuzzedDataProvider or external file format is involved.

### Format Links
- [[websocket-permessage-deflate-over-mocked-tcp]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
