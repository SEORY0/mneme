---
type: harness-contract
title: "Libfuzzer Fuzzshark Ip harness"
description: "Input contract facts for libfuzzer-fuzzshark-ip."
tags: ["libfuzzer-fuzzshark-ip"]
okf_support: 0
---
# Libfuzzer Fuzzshark Ip Harness

## Round 10 Input Contract
- The fuzzshark target consumes raw IPv4 packet bytes and configures the IP dissector. Protocol-specific payloads must be wrapped in an IP header with the correct next-protocol value; direct protocol fragments are ignored as malformed IP.

## Round 10 Format Links
- [[ipv4-cotp]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
