---
type: format
title: "Ipv4 Tcp Http Response"
input_format: ipv4-tcp-http-response
access_scope: generate
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
---
# Ipv4 Tcp Http Response

## Schema
- The selected nDPI target consumes a raw layer-three packet, not an Ethernet frame or pcap. For HTTP response parsing, the packet needs an IPv4 header, TCP header, and printable HTTP response payload with CRLF-delimited headers. The server header value is parsed as a named server family followed by a version-like token.
