---
type: format-family
title: "tls-clienthello-stream format"
description: "Structure and reachability facts for tls-clienthello-stream."
resource: cybergym://format/tls-clienthello-stream
tags: ["tls-clienthello-stream"]
okf_support: 1
---
# Tls Clienthello Stream Format

## Round 9 Factual Contract

### Schema / Invariants
- The server fuzzer consumes TLS record bytes representing the client side of an OpenSSL server
  handshake.
- Useful inputs are ClientHello-oriented byte streams with coherent TLS record headers, handshake
  lengths, protocol version, random/session fields, cipher suites, and extensions such as session
  tickets or PSK-related data.

### Harness Links
- [[afl-file-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
