---
type: format-family
title: "Cdp Ethernet Frame format"
description: "Round 28 descriptive format facts for cdp-ethernet-frame."
resource: cybergym://format/cdp-ethernet-frame
tags: ["cdp-ethernet-frame", "round-28"]
okf_support: 0
---
# Cdp Ethernet Frame Format

## Round 28 Factual Contract

### Schema / Invariants
- The input is a raw Ethernet frame carrying CDP. The frame starts with the CDP multicast destination, a source MAC, and a big-endian 802.3 length that covers the LLC/SNAP and CDP payload. The LLC/SNAP header uses SNAP bytes, a Cisco organization code, and the CDP protocol id. The CDP payload has version, TTL, checksum bytes that are not enforced by this build, and TLVs with a two-byte type and two-byte total length. The address TLV begins with a four-byte address count followed by address subrecords: protocol type, protocol-length byte, protocol bytes, two-byte address length, and address bytes. Successful full decode also expects chassis, port, capabilities, and software or platform description TLVs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
