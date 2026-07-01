---
type: harness-contract
title: "Afl Libfuzzer Ncp Uart Received harness"
description: "Input contract facts for afl-libfuzzer-ncp-uart-received."
tags: ["afl-libfuzzer-ncp-uart-received", "round-32"]
okf_support: 1
---
# Afl Libfuzzer Ncp Uart Received Harness

## Round 32 Input Contract
- The selected fuzzer initializes an OpenThread instance, initializes NCP, sets the PAN ID, enables IPv6 and Thread, becomes leader, then passes the entire raw input once to otPlatUartReceived and drains pending tasklets. There is no FuzzedDataProvider and no outer mode byte; all structure must be expressed as UART HDLC/Spinel bytes in the file.

## Round 32 Format Links
- [[openthread-ncp-uart]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
