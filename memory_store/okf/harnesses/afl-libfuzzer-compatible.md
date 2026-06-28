---
type: harness-contract
title: "Afl Libfuzzer Compatible harness"
description: "Input contract facts for afl-libfuzzer-compatible."
tags: ["afl-libfuzzer-compatible"]
okf_support: 1
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

## Round 21 Input Contract (rawspeed-panasonic-fuzzer-record)

- Raw bytes are consumed front-to-back by helper reads; there is no file magic. The trailing region is passed as a byte stream to the Panasonic decompressor after the metadata fields are consumed.

## Round 21 Format Links (rawspeed-panasonic-fuzzer-record)
- [[rawspeed-panasonic-fuzzer-record]]

## Round 21 Notes (rawspeed-panasonic-fuzzer-record)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
