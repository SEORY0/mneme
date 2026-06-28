---
type: harness-contract
title: "Afl File Fuzzer harness"
description: "Input contract facts for afl-file-fuzzer."
tags: ["afl-file-fuzzer", "round-9"]
okf_support: 3
---
# Afl File Fuzzer Harness

## Round 9 Input Contract
- The AFL-style wrapper writes the raw bytes to a temporary config file and calls the Net-SNMP
  read_config path.
- There is no front selector and no FuzzedDataProvider layout; line/token syntax determines the
  parser branch.
- The wrapper reads raw file bytes from disk, initializes libdwarf on that file, repeatedly changes
  frame-rule defaults, and reads both .debug_frame and .eh_frame.
- There is no selector byte or FuzzedDataProvider carving.
- The AFL wrapper feeds the raw file bytes to the OpenSSL server fuzzer.
- There is no extra prefix; the fuzzer initializes a server context with built-in credentials and
  drives the first part of the server handshake from the supplied TLS records.

## Round 9 Format Links
- [[dwarf-object-debug-file]]
- [[net-snmp-config-text]]
- [[tls-clienthello-stream]]

## Round 9 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
