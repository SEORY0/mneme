---
type: harness-contract
title: "Libfuzzer Qpdf Harness"
description: "Round 26 input contract facts for libfuzzer-qpdf."
tags: ["libfuzzer-qpdf", "round-26"]
okf_support: 10
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

## Round 27 Input Contract
- The qpdf libFuzzer target consumes raw PDF bytes through a buffer-backed input source.
- It parses the PDF, creates a writer with full stream decode enabled, disables object streams, applies insecure R3 output encryption, and writes to a discard pipeline.
- There is no leading selector byte or FuzzedDataProvider carving.

## Round 27 Format Links
- [[pdf-encrypt-dictionary]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
