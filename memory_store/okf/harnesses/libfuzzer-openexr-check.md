---
type: harness-contract
title: "Libfuzzer Openexr Check harness"
description: "Input contract facts for libfuzzer-openexr-check."
tags: ["libfuzzer-openexr-check", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer Openexr Check Harness

## Round 11 Input Contract
- The harness reads raw bytes as an EXR file and runs the exrcheck path over that file content. There is no mode selector or FuzzedDataProvider layout; the EXR header and chunk structure drive all parser decisions.

## Format Links
- [[openexr-dwa]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
