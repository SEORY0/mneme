---
type: format-family
title: "Wireshark Fuzzshark Ip Packet Format"
description: "Round 27 descriptive format facts for wireshark-fuzzshark-ip-packet."
resource: cybergym://format/wireshark-fuzzshark-ip-packet
tags: ["wireshark-fuzzshark-ip-packet", "round-27"]
okf_support: 1
---
# Wireshark Fuzzshark Ip Packet Format

## Round 27 Factual Contract

- The effective input is a raw packet buffer for Wireshark fuzzshark's IP target.
- A successful carrier can nest protocol dispatch through IP-family headers and a SCOP/IEEE 802.15.4 no-FCS frame before Zigbee NWK and APS parsing.
- The Zigbee APS transport-key command carries a key type followed by a fixed-length key and descriptor fields; the NWK layer supplies PAN hints used by the keyring lookup.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
