---
type: harness-contract
title: "Libfuzzer Wrapper File Contract Mismatch harness"
description: "Round 8 input contract facts for libfuzzer-wrapper-file-contract-mismatch."
tags: ["libfuzzer-wrapper-file-contract-mismatch", "round-8"]
okf_support: 1
---
# Libfuzzer Wrapper File Contract Mismatch Harness

## Round 8 Input Contract
- The intended fuzzer reads raw bytes front-to-back from a memory stream, but the benchmark wrapper invokes the libFuzzer binary with a regular file path in a way this target interprets as a required corpus directory. No candidate file reached LLVMFuzzerTestOneInput in local verification.

## Round 8 Format Links
- [[libheif-color-conversion-raw]]

## Round 8 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

