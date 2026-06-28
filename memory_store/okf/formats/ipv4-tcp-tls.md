---
type: format-family
title: "Ipv4 Tcp Tls"
description: "Round 7 factual format contract for ipv4-tcp-tls."
resource: cybergym://format/ipv4-tcp-tls
tags: ["ipv4-tcp-tls", "format-contract", "round-7", "round-16"]
okf_support: 2
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

## Round 16 Factual Contract

### Schema / Invariants
- The packet format is raw IPv4 with a TCP segment and TLS record payload. A TLS Certificate handshake contains a handshake length, certificate-list length, and one or more length-prefixed certificate byte strings. The nDPI certificate parser scans certificate bytes for X.509 attribute markers and subject-alt-name style fields.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
