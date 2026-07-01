---
type: harness-contract
title: "Libfuzzer Libssh Server Socket harness"
description: "Input contract facts for libfuzzer-libssh-server-socket."
tags: ["libfuzzer-libssh-server-socket", "round-32"]
okf_support: 1
---
# Libfuzzer Libssh Server Socket Harness

## Round 32 Input Contract
- LibFuzzer bytes are written as the client side of a socketpair to a libssh server instance. There is no FuzzedDataProvider or mode selector; the raw file bytes must include the SSH stream framing needed before pre-crypto packet dispatch reaches userauth parsing.

## Round 32 Format Links
- [[ssh-server-byte-stream]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
