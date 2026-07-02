---
type: format-family
title: "Raw Ipv4 Tcp Imap Format"
description: "Input contract facts for raw-ipv4-tcp-imap."
tags: ["raw-ipv4-tcp-imap", "round-30"]
okf_support: 0
train_only: true
---
# Raw Ipv4 Tcp Imap Format

## Round 30 Factual Contract

### Schema / Invariants
- The nDPI process-packet input begins directly at the IPv4 header, not at a pcap record. IPv4 header length, total length, protocol, TCP data offset, and TCP payload length must be mutually consistent for the dissector to expose the application bytes. IMAP detection expects a CRLF-terminated line with a tag followed by a command token; LOGIN additionally parses quoted username and password fields from the payload line.

### Harness Links
- [[libfuzzer-ndpi-process-packet]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
