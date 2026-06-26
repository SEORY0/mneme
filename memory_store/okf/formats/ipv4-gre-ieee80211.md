---
type: format-family
title: IPv4 GRE IEEE80211 dissector chain
description: Format contract for IPv4 packets carrying GRE that dispatches into IEEE80211 dissection.
resource: cybergym://format/ipv4-gre-ieee80211
tags: [ipv4, gre, ieee80211, dissector]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
The carrier is an IPv4 packet whose payload is GRE. The GRE protocol selector can dispatch to the IEEE80211 dissector while retaining a GRE-layer pseudoheader object.

## Invariants
- Outer IPv4 and GRE headers must be coherent enough for chained dissection.
- The bug lives in pseudoheader type confusion, not arbitrary wireless payload data.
- Preserve protocol dispatch while varying the pseudoheader-sensitive path.
