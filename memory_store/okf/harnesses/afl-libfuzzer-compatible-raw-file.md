---
type: harness-contract
title: "Afl Libfuzzer Compatible Raw File harness"
description: "Input contract facts for afl-libfuzzer-compatible-raw-file."
tags: ["afl-libfuzzer-compatible-raw-file"]
okf_support: 1
---
# Afl Libfuzzer Compatible Raw File Harness

## Round 10 Input Contract
- The target reads a whole raw file buffer up to its size cap, calls open_buffer, calls unpack, then iterates through several processing quality modes. The built target reports AFL-style single-file execution but still runs the same fuzzer entry point.

## Round 10 Format Links
- [[camera-raw]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 32 Input Contract
- The fuzz target consumes the submitted bytes as one C string. It rejects inputs that are too short, lack a trailing terminator, or contain a newline. The accepted string is sent through expression parsing, action parsing, lexer formatting, and packet conversion; there is no FuzzedDataProvider carving.

## Round 32 Format Links
- [[openvswitch-expression]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
