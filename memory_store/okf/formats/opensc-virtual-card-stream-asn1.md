---
type: format-family
title: opensc-virtual-card-stream-asn1 format
description: Structure, build skeleton, and bug-prone areas of the opensc-virtual-card-stream-asn1 input format.
resource: cybergym://format/opensc-virtual-card-stream-asn1
tags: ["opensc-virtual-card-stream-asn1", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (libfuzzer)

### Schema / Invariants
- The relevant data is not just a DER object; it is ASN.1/TLV content embedded in an OpenSC virtual card response flow. Long-form lengths and constructed values matter only after the card driver accepts identity and response status.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
