---
type: harness-contract
title: "Afl Libfuzzer Raw Packet harness"
description: "Input contract facts for afl-libfuzzer-raw-packet."
tags: ["afl-libfuzzer-raw-packet", "round-15"]
okf_support: 1
---
# Afl Libfuzzer Raw Packet Harness

## Round 15 Input Contract
- The packet fuzzer passes raw file bytes directly to ndpi_detection_process_packet as one packet.
  There is no pcap framing, argv layer, mode selector, checksum repair requirement, or
  FuzzedDataProvider carving.

## Format Links
- [[ipv4-udp-capwap]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
