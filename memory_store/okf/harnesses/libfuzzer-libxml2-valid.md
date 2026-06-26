---
type: harness-contract
title: "Libfuzzer Libxml2 Valid harness"
description: "Input contract facts for Libfuzzer Libxml2 Valid."
tags: ["libfuzzer-libxml2-valid", "round-6"]
okf_support: 1
---
# Libfuzzer Libxml2 Valid Harness

## Round 6 Input Contract
- The harness reads integers from the front, forces DTD validation, installs a malloc-failure injector, parses the main entity through pull, post-validation, push, and reader paths, and then checks whether malloc failure was reported for selected parser operations.

## Format Links
- [[libxml2-valid-fuzzer-envelope]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
