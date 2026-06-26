---
type: harness-contract
title: "Libfuzzer Ucasemap Fuzzer harness"
description: "Input contract facts for Libfuzzer Ucasemap Fuzzer."
tags: ["libfuzzer-ucasemap-fuzzer", "round-6"]
okf_support: 1
---
# Libfuzzer Ucasemap Fuzzer Harness

## Round 6 Input Contract
- The first byte selects lower/upper/title/fold, the next selector chooses one ICU locale, the next option word is passed to UCaseMap open, and the remaining bytes are copied as UTF-8 source. The destination capacity is derived from the remaining byte count.

## Format Links
- [[icu-ucasemap-fuzzer-bytes]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
