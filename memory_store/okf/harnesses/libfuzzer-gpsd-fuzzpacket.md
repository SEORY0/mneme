---
type: harness-contract
title: "Libfuzzer Gpsd Fuzzpacket harness"
description: "Input contract facts for libfuzzer-gpsd-fuzzpacket."
tags: ["libfuzzer-gpsd-fuzzpacket", "round-24"]
okf_support: 1
---
# Libfuzzer Gpsd Fuzzpacket Harness

## Round 24 Factual Contract

### Input Contract
- The fuzzer requires a minimum input size, copies raw bytes into the lexer input buffer, calls packet_parse once, then repeats with packet_get on a null file descriptor until no more packet is returned.

### Format Links
- [[gpsd-raw-packet-stream]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 29 Input Contract

- The libFuzzer target requires a minimum input size and rejects overly large files. It treats the input as raw bytes with no mode selector and no FuzzedDataProvider splitting. The harness copies all bytes into the lexer input buffer, calls packet_parse once, then reinitializes the lexer and repeatedly calls packet_get on the same buffered bytes with a null file descriptor until packet_get returns no further packet.

## Round 29 Format Links
- [[gpsd-raw-packet-stream]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
