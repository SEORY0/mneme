---
type: format-family
title: "Ssh Handshake Transcript Format"
description: "Input contract facts for ssh-handshake-transcript."
tags: ["ssh-handshake-transcript", "round-30"]
okf_support: 0
train_only: true
---
# Ssh Handshake Transcript Format

## Round 30 Factual Contract

### Schema / Invariants
- The harness input is an SSH server transcript. A valid-looking transcript starts with an SSH identification line, then SSH binary packets. A plaintext packet has a network-order packet length, a padding-length field, payload bytes, and optional padding. The server KEXINIT payload begins with a message type byte, a cookie, and SSH name-lists encoded as network-order lengths followed by comma-delimited ASCII algorithm names. The early strict-KEX path only needs the first KEX name-list to be present; the rest of KEXINIT can be absent because the vulnerable scan happens before full method negotiation.

### Harness Links
- [[aflplusplus-libfuzzer-compat]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
