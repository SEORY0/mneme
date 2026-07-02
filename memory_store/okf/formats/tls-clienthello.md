---
type: format-family
title: "tls-clienthello format"
description: "Structure, build skeleton, and bug-prone areas of the tls-clienthello input format."
resource: cybergym://format/tls-clienthello
tags: ["tls-clienthello", "round-29"]
okf_support: 0
---
# TLS Clienthello Format

## Round 29 Factual Contract

### Schema / Invariants
- The input is a TLS handshake record containing a ClientHello. The ClientHello body includes version/random fields, session-id, cipher-suite and compression vectors, then a two-byte total extensions length followed by extension records. A status-request extension contains a one-byte status type, a two-byte responder-id-list vector length and bytes, then a two-byte request-extensions vector length and bytes.

### Harness Links
- [[afl-libfuzzer-wolfssl-server]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
