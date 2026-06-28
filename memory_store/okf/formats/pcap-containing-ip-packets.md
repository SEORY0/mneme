---
type: format-family
title: "Pcap Containing IP Packets format"
description: "Structure and invariants for the pcap-containing-ip-packets input format."
tags: ["pcap-containing-ip-packets", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The reader target expects a libpcap file with global header, per-packet records, and a supported datalink such as Ethernet. Packet caplen controls the copied packet buffer before ndpi_workflow_process_packet handles link/IP/transport parsing.

### Harness Links
- [[ndpi-reader-pcap-file-harness]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
