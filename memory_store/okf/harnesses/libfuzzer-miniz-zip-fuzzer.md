---
type: harness-contract
title: "Libfuzzer Miniz Zip Fuzzer harness"
description: "Input contract facts for libfuzzer-miniz-zip-fuzzer."
tags: ["libfuzzer-miniz-zip-fuzzer", "round-20"]
okf_support: 1
---
# Libfuzzer Miniz Zip Fuzzer Harness

## Round 20 Input Contract
- The active zip_fuzzer consumes the raw archive bytes directly. It opens the in-memory ZIP, validates file headers and file contents, and extracts member data; there is no leading selector or FuzzedDataProvider layout.

## Round 20 Format Links
- [[zip]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
