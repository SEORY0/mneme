---
type: harness-contract
title: "Libfuzzer Pcap Reader harness"
description: "Input contract facts for libfuzzer-pcap-reader."
tags: ["libfuzzer-pcap-reader", "round-15"]
okf_support: 1
---
# Libfuzzer Pcap Reader Harness

## Round 15 Input Contract
- The active nDPI harness writes the raw fuzzer buffer to a temporary capture file, opens it with
  pcap, iterates captured packets, copies each packet to a heap buffer, and passes packets into the
  nDPI workflow. It is not a raw packet-only or FuzzedDataProvider harness.

## Format Links
- [[pcap-tls]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
