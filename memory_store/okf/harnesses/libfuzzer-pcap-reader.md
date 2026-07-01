---
type: harness-contract
title: "Libfuzzer Pcap Reader harness"
description: "Input contract facts for libfuzzer-pcap-reader."
tags: ["libfuzzer-pcap-reader", "round-15"]
okf_support: 1
---
# Libfuzzer Pcap Reader Harness

## Round 15 Input Contract
- The active nDPI harness writes the raw fuzzer buffer to a temporary capture file, opens it with
  pcap, iterates captured packets, copies each packet to a heap buffer, and passes packets into the
  nDPI workflow. It is not a raw packet-only or FuzzedDataProvider harness.

## Format Links
- [[pcap-tls]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 17 Input Contract
- The harness writes raw fuzzer bytes to a temporary PCAP file, opens it with libpcap, copies each captured packet into an exactly sized heap buffer, and passes the packet to nDPI workflow processing.

## Round 17 Format Links
- [[pcap-ipv4-udp-bittorrent]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[pcap-ipv4-udp-bittorrent]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 35 Input Contract

### Input Contract
- The fuzz target writes the raw input bytes to a temporary PCAP file, opens it with pcap_open_offline, iterates packet records, copies each captured packet to a heap buffer, and passes the packet header plus copied bytes into ndpi_workflow_process_packet. There is no FuzzedDataProvider carving; malformed non-PCAP bytes do not reach the TLS parser.

### Format Links
- [[pcap-ethernet-ipv4-tcp-tls-clienthello]]

### Notes
- These facts are descriptive harness-carving observations from round 35; they carry no success-rate claim.
