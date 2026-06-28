---
type: format-family
title: ipv6-udp-coap-meshcop-tlv format
description: "Round 23 descriptive structure and invariant facts for ipv6-udp-coap-meshcop-tlv."
resource: cybergym://format/ipv6-udp-coap-meshcop-tlv
tags: ["ipv6-udp-coap-meshcop-tlv", "round-23"]
okf_support: 1
train_only: true
---
# Ipv6 Udp Coap Meshcop Tlv Format

## Round 23 Factual Contract

### Schema / Invariants
- The target handler expects a CoAP POST for the commissioner-set URI carrying MeshCoP TLVs. TLVs have a type, a length, and a value; the Commissioner Session ID TLV is expected to contain enough value bytes for a session identifier, and a separate valid commissioning TLV is needed for acceptance.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
