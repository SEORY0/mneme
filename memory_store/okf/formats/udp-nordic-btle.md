---
type: format
title: "Udp Nordic Btle"
access_scope: generate
confidence: medium
tags: ["udp-nordic-btle", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Udp Nordic Btle

## Round 13 Facts
- The relevant protocol stack is UDP carrying a Nordic BLE sniffer record, which can then pass a context object into the BTLE dissector. Nordic BLE records contain a sniffer header with version, lengths, packet id, flags, channel, signal metadata, timing metadata, and then the BTLE link-layer payload.
