---
type: format-family
title: "Samba Ndr Nbt Public Struct Stream format"
description: "Round 34 factual contract for samba-ndr-nbt-public-struct-stream."
tags: ["samba-ndr-nbt-public-struct-stream", "round-34"]
okf_support: 1
train_only: true
---
# Samba Ndr Nbt Public Struct Stream format

## Round 34 Factual Contract

### Schema / Invariants
- The input begins with a little-endian fuzzer header containing flags and a public-structure selector, followed by the NDR body for that selected structure. For this NBT target, public structures include name, class/type, resource-data, name-packet, datagram, sockaddr, netlogon, and browse structures. Several NBT structures use count-controlled arrays, custom NBT string/name helpers, no-alignment or big-endian flags, and scalar-plus-buffer pull/push phases.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
