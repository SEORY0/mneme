---
type: format-family
title: "Ipv4 Tcp Http Request format"
description: "Descriptive contract facts for Ipv4 Tcp Http Request."
resource: "cybergym://format/ipv4-tcp-http-request"
tags: ["ipv4-tcp-http-request", "round-6"]
okf_support: 1
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- The carrier is not a pcap file for this harness; it is a raw IPv4 packet with a TCP header and HTTP payload. HTTP subprotocol parsing extracts hostnames from Host and Origin headers and passes the hostname pointer plus length to the host subprotocol matcher.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
