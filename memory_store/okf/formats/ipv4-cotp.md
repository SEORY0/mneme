---
type: format-family
title: ipv4-cotp format
description: Structure and reachability facts for ipv4-cotp inputs.
tags: [ipv4-cotp]
okf_support: 0
---
# Ipv4 Cotp Format

## Round 10 Factual Contract

### Schema / Invariants
- COTP data packets use a length indicator followed by a TPDU type and sequence/control byte; CR and CC packets include reference fields and may carry user data after the variable part. In the IP harness, OSI transport is reached through IPv4 protocol dispatch rather than raw COTP bytes.

### Harness Links
- [[libfuzzer-fuzzshark-ip]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
