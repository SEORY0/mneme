---
type: format-family
title: "Netbios Name Service Packet"
description: "Round 12 factual format contract for netbios-name-service-packet."
resource: cybergym://format/netbios-name-service-packet
tags: ["netbios-name-service-packet", "format-contract", "round-12"]
okf_support: 0
train_only: true
---
# Netbios Name Service Packet

## Round 12 Factual Contract

### Schema / Invariants
- The packet starts with a NetBIOS name-service header containing count fields. A question record contains an encoded NetBIOS name followed by type and class fields when parsing succeeds. Encoded names use a length-prefixed doubled-letter representation, and domain components may use DNS-style compression pointers.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
