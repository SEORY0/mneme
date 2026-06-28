---
type: format-family
title: pcap-or-pcapng-ip-capture format
description: Structure, build skeleton, and bug-prone areas of the pcap-or-pcapng-ip-capture input format.
resource: cybergym://format/pcap-or-pcapng-ip-capture
tags: [pcap-or-pcapng-ip-capture, "round-22"]
timestamp: 2026-06-28T06:03:30Z
okf_support: 1
---
# Schema

## Round 22 Factual Contract

### Schema / Invariants
- The input must be a pcap or pcapng capture containing frames that the IP dissector harness can extract and dissect. Conversation handling is driven by packet endpoints, ports or protocol-specific conversation identifiers, and dissector registration state.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
