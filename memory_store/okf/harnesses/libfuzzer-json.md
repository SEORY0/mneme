---
type: harness-contract
title: "Libfuzzer Json harness"
description: "Input contract facts for libfuzzer-json."
tags: ["libfuzzer-json"]
okf_support: 0
---
# Libfuzzer Json Harness

## Round 10 Input Contract
- The fuzzer consumes raw JSON bytes, parses them into a Unit configuration object, then validates the configuration. There is no outer file wrapper; schema validity is needed before templated-string validation is reached.

## Round 10 Format Links
- [[unit-json-config]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
