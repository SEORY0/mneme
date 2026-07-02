---
type: harness-contract
title: "libfuzzer-pcap-file-reader harness"
description: "Input contract facts for libfuzzer-pcap-file-reader."
tags: ["libfuzzer-pcap-file-reader", "round-35"]
okf_support: 1
train_only: true
---
# libfuzzer-pcap-file-reader Harness

## Round 35 Input Contract
### Input Contract
- The libFuzzer target writes the raw input bytes to a temporary pcap file, opens it with PcapFileReaderDevice, reads only the first packet, copies the captured bytes into a heap buffer in getNextPacket, stores the pcap datalink as a LinkLayerType, then constructs a parsed Packet from that RawPacket. There is no selector byte or FuzzedDataProvider carving.

### Format Links
- [[classic-pcap-raw-ip-packet]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
