---
type: harness-contract
title: "Libfuzzer Qpdf Harness"
description: "Round 26 input contract facts for libfuzzer-qpdf."
tags: ["libfuzzer-qpdf", "round-26"]
okf_support: 1
train_only: true
---
# Libfuzzer Qpdf Harness

## Round 26 Factual Contract

### Input Contract
- The qpdf fuzz target consumes raw PDF bytes through a buffer-backed input source. There is no leading selector or FuzzedDataProvider layout; object creation parses startxref and xref data before later page or outline checks.

### Format Links
- [[pdf]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
