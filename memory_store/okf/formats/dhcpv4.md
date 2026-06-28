---
type: format-family
title: "Dhcpv4"
description: "Round 7 factual format contract for dhcpv4."
resource: cybergym://format/dhcpv4
tags: ["dhcpv4", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Dhcpv4

## Round 7 Factual Contract

### Schema / Invariants
- DHCPv4 uses a fixed BOOTP-style header followed by an option area. Normal options are tag-length-
value records, with special padding/end tags. The message-type option is required by this decoder
before full option parsing proceeds.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
