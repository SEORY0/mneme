---
type: harness-contract
title: "Libfuzzer Opensips Message Parser Harness"
description: "Input contract facts for libfuzzer-opensips-message-parser."
tags: ["libfuzzer-opensips-message-parser", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Opensips Message Parser Harness

## Round 30 Input Contract

### Input Contract
- The libFuzzer/AFL driver passes the raw file buffer and length directly to the SIP message parser. The input is a text SIP buffer with no guaranteed NUL terminator, no mode byte, no argv framing, and no FuzzedDataProvider front/back layout.

### Format Links
- [[sip-message]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
