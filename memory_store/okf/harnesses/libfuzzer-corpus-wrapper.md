---
type: harness-contract
title: "Libfuzzer Corpus Wrapper harness"
description: "Input contract facts for libfuzzer-corpus-wrapper."
tags: ["libfuzzer-corpus-wrapper", "round-25"]
okf_support: 0
---
# Libfuzzer Corpus Wrapper Harness

## Round 25 Input Contract
- The observed wrapper did not feed raw file bytes to LLVMFuzzerTestOneInput. It treated the submitted path as a corpus directory; raw fonts and a zipped corpus were rejected before parser entry.
- The observed wrapper did not pass raw bytes to LLVMFuzzerTestOneInput. It emitted a required-directory error for both file and directory-path attempts under the local verify surface.

## Round 25 Format Links
- [[opentype-font-corpus]]
- [[avc-encoder-control-and-raw-frames]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
