---
type: harness-contract
title: "Afl Driver Libfuzzer Harness"
description: "Input contract facts for afl-driver-libfuzzer."
tags: ["afl-driver-libfuzzer", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Afl Driver Libfuzzer Harness

## Round 19 Input Contract

- The active FuzzJson harness passes the raw file buffer as a C string to libgps_json_unpack and json_toff_read. It does not append a terminator, so unterminated inputs can crash in parser boundary code before reaching the numeric invariant.
- Format link: [[gpsd-json]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
