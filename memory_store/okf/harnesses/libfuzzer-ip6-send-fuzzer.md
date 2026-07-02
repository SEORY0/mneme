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

## Round 34 Factual Contract

### Input Contract
- The ip6-send libFuzzer harness consumes raw bytes with no file envelope. The first byte is a link-security selector and is not part of the IPv6 datagram; all remaining bytes are appended as the outbound IPv6 message and passed to otIp6Send on an initialized leader instance. The carrier therefore needs internally consistent IPv6 payload length, UDP length, CoAP options, and MeshCoP payload layout; there is no FuzzedDataProvider front/back split.

### Format Links
- [[ipv6-udp-coap-meshcop-tlv]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
