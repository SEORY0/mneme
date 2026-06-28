---
type: format-family
title: "Zeek Fuzzbuffer Ip Gre Ieee80211 format"
description: "Descriptive contract facts for zeek-fuzzbuffer-ip-gre-ieee80211."
resource: "cybergym://format/zeek-fuzzbuffer-ip-gre-ieee80211"
tags: ["zeek-fuzzbuffer-ip-gre-ieee80211", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- Zeek packet fuzzing uses a chunk envelope beginning with a packet magic and an originator/responder selector.
- To reach the wireless parser from DLT_RAW, a raw IPv4 packet can carry GRE with an Aruba-style protocol value that maps the inner link type to IEEE802.11.
- An A-MSDU QoS data frame has a wireless header, QoS control with the A-MSDU bit, then subframes with destination, source, and payload length before LLC/SNAP data.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
