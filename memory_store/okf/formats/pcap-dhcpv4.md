---
type: format-family
title: "Pcap Dhcpv4 format"
description: "Descriptive contract facts for pcap-dhcpv4."
resource: "cybergym://format/pcap-dhcpv4"
tags: ["pcap-dhcpv4", "round-16"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 16 Factual Contract

### Schema / Invariants
- The relevant packet is DHCPv4 carried inside IPv4/UDP and usually wrapped in a pcap record for this harness. DHCP options follow the fixed BOOTP/DHCP header and magic cookie; each option has an id, a length, and length-controlled value bytes, ending with an end marker.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
