---
type: format-family
title: "Openthread Ip6 Message format"
description: "Descriptive contract facts for Openthread Ip6 Message."
resource: "cybergym://format/openthread-ip6-message"
tags: ["openthread-ip6-message", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The attempted carrier is an OpenThread IPv6 message buffer: the first fuzzer byte selects message settings and the remaining bytes are appended to a newly allocated otMessage before otIp6Send drives tasklets and platform processing.

### Harness Links
- [[libfuzzer-ip6-send-fuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
