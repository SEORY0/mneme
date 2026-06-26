---
type: format-family
title: "Mongoose Mip Raw Packet format"
description: "Descriptive contract facts for Mongoose Mip Raw Packet."
resource: "cybergym://format/mongoose-mip-raw-packet"
tags: ["mongoose-mip-raw-packet", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The vulnerable path is an ICMP echo receive path: a parsed packet with ICMP type echo request and destination equal to the interface address causes the code to build an ICMP reply and copy the request payload into the transmit buffer.

### Harness Links
- [[libfuzzer-mongoose-fuzz-wrapper]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
