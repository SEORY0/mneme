---
type: format
title: "Bootp Dhcp Dns Name"
access_scope: generate
confidence: medium
tags: ["bootp-dhcp-dns-name", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Bootp Dhcp Dns Name

## Round 13 Facts
- BOOTP/DHCP options can carry DNS names through the domain-search option and SIP-server option. Long options can be split and reassembled using the DHCP long-option convention before the composite option data is passed to the shared DNS-name expander.
