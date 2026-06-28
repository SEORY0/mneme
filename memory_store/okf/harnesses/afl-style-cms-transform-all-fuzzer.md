---
type: harness-contract
title: "Afl Style Cms Transform All Fuzzer harness"
description: "Input contract facts for AFL-style cms_transform_all_fuzzer."
tags: ["afl-style-cms-transform-all-fuzzer", "round-16"]
okf_support: 1
---
# Afl Style Cms Transform All Fuzzer Harness

## Round 16 Input Contract
- The wrapper uses the cms_transform_all harness. It does not run pixel transformation; it opens both profiles from memory and calls cmsCreateTransform with the front-loaded format words, then deletes the transform if creation succeeds.

## Round 16 Format Links
- [[lcms-transform-fuzzer-input-with-icc-profiles]]

## Round 16 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
