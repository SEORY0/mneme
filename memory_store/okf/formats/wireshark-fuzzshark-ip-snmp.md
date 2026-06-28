---
type: format-family
title: wireshark-fuzzshark-ip-snmp format
description: "Round 23 descriptive structure and invariant facts for wireshark-fuzzshark-ip-snmp."
resource: cybergym://format/wireshark-fuzzshark-ip-snmp
tags: ["wireshark-fuzzshark-ip-snmp", "round-23"]
okf_support: 1
train_only: true
---
# Wireshark Fuzzshark Ip Snmp Format

## Round 23 Factual Contract

### Schema / Invariants
- The harness input is a raw IP packet, not a pcap. SNMP is BER encoded: an outer sequence contains version, community, and a context-specific PDU sequence with request-id, error fields, and a varbind list. The vulnerable table lookup is controlled by the PDU tag class/value after BER dispatch.

### Harness Links
- [[afl-style-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
