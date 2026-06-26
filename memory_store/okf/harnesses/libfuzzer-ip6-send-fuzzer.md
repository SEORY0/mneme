---
type: harness-contract
title: "Libfuzzer Ip6 Send Fuzzer harness"
description: "Input contract facts for Libfuzzer Ip6 Send Fuzzer."
tags: ["libfuzzer-ip6-send-fuzzer", "round-6"]
okf_support: 1
---
# Libfuzzer Ip6 Send Fuzzer Harness

## Round 6 Input Contract
- `ip6_send` consumes raw libFuzzer bytes; byte zero controls link-security settings and bytes after it become the outbound IPv6 message payload. There is no pcap, file header, or CLI argv envelope in this selected harness.

## Format Links
- [[openthread-ip6-message]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
