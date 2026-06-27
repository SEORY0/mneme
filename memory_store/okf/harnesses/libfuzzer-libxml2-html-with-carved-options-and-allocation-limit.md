---
type: harness-contract
title: "Libfuzzer Libxml2 Html With Carved Options And Allocation Limit harness"
description: "Input contract facts for libfuzzer-libxml2-html-with-carved-options-and-allocation-limit."
tags: ["libfuzzer-libxml2-html-with-carved-options-and-allocation-limit", "round-20"]
okf_support: 1
---
# Libfuzzer Libxml2 Html With Carved Options And Allocation Limit Harness

## Round 20 Input Contract
- The harness reads four bytes of options, four bytes of max allocation modulo input size, then treats the remaining bytes as the HTML document. It exercises both pull parsing and push parsing in fixed-size chunks under the same allocation limit.

## Round 20 Format Links
- [[libxml2-html-fuzzer-input]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
