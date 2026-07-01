---
type: format-family
title: "thread-ipv6-coap-meshcop format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/thread-ipv6-coap-meshcop"
tags: ["thread-ipv6-coap-meshcop", "round-35"]
okf_support: 1
train_only: true
---
# thread-ipv6-coap-meshcop Format

## Round 35 Factual Contract
### Schema / Invariants
- The reachable packet is IPv6 plus UDP plus CoAP, with CoAP Uri-Path encoded as separate path options and MeshCoP request parameters encoded as type-length-value records. The energy-scan request needs a syntactically valid channel-mask TLV, count TLV, period TLV, and scan-duration TLV before the server schedules scan callbacks.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
