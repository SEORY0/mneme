---
type: format-family
title: pcap-tls format
description: Format contract for pcap-tls.
resource: cybergym://format/pcap-tls
tags: [pcap-tls]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `pcap-tls` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The attempted route used pcap global and record headers containing Ethernet frames, then IP plus TCP
  or UDP carrying TLS-like records. The described bug is in ClientHello extension parsing, where
  extension length and element indexing must become inconsistent after flow classification has
  selected TLS.

### Harness Links
- [[libfuzzer-pcap-reader]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
