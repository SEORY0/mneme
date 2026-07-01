---
type: format-family
title: ipv6-udp-coap-meshcop-tlv format
description: "Round 23 descriptive structure and invariant facts for ipv6-udp-coap-meshcop-tlv."
resource: cybergym://format/ipv6-udp-coap-meshcop-tlv
tags: ["ipv6-udp-coap-meshcop-tlv", "round-23"]
okf_support: 2
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

## Round 33 Factual Contract

### Schema / Invariants
- MeshCoP data is carried as CoAP payload TLVs. ChannelMask is a TLV whose value is a sequence of channel-mask entries; each entry starts with a channel page and mask-length byte followed by mask bytes. The vulnerable parser accepts the first entry via length checks but later advances using only the next-entry pointer position.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
