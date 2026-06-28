---
type: harness-contract
title: "Libfuzzer Raw JSON Bytes harness"
description: "Input contract facts for Libfuzzer Raw JSON Bytes."
tags: ["libfuzzer-raw-json-bytes", "round-6"]
okf_support: 1
---
# Libfuzzer Raw JSON Bytes Harness

## Round 6 Input Contract
- The libplist jplist fuzzer passes the full raw byte buffer directly to plist_from_json. There is no mode selector, back-consumed size field, or filename-based format gate.

## Format Links
- [[json]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
