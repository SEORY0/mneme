---
type: harness-contract
title: "Libfuzzer Raw Packet Processor harness"
description: "Input contract facts for libfuzzer-raw-packet-processor."
tags: ["libfuzzer-raw-packet-processor"]
okf_support: 0
---
# Libfuzzer Raw Packet Processor Harness

## Round 10 Input Contract
- The fuzz target passes the entire input buffer directly to nDPI packet processing as one packet. There is no pcap decoding and no leading mode selector.

## Round 10 Format Links
- [[raw-ip-packet-carrying-quic]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The fuzz target passes the entire input directly to nDPI packet processing as one packet. There is no pcap header and no leading mode selector.

## Format Links
- [[raw-ipv4-packet-carrying-netbios]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
