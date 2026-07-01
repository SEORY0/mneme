---
type: format-family
title: "pcap-ethernet-ipv4-tcp-tls-clienthello format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/pcap-ethernet-ipv4-tcp-tls-clienthello"
tags: ["pcap-ethernet-ipv4-tcp-tls-clienthello", "round-35"]
okf_support: 1
train_only: true
---
# pcap-ethernet-ipv4-tcp-tls-clienthello Format

## Round 35 Factual Contract
### Schema / Invariants
- The harness input is a PCAP capture, not a raw packet. A useful carrier is an Ethernet/IPv4/TCP packet containing a TLS ClientHello record. The ClientHello body contains variable-length session, cipher, compression, and extension sections; the Supported Versions extension payload begins with a vector length followed by fixed-width version entries.

### Harness Links
- [[libfuzzer-pcap-reader]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
