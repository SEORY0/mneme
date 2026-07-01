---
type: format-family
title: "Raw Ipv4 Nested Ieee1905 Format"
description: "Structure, build skeleton, and bug-prone areas of the raw-ipv4-nested-ieee1905 input format."
resource: "cybergym://format/raw-ipv4-nested-ieee1905"
tags: ["raw-ipv4-nested-ieee1905", "round-37"]
okf_support: 1
train_only: true
---
# Raw Ipv4 Nested Ieee1905 Format
## Round 37 Factual Contract

### Schema / Invariants
- IEEE1905 is registered through Wireshark's ethertype table.
- Its message header contains version/reserved fields, message type, message id, fragment id, and flags.
- A non-final fragment or a nonzero fragment id takes the reassembly path; a last fragment with the initial fragment id takes direct TLV parsing.
- NHRP traffic indications can dispatch the embedded packet by protocol type, including ethertype and SNAP-derived ethertype forms.
- IEEE 802.15.4 data frames can carry payload IEs; an MPX payload IE can dispatch its remaining payload by ethertype, and the default dissector expects frame-control/address fields plus its normal trailer handling.

### Harness Links
- [[afl-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
