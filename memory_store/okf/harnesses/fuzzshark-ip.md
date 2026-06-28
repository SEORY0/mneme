---
type: harness-contract
title: "Fuzzshark Ip harness"
description: "Round 23 input contract facts for fuzzshark-ip."
tags: ["fuzzshark-ip", "round-23"]
okf_support: 2
train_only: true
---
# Fuzzshark Ip Harness

## Round 23 Input Contract
- The Wireshark fuzzer is compiled for the IP dissector target and runs raw input as a packet record with an unknown wiretap encapsulation, then registers the target dissector as a postdissector. NBAP normally hangs off SCTP payload protocol dispatch and decode-as tables, so an input must first be interpreted as an IP packet and then as SCTP before NBAP can be reached.
- The fuzzshark binary is configured for the IP dissector and disables several transport/application dissectors before registering the IP target as a postdissector over raw unknown-encapsulation packets. RF4CE is not an IP child protocol; it is registered as a heuristic under the IEEE 802.15.4 WPAN dissector, so the missing gate is a carrier path from the IP target to WPAN.

## Round 23 Format Links
- [[nbap-per-over-sctp]]
- [[rf4ce-over-ieee802154]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
