---
type: harness-contract
title: "Fuzztest Libfuzzer Bridge harness"
description: "Input contract facts for Fuzztest Libfuzzer Bridge."
tags: ["fuzztest-libfuzzer-bridge", "round-21"]
okf_support: 1
---
# Fuzztest Libfuzzer Bridge Harness

## Round 21 Input Contract (fuzztest-encoded-image-case)

- The observed runner is a FuzzTest-based libFuzzer bridge for Enc.EncTest. It does not treat the input as raw image bytes; invalid testcase serialization is rejected with an unexpected-format message before image decoding.

## Round 21 Format Links (fuzztest-encoded-image-case)
- [[fuzztest-encoded-image-case]]

## Round 21 Notes (fuzztest-encoded-image-case)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
