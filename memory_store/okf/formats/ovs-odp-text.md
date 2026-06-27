---
type: format-family
title: ovs-odp-text format
description: Structure and reachability facts for ovs-odp-text inputs.
tags: [ovs-odp-text]
okf_support: 0
---
# Ovs Odp Text Format

## Round 10 Factual Contract

### Schema / Invariants
- The selected target consumes a single NUL-terminated OVS datapath text string. It rejects very short inputs, embedded newlines, and inputs without a trailing terminator. The same string is tried as an ODP key, wildcard key, and action list; nested attributes are expressed textually with parenthesized encap-style clauses.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
