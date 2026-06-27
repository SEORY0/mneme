---
type: harness-contract
title: "Afl Libfuzzer Compatible harness"
description: "Input contract facts for afl-libfuzzer-compatible."
tags: ["afl-libfuzzer-compatible"]
okf_support: 0
---
# Afl Libfuzzer Compatible Harness

## Round 10 Input Contract
- The first input byte selects a handshake stage when the build does not force one. The harness internally opens an SCTP client, injects canned peer handshake packets, prepends a common header with the captured verification tag to the remaining fuzz bytes, and then feeds that packet to usrsctp.

## Round 10 Format Links
- [[sctp-packet]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 19 Input Contract

- The fuzzshark binary reads a packet-capture input file and was configured at runtime for a UDP dissector under an IP protocol table. It disables unrelated dissectors before processing the file. The input is not a bare protocol payload.
- Format link: [[pcap-udp-packet]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
