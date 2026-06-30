---
type: format-family
title: "Ipv4 GRE Ieee80211 Amsdu Format"
description: "Round 26 descriptive structure and invariant facts for ipv4-gre-ieee80211-amsdu."
tags: ["ipv4-gre-ieee80211-amsdu", "round-26"]
okf_support: 1
train_only: true
---
# Ipv4 GRE Ieee80211 Amsdu Format

## Round 26 Factual Contract

### Schema / Invariants
- The packet is a raw IPv4 datagram for the fuzzshark IP dissector. GRE protocol payloads can carry Aruba IEEE 802.11 frames. A QoS data frame can contain A-MSDU subframes, and each subframe carries its own LLC/SNAP header that can dispatch to nested protocols, including another IP/GRE/WLAN path or the IEEE 802.11 data-encapsulation tag path.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
