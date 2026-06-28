---
type: harness-contract
title: "Libfuzzer Or Wrapper Selected Libxml2 Fuzzer harness"
description: "Input contract facts for libfuzzer-or-wrapper-selected-libxml2-fuzzer."
tags: ["libfuzzer-or-wrapper-selected-libxml2-fuzzer", "round-25"]
okf_support: 0
---
# Libfuzzer Or Wrapper Selected Libxml2 Fuzzer Harness

## Round 25 Input Contract
- The valid fuzzer reads front-carved integers, forces DTD validation, installs the fuzz entity loader, then parses the main entity through pull, post-validation, push, and reader paths while optionally injecting malloc failures. The useful XML bytes are inside the first entity content, not raw at file start.

## Round 25 Format Links
- [[libxml2-valid-fuzzer-envelope]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
