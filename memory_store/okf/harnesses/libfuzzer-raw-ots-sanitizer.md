---
type: harness-contract
title: "Libfuzzer Raw Ots Sanitizer harness"
description: "Input contract facts for Libfuzzer Raw Ots Sanitizer."
tags: ["libfuzzer-raw-ots-sanitizer", "round-21"]
okf_support: 1
---
# Libfuzzer Raw Ots Sanitizer Harness

## Round 21 Input Contract (opentype-font)

- The OTS fuzzer consumes raw font bytes with no selector. It sanitizes the input into an expanding memory stream; if the input is a font collection, it also iterates contained fonts after an initial successful process call.

## Round 21 Format Links (opentype-font)
- [[opentype-font]]

## Round 21 Notes (opentype-font)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
