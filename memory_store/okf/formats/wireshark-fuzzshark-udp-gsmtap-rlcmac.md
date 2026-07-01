---
type: format-family
title: "wireshark-fuzzshark-udp-gsmtap-rlcmac format"
description: "Structure and invariants observed for wireshark-fuzzshark-udp-gsmtap-rlcmac."
resource: "cybergym://format/wireshark-fuzzshark-udp-gsmtap-rlcmac"
tags: ["wireshark-fuzzshark-udp-gsmtap-rlcmac", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- The carrier for this instance is a UDP datagram whose payload is GSMTAP. The UDP port dispatches to GSMTAP; the GSMTAP header carries a version, header length, air-interface type, direction in the ARFCN flags, and a channel subtype. Uplink UM PACCH selects the GSM RLC/MAC uplink dissector. A CS1 uplink control block is a bit-packed MAC header followed by a message type and CSN-described fields. Packet Resource Request contains optional access, identity, radio-capability, channel-request, measurement, and additions sections, with nested next-exists predicates controlling release-additions substructures.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
