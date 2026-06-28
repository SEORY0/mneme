---
type: format-family
title: ovs-ofctl-flow-text format
description: Structure, build skeleton, and bug-prone areas of the ovs-ofctl-flow-text input format.
resource: cybergym://format/ovs-ofctl-flow-text
tags: ["ovs-ofctl-flow-text", "round-21"]
timestamp: 2026-06-28T00:00:00Z
okf_support: 1
---
# Schema

## Round 21 Factual Contract (afl-wrapper)

### Schema / Invariants
- The ofctl parse fuzzer expects a leading command-selection byte followed by a NUL-terminated flow-mod text string with no embedded newline. Flow syntax can include packet_type, protocol fields, metadata, ports, and actions; packet_type encoding may be inserted before other match fields.

### Harness Links
- [[afl-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
