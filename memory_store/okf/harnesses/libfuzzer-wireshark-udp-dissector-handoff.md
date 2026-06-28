---
type: harness-contract
title: "Libfuzzer Wireshark UDP Dissector Handoff harness"
description: "Input contract facts for libfuzzer Wireshark udp dissector handoff."
tags: ["libfuzzer-wireshark-udp-dissector-handoff", "round-16"]
okf_support: 1
---
# Libfuzzer Wireshark UDP Dissector Handoff Harness

## Round 16 Input Contract
- The wrapper runs fuzzshark configured for the UDP dissector in the IP protocol table. It wraps the raw bytes in an in-memory Wireshark frame, dissects them, then resets the epan dissection state between iterations.

## Round 16 Format Links
- [[raw-ipv4-udp-packet-bytes]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
