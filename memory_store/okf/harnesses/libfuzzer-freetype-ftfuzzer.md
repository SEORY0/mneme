---
type: harness-contract
title: "Libfuzzer Freetype Ftfuzzer harness"
description: "Input contract facts for libfuzzer-freetype-ftfuzzer."
tags: ["libfuzzer-freetype-ftfuzzer", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Freetype Ftfuzzer Harness

## Round 11 Input Contract
- The FreeType fuzzer consumes raw font bytes, and can also process archive-style multi-file inputs in other cases. For this target path there is no front selector byte; parser reachability depends on the font container and table-directory consistency.

## Format Links
- [[cff2-opentype-variable-font]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
