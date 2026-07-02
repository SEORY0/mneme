---
type: harness-contract
title: "Afl Style Fio Parseini Buffer With Trailing Type Byte harness"
description: "Input contract facts for afl-style-fio-parseini-buffer-with-trailing-type-byte."
tags: ["afl-style-fio-parseini-buffer-with-trailing-type-byte", "round-20"]
okf_support: 1
---
# Afl Style Fio Parseini Buffer With Trailing Type Byte Harness

## Round 20 Input Contract
- The fuzzer copies all but the final input byte into a NUL-terminated ini buffer, initializes fio parse-only mode once, and passes the final byte as the parse_jobs_ini client/type argument.

## Round 20 Format Links
- [[fio-ini-job-file]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
## Round 37 Input Contract

### Input Contract
- The fuzz harness initializes fio in parse-only mode, copies all input bytes except the final byte into a NUL-terminated in-memory ini buffer, and passes the final byte as the parse_jobs_ini client/type argument.
- There is no FuzzedDataProvider layout or checksum; the only carving is the trailing type byte.

### Format Links
- [[fio-ini-job-file]]

### Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
