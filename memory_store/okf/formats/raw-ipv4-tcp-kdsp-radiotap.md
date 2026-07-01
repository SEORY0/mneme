---
type: format-family
title: "raw-ipv4-tcp-kdsp-radiotap format"
description: "Structure and invariants observed for raw-ipv4-tcp-kdsp-radiotap."
resource: "cybergym://format/raw-ipv4-tcp-kdsp-radiotap"
tags: ["raw-ipv4-tcp-kdsp-radiotap", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- fuzzshark_ip expects a raw IP packet, not a pcap file. KDSP is reachable through TCP from IP dissection and frames messages with a fixed command/length header followed by a capture-packet bitmap. A KDSP capture-data header can carry both a reported payload length and a datalink selector; the radiotap datalink selector hands the remaining payload to the radiotap dissector. Radiotap uses a little-endian header with a present bitmap; present fields are naturally aligned. The VHT radiotap field includes known flags, flag bits, bandwidth, and per-user MCS/NSS nibbles; rate calculation requires known bandwidth and guard interval.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
