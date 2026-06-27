---
type: format
title: "Bootp Dhcp Dns Name"
input_format: bootp-dhcp-dns-name
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Bootp Dhcp Dns Name

## Schema
- BOOTP/DHCP options can carry DNS names through the domain-search option and SIP-server option. Long options can be split and reassembled using the DHCP long-option convention before the composite option data is passed to the shared DNS-name expander.
