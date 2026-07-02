---
type: harness-contract
title: "Libfuzzer Cms Transform All Fuzzer Harness"
description: "Input contract facts for libfuzzer-cms-transform-all-fuzzer."
tags: ["libfuzzer-cms-transform-all-fuzzer", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Cms Transform All Fuzzer Harness

## Round 30 Input Contract

### Input Contract
- The selected LittleCMS fuzz target consumes the leading control words as input format, output format, flags, and intent selector. It splits the remaining bytes into two halves, opens both halves with cmsOpenProfileFromMem, calls cmsCreateTransform, and deletes the transform if one is created. There is no FuzzedDataProvider carving.

### Format Links
- [[lcms-transform-fuzzer-input-with-icc-profiles]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
