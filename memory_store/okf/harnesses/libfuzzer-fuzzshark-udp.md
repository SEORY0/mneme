---
type: harness-contract
title: "Libfuzzer Fuzzshark UDP harness"
description: "Input contract facts for libfuzzer-fuzzshark-udp."
tags: ["libfuzzer-fuzzshark-udp", "round-20"]
okf_support: 10
---
# Libfuzzer Fuzzshark UDP Harness

## Round 20 Input Contract
- The verifier output identifies the configured fuzzshark target as UDP in the ip.proto table. Raw input is treated as UDP dissector payload or datagram-like bytes, not as a pcap file and not as direct Bluetooth HCI/L2CAP bytes. Reaching btl2cap requires a registered UDP encapsulation handoff that these probes did not satisfy.

## Round 20 Format Links
- [[wireshark-udp-dissector-payload]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 27 Input Contract
- The fuzzshark target feeds the raw file bytes directly as packet data, not as pcap or pcapng.
- The configured handle is the UDP dissector from the IP protocol table registered as a postdissector, so the input should be a UDP header followed by UDP payload.
- There is no mode selector, checksum envelope, or FuzzedDataProvider front/back layout.

## Round 27 Format Links
- [[udp-sigcomp]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
