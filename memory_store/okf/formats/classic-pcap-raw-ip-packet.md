---
type: format-family
title: "classic-pcap-raw-ip-packet format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/classic-pcap-raw-ip-packet"
tags: ["classic-pcap-raw-ip-packet", "round-35"]
okf_support: 1
train_only: true
---
# classic-pcap-raw-ip-packet Format

## Round 35 Factual Contract
### Schema / Invariants
- Classic pcap inputs have a global header with byte order, version, snap length, and link-layer type, followed by per-packet timestamp, captured-length, original-length, and packet bytes. The packet record lengths must match the bytes present so libpcap returns a packet to PcapPlusPlus. Raw-IP link-layer captures start packet bytes at the IP header, without Ethernet framing.

### Harness Links
- [[libfuzzer-pcap-file-reader]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
