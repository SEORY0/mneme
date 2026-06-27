---
type: harness
title: "Afl Fuzzshark"
harness_convention: afl-fuzzshark
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Afl Fuzzshark

## Input Contract
- For `udp-nordic-btle`, The fuzzshark binary reads a raw input file as an IP-protocol UDP payload and invokes the UDP dissector. Port fields inside the UDP header can influence downstream payload dispatch, but decode-as-only dissectors may not be selected by raw payload bytes alone.
- For `bootp-dhcp-dns-name`, The fuzzshark target invokes the BOOTP dissector from the UDP port table on raw UDP payload bytes. A valid BOOTP fixed header, DHCP magic cookie, and option list are needed before DNS-name option payloads are interpreted.
