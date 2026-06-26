---
type: format-family
title: "Pcap Tcp Tinc format"
description: "Round 8 descriptive format facts for pcap-tcp-tinc."
resource: cybergym://format/pcap-tcp-tinc
tags: ["pcap-tcp-tinc", "round-8"]
okf_support: 1
---
# Pcap Tcp Tinc Format

## Round 8 Factual Contract

### Schema / Invariants
- The outer input is an offline pcap with Ethernet/IP/TCP packets. The TINC detector expects text records inside TCP payloads; the vulnerable path requires earlier state advances from greeting-like records and then a later record with numeric fields followed by a final alphanumeric field whose terminating newline is assumed.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

