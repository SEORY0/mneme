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

## Round 34 Factual Contract

### Schema / Invariants
- OpenThread Thread-management traffic for this path is a raw IPv6 datagram carrying UDP to the Thread management CoAP port. The CoAP request must use POST, Uri-Path options for the commissioner-set resource, and a payload marker before MeshCoP TLVs. MeshCoP TLVs use a type byte, a one-byte base length, and, when the base length is the extended marker, an additional length field before the value. Commissioner-set parsing expects a commissioner session TLV and at least one valid commissioning TLV such as joiner UDP port or steering data; unknown TLVs are otherwise skipped by walking to the next TLV.

### Harness Links
- [[libfuzzer-ip6-send-fuzzer]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
## Round 37 Factual Contract

### Schema / Invariants
- The tested carrier is a complete IPv6 datagram containing UDP to the Thread Management Framework port and CoAP payloads.
- CoAP Uri-Path options are split into path segments.
- MeshCoP payloads are type-length-value records; active dataset messages require a timestamp TLV before dataset contents are accepted.
- Channel-mask TLV values are sequences of entries, each with a page selector, a mask-length field, and mask bytes.
- Pan ID query messages carry both a channel mask and a PAN ID field, while active dataset messages store dataset TLVs after validation.

### Harness Links
- [[libfuzzer-ip6-send]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 38 Factual Contract

### Schema / Invariants
- The carrier is an IPv6 packet with UDP and CoAP framing before MeshCoP TLVs. CoAP resource routing is driven by URI-path options and a payload marker separates options from the TLV body. MeshCoP TLVs use a type/length/value layout; valid Joiner UDP Port or Steering Data TLVs can satisfy the handler's accepted-data gate, while Commissioner Session ID has a fixed-width value that must match its declared TLV length.

### Harness Links
- [[libfuzzer-ip6-send]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
