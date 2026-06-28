---
type: harness-contract
title: "Afl Libfuzzer Raw Ndpi Process Packet harness"
description: "Input contract facts for afl-libfuzzer-raw-ndpi-process-packet."
tags: ["afl-libfuzzer-raw-ndpi-process-packet", "round-20"]
okf_support: 1
---
# Afl Libfuzzer Raw Ndpi Process Packet Harness

## Round 20 Input Contract
- The harness initializes nDPI once, allocates one flow plus source/destination ids, clears them for each input, and calls ndpi_detection_process_packet directly on the raw input bytes. There is no pcap wrapper and no front/back byte carving.

## Round 20 Format Links
- [[raw-ipv4-packet]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
