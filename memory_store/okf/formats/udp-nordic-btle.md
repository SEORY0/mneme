---
type: format
title: "Udp Nordic Btle"
input_format: udp-nordic-btle
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Udp Nordic Btle

## Schema
- The relevant protocol stack is UDP carrying a Nordic BLE sniffer record, which can then pass a context object into the BTLE dissector. Nordic BLE records contain a sniffer header with version, lengths, packet id, flags, channel, signal metadata, timing metadata, and then the BTLE link-layer payload.
