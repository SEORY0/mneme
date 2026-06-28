---
type: harness-contract
title: "Libfuzzer Fuzzed Data Provider harness"
description: "Input contract facts for libfuzzer-fuzzed-data-provider."
tags: ["libfuzzer-fuzzed-data-provider", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Fuzzed Data Provider Harness

## Round 17 Input Contract
- The fuzzer builds an encoder configuration from provider-carved booleans and integers, creates the encoder, then loops while bytes remain.
- Each loop chooses either a front-consumed input vector or a scalar fill byte for the encoder input buffer.

## Round 17 Format Links
- [[libxaac-encoder-fuzzed-provider]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[libxaac-encoder-fuzzed-provider]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 25 Input Contract
- The libFuzzer target uses FuzzedDataProvider-style consumption for scalar controls and generated buffers. The effective image data is constructed in memory by the harness, so successful inputs must satisfy the harness control contract rather than file magic or container checks.

## Round 25 Format Links
- [[ultrahdr-encoder-frame]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
