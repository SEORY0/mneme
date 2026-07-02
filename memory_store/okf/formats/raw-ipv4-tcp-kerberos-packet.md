---
type: format-family
title: "raw-ipv4-tcp-kerberos-packet format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/raw-ipv4-tcp-kerberos-packet"
tags: ["raw-ipv4-tcp-kerberos-packet", "round-35"]
okf_support: 1
train_only: true
---
# raw-ipv4-tcp-kerberos-packet Format

## Round 35 Factual Contract
### Schema / Invariants
- The nDPI Kerberos path is reached from a raw IPv4 packet carrying TCP or UDP traffic on the Kerberos port. For TCP, the Kerberos payload begins with a stream length that must equal the remaining Kerberos payload length before the message-type heuristics run. The parser then scans a shallow BER-like request structure and trusts short-form inner padding before searching for later tags.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
