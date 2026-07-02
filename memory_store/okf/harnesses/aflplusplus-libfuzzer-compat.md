---
type: harness-contract
title: "Aflplusplus Libfuzzer Compat Harness"
description: "Input contract facts for aflplusplus-libfuzzer-compat."
tags: ["aflplusplus-libfuzzer-compat", "round-30"]
okf_support: 0
train_only: true
---
# Aflplusplus Libfuzzer Compat Harness

## Round 30 Input Contract

### Input Contract
- The oss-fuzz client harness writes the entire file verbatim to one side of a socketpair, shuts down writes, and runs libssh2_session_handshake on the other side in blocking mode. There is no FuzzedDataProvider, mode selector, or tail carving; all bytes are consumed as network input from a synthetic SSH server. The AFL++ standalone driver calls the libFuzzer-style entry point once for the file.

### Format Links
- [[ssh-handshake-transcript]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
