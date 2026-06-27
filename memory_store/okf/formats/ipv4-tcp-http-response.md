---
type: format
title: "Ipv4 Tcp Http Response"
access_scope: generate
confidence: medium
tags: ["ipv4-tcp-http-response", "format", "round-13"]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
train_only: true
---
# Ipv4 Tcp Http Response

## Round 13 Facts
- The selected nDPI target consumes a raw layer-three packet, not an Ethernet frame or pcap. For HTTP response parsing, the packet needs an IPv4 header, TCP header, and printable HTTP response payload with CRLF-delimited headers. The server header value is parsed as a named server family followed by a version-like token.
