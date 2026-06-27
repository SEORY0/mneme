---
type: harness-contract
title: "Honggfuzz Libfuzzer Wrapper Harness"
description: "Input contract facts for honggfuzz/libfuzzer-wrapper."
tags: ["honggfuzz-libfuzzer-wrapper", "round-12"]
okf_support: 0
train_only: true
---
# Honggfuzz Libfuzzer Wrapper Harness

## Round 12 Input Contract
- The OpenSC pkcs15 reader harness installs a fuzz reader, connects using the first chunk as the card ATR, then services reader transmit calls from later chunks. It binds a PKCS15 card and drives reader operations from the chunk stream; it is not a raw ASN.1 file parser.
- The wrapper runs snmp_api_fuzzer. The fuzzer first calls agentx_parse on the raw bytes, then uses helper functions that carve fixed-size chunks from the front, adds a variable to a PDU, optionally builds it, parses another SNMP message, and builds the parsed PDU.

## Round 12 Format Links
- [[net-snmp-api-fuzzer-stream]]
- [[opensc-pkcs15-reader-chunk-stream]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
