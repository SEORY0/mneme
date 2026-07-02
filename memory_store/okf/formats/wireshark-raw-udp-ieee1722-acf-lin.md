---
type: format-family
title: "Wireshark Raw Udp Ieee1722 Acf Lin format"
description: "Round 34 factual contract for wireshark-raw-udp-ieee1722-acf-lin."
tags: ["wireshark-raw-udp-ieee1722-acf-lin", "round-34"]
okf_support: 1
train_only: true
---
# Wireshark Raw Udp Ieee1722 Acf Lin format

## Round 34 Factual Contract

### Schema / Invariants
- For this harness the file is the UDP datagram seen by Wireshark, not an Ethernet or IP frame. The UDP header drives dissector-table dispatch. The IEEE 1722 payload has a common AVTP subtype header, a timing-control header, then ACF records; each ACF record has a message type and quadlet-count length, and the LIN record carries a small fixed header followed by payload bytes whose effective length is reduced by a pad field.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
