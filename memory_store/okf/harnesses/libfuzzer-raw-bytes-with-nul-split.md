---
type: harness-contract
title: "Libfuzzer Raw Bytes With Nul Split harness"
description: "Input contract facts for libfuzzer-raw-bytes-with-nul-split."
tags: ["libfuzzer-raw-bytes-with-nul-split", "round-24"]
okf_support: 1
---
# Libfuzzer Raw Bytes With Nul Split Harness

## Round 24 Factual Contract

### Input Contract
- Raw bytes are scanned for the first NUL byte. The prefix is parsed as WKT and the suffix beginning at that NUL byte is parsed as WKB; if both geometries parse, the harness runs intersection, difference, union, and serialization/destruction paths.

### Format Links
- [[wkt-plus-wkb-split-stream]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
