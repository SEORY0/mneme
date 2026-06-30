---
type: harness-contract
title: "Libfuzzer Afl Compatible Harness"
description: "Input contract facts for libfuzzer-afl-compatible."
tags: ["libfuzzer-afl-compatible", "round-27"]
okf_support: 1
---
# Libfuzzer Afl Compatible Harness

## Round 27 Input Contract
- The libFuzzer/AFL-compatible harness passes raw file bytes directly to ndpi_detection_process_packet.
- There is no FuzzedDataProvider split and no pcap container; bytes must form a packet buffer with IPv4 and UDP headers before the STUN payload.

## Round 27 Format Links
- [[ipv4-udp-stun-packet]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
