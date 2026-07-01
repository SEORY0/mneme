---
type: harness-contract
title: "Libfuzzer Fuzzshark Ip harness"
description: "Input contract facts for libfuzzer-fuzzshark-ip."
tags: ["libfuzzer-fuzzshark-ip"]
okf_support: 4
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

## Round 32 Input Contract
- The oss-fuzzshark wrapper is configured for the ip dissector and feeds the entire file as one raw frame buffer with unknown outer encapsulation. There is no corpus directory, no FuzzedDataProvider layout, and no capture-file wrapper; secondary dispatch depends on the packet headers and dissector tables reached from the raw IPv4 frame.

## Round 32 Format Links
- [[raw-ipv4-udp-dof-packet]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The fuzzshark target is configured for the IP dissector. The PoC file bytes are fed directly as one raw IPv4 packet; there is no pcap wrapper, no stdin line protocol beyond the raw file, and no FuzzedDataProvider front/back carving. Nested dispatch depends on the IPv4 protocol field, TCP payload, and RTI-TCP/RTPS magic and length fields.
- The fuzz target feeds the entire file as one packet to the Wireshark IP dissector. There is no FuzzedDataProvider, no length prefix outside the packet headers, and no capture-file envelope. Packet-level lengths must be coherent enough for IP and UDP to reach the selected application dissector.
- The libFuzzer input is consumed as raw packet bytes by fuzzshark_ip. There is no FuzzedDataProvider, no leading mode selector, and no pcap reader in this path. The IP dissector is registered as a postdissector over the full input buffer, so nested protocols must be carried by a valid raw IP packet and then dispatched through normal IP, TCP, and dissector-table routing.

### Format Links
- [[raw-ipv4-tcp-kdsp-radiotap]]
- [[raw-ipv4-tcp-rtitcp-rtps]]
- [[raw-ipv4-udp-snmp-ber]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
