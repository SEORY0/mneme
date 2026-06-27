---
type: harness-contract
title: "Libfuzzer Pcap File harness"
description: "Input contract facts for libfuzzer-pcap-file."
tags: ["libfuzzer-pcap-file", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Pcap File Harness

## Round 17 Input Contract
- The harness opens raw input as a pcap file, accepts supported datalink types, and for each packet copies exactly the captured length to a heap buffer before nDPI packet processing.
- Truncating caplen is therefore observable by ASan in tunnel parsing.

## Round 17 Format Links
- [[pcap-vxlan]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[pcap-vxlan]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
