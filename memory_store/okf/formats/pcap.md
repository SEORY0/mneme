---
type: format-family
title: pcap format
description: Structure, build skeleton, and bug-prone areas of the pcap input format.
resource: cybergym://format/pcap
tags: [pcap]
timestamp: 2026-06-24T00:00:00Z
okf_support: 4
---
# Schema
## Structure
Not yet curated in detail. Identify the magic/header, keep the prefix valid to reach the sink, and prefer seed-mutate when a corpus exists.

# Examples
- Support: 4 train-set solves.
- Winning strategies (observed): {'seed-sweep': 3, 'fuzzer': 1}
- Format families (observed): {'pcap': 4}
- Abstract sink shapes (observed): heap-buffer-overflow:READ, heap-buffer-overflow:WRITE

# Citations
- Distilled from train-set solves with this format + curated format knowledge.
## Round 3 Verified Contracts
- [[pcap-usb-metadata-short-capture]]: Classic PCAP packet records can reach link-type fixup with a capture length shorter than the metadata header.

## Round 9 Factual Contract

### Schema / Invariants
- The harness expects a complete PCAP file, not a raw packet.
- A valid global header and packet record are required.
- The vulnerable path is reached through Ethernet linktype parsing, VLAN ethertype rechecks, and
  then MPLS ethertype handling.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- Classic pcap uses a global header with a network/link-type field followed by per-packet timestamp and captured-length records.
- Pcapng uses a section header, interface description blocks with a per-interface link type, and enhanced packet blocks.
- PcapPlusPlus reads the first packet via libpcap before constructing a RawPacket.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
