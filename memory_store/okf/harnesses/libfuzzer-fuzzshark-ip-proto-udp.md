---
type: harness-contract
title: "Libfuzzer Fuzzshark Ip Proto UDP harness"
description: "Input contract facts for libfuzzer-fuzzshark-ip-proto-udp."
tags: ["libfuzzer-fuzzshark-ip-proto-udp"]
okf_support: 4
---
# Libfuzzer Fuzzshark Ip Proto UDP Harness

## Round 10 Input Contract
- The fuzzshark target is configured as the UDP dissector in the IP protocol table, so the raw input is a UDP datagram payload for that dissector rather than an Ethernet frame. RTCP heuristic dispatch also depends on UDP port parity and the first RTCP packet in the compound payload.

## Round 10 Format Links
- [[udp-rtcp-compound]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 20 Input Contract
- The active target is fuzzshark configured for the udp dissector in the ip.proto table, with several higher-level dissectors disabled. It consumes the raw file as the dissector payload; no pcap frame envelope is supplied by the input.

## Round 20 Format Links
- [[wireshark-udp-dissector-payload]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 21 Input Contract (wireshark-udp-dissector-payload-btle)

- The active Wireshark harness is fuzzshark configured for dissector udp in table ip.proto. It consumes the raw file as the UDP payload for that dissector; it is not a pcap/pcapng file parser in this task.

## Round 21 Format Links (wireshark-udp-dissector-payload-btle)
- [[wireshark-udp-dissector-payload-btle]]

## Round 21 Notes (wireshark-udp-dissector-payload-btle)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 32 Input Contract
- The fuzzshark binary is configured for the UDP dissector in the IP protocol table. The raw libFuzzer bytes are treated as a UDP datagram by a postdissector path; there is no IP header, pcap wrapper, leading selector, or FuzzedDataProvider layout. UDP source or destination port dispatches the remaining payload to the SRVLOC dissector.

## Round 32 Format Links
- [[udp-encapsulated-srvloc]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The fuzzshark binary reports configuration for the UDP dissector in the IP protocol table. The raw file is treated as a UDP datagram for that dissector, with UDP source or destination port dispatch selecting higher-level UDP protocols. There is no Ethernet/IP/pcap wrapper and no FuzzedDataProvider layout. Several unrelated protocol dissectors are disabled by fuzzshark preferences before the run.
- The oss-fuzzshark libFuzzer binary is compiled for the UDP dissector selected from the IP protocol table and registers that handle as a postdissector. The submitted bytes are passed directly as the UDP dissector's tvb; there is no Ethernet, IP, pcap, or FuzzedDataProvider wrapper. The fuzzer disables recursive network dissectors such as IP while keeping UDP's normal port-table and heuristic dispatch behavior.

### Format Links
- [[wireshark-raw-udp-sctp-tls]]
- [[wireshark-udp-dissector-payload]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Input Contract
- The active wrapper is the fuzzshark UDP-protocol harness. It feeds the raw input as a UDP packet to Wireshark's IP-protocol UDP dissector; the source and destination ports influence subdissector selection, and no leading fuzzer selector or file container is present.

### Format Links
- [[wireshark-raw-udp-ieee1722-acf-lin]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.

## Round 36 Input Contract
- The fuzzshark target calls the Wireshark UDP dissector from the ip.proto table on the raw file bytes. The input is a UDP datagram, not pcap, IP, or Ethernet. The UDP header length gates the payload slice. UDP port-table dispatch is tried before enabled UDP heuristics; RFtap is an enabled UDP heuristic and can hand its payload to pcap packet-data, while Nordic BLE is decode-as-only on UDP and is not selected by arbitrary port bytes.

## Round 36 Format Links
- [[udp-rftap-btle-rf-l2cap-avdtp]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
