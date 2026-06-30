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

## Round 26 Factual Contract


### Input Contract
- The Wireshark fuzzshark target is configured for the IP dissector. It treats the input as one raw IPv4 packet and relies on protocol fields for nested dispatch; there is no pcap header, external capture wrapper, checksum repair requirement, or FuzzedDataProvider byte carving.

### Format Links
- [[ipv4-gre-ieee80211-amsdu]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 28 Input Contract

- The image is configured as fuzzshark_ip. libFuzzer supplies the raw file bytes directly to Wireshark's frame dissector, and the selected IP dissector is run as a postdissector. The input is therefore a raw IPv4 packet; there is no pcap global header, no pcap record header, and no FuzzedDataProvider carving.

## Round 28 Format Links
- [[raw-ipv4-tcp-rtitcp-rtps]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 30 Input Contract

### Input Contract
- The fuzzshark IP target registers the IP dissector and feeds libFuzzer bytes as one synthetic packet. There is no pcap envelope, mode byte, checksum repair requirement, or FuzzedDataProvider split; nested dispatch is controlled by the IP protocol, UDP service, GSMTAP metadata, and RLC/MAC control bits.

### Format Links
- [[wireshark-fuzzshark-ip-gsmtap-rlcmac]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
