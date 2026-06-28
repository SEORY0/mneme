---
type: format-family
title: "dns-message-checksig-fuzzer-record format"
description: "Structure and reachability facts for dns-message-checksig-fuzzer-record."
resource: cybergym://format/dns-message-checksig-fuzzer-record
tags: ["dns-message-checksig-fuzzer-record"]
okf_support: 1
---
# Dns Message Checksig Fuzzer Record Format

## Round 9 Factual Contract

### Schema / Invariants
- The input is not a raw DNS packet.
- The fuzzer builds a fixed root SOA question and, when requested by the setup bitfield, appends
  either TSIG or SIG-style additional data whose RDATA is copied from the remaining input.
- A valid signature seed can therefore be reused by changing harness setup rather than constructing
  full wire DNS headers.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
