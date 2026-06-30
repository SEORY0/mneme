---
type: harness-contract
title: "Libfuzzer ICU Time Zone Names Harness"
description: "Input contract facts for libfuzzer-icu-time-zone-names."
tags: ["libfuzzer-icu-time-zone-names", "round-27"]
okf_support: 1
---
# Libfuzzer ICU Time Zone Names Harness

## Round 27 Input Contract
- The scoring wrapper runs the ICU time_zone_names_fuzzer.
- It consumes raw bytes directly with fixed front fields and UTF-16 tail data; there is no FuzzedDataProvider and no calendar operation stream.
- Calendar-style records do not exercise this active wrapper.

## Round 27 Format Links
- [[icu-time-zone-names-fuzzer-record]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
