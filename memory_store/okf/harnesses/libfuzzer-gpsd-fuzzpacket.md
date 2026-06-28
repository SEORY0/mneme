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
