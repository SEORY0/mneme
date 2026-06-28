---
type: format-family
title: udp-rtcp-compound format
description: Structure and reachability facts for udp-rtcp-compound inputs.
tags: [udp-rtcp-compound]
okf_support: 0
---
# UDP RTCP Compound Format

## Round 10 Factual Contract

### Schema / Invariants
- RTCP over UDP uses UDP port heuristics and compound RTCP framing. Transport-wide feedback carries sender/source identifiers, a base sequence, a packet-status count, reference time, feedback count, packet-status chunks, and receive deltas. Status-vector or run-length chunks can describe more packet states than the count field if not validated.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
