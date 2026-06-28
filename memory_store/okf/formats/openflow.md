---
type: format-family
title: "openflow format"
description: "Structure and invariants observed for openflow."
resource: "cybergym://format/openflow"
tags: ["openflow", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- OpenFlow messages begin with a fixed message header containing version, type, total length, and transaction id. Packet-out bodies carry an action byte count, and actions are aligned records. Experimenter actions add a vendor and subtype before action-specific fields; RAW_ENCAP carries an encapsulation type followed by padded property records.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
