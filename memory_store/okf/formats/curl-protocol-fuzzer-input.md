---
type: format-family
title: curl-protocol-fuzzer-input format
description: Structure and reachability facts for curl-protocol-fuzzer-input inputs.
tags: [curl-protocol-fuzzer-input]
okf_support: 0
---
# Curl Protocol Fuzzer Input Format

## Round 10 Factual Contract

### Schema / Invariants
- The input is not a full network transcript by itself; the fuzzer interprets raw bytes as protocol-specific curl stimulus and then drives an FTP-oriented transfer/disconnect path internally. URL-like protocol selection alone is accepted but is not sufficient to force the target teardown edge.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
