---
type: harness-contract
title: "Afl Libfuzzer Raw File harness"
description: "Input contract facts for afl-libfuzzer-raw-file."
tags: ["afl-libfuzzer-raw-file", "round-28"]
okf_support: 0
---
# Afl Libfuzzer Raw File Harness

## Round 28 Input Contract

- The AFL/libFuzzer wrapper reads the raw file bytes, NUL-terminates them with g_strndup, passes the whole string to g_date_time_new_from_iso8601, and if parsing returns a GDateTime it immediately calls g_date_time_format_iso8601. There is no mode byte, FuzzedDataProvider layout, checksum, or container envelope.

## Round 28 Format Links
- [[iso8601-datetime-text]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
