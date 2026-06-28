---
type: harness-contract
title: "Libfuzzer Libical Parse String harness"
description: "Input contract facts for libfuzzer-libical-parse-string."
tags: ["libfuzzer-libical-parse-string", "round-20"]
okf_support: 1
---
# Libfuzzer Libical Parse String Harness

## Round 20 Input Contract
- The active libical target copies raw input bytes into a NUL-terminated string and calls the string parser. There is no filename, multi-file container, leading selector, or FuzzedDataProvider layout.

## Round 20 Format Links
- [[icalendar]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
