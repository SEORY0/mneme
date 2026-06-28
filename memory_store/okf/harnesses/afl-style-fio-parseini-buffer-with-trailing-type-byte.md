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
