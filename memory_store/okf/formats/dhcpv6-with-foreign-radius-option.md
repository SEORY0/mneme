---
type: format
title: "Dhcpv6 With Foreign Radius Option"
access_scope: generate
confidence: medium
tags: ["dhcpv6-with-foreign-radius-option", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Dhcpv6 With Foreign Radius Option

## Round 13 Facts
- Normal DHCPv6 packets start with a compact message header followed by options; relay packets use a larger relay header. Options are big-endian code-and-length records, and the option length gates all nested decoding. Some DHCPv6 options are decoded by a foreign protocol dictionary, so their payload is handed to another protocol parser after the DHCPv6 option envelope is accepted. RADIUS long-extended attributes are fragmentable records where consecutive fragments can be coalesced by matching header fields, and the fragment loop must still ensure that each following fragment has enough room for the fragment header before inspecting it.
