---
type: harness-contract
title: "Afl Libfuzzer HTTP2 Socket harness"
description: "Input contract facts for afl-libfuzzer-http2-socket."
tags: ["afl-libfuzzer-http2-socket", "round-32"]
okf_support: 1
---
# Afl Libfuzzer HTTP2 Socket Harness

## Round 32 Input Contract
- The AFL/libFuzzer-compatible H2O harness reads the submitted file and writes it to a socket in chunks split by a textual marker. Bytes before each marker are sent as one client write, empty marker turns let the event loop drain without adding protocol bytes, and the server runs H2O HTTP/2 with fixed, reverse-proxy, and file-root handlers.

## Round 32 Format Links
- [[http2-frame-stream]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
