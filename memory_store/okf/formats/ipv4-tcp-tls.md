---
type: format-family
title: "Ipv4 Tcp Tls"
description: "Round 7 factual format contract for ipv4-tcp-tls."
resource: cybergym://format/ipv4-tcp-tls
tags: ["ipv4-tcp-tls", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Ipv4 Tcp Tls

## Round 7 Factual Contract

### Schema / Invariants
- The packet is raw IPv4 with a TCP segment and TLS record payload. The TLS ServerHello contains
standard version, random, session, cipher, compression, and extension fields; ALPN is encoded as an
extension with a vector of length-prefixed protocol names.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
