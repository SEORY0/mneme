---
type: harness-contract
title: "Libfuzzer Tempfile BFD harness"
description: "Input contract facts for libfuzzer-tempfile-bfd."
tags: ["libfuzzer-tempfile-bfd"]
okf_support: 0
---
# Libfuzzer Tempfile BFD Harness

## Round 10 Input Contract
- The fuzzer writes the raw input to a temporary file, opens it with BFD auto-detection, and checks archive format. Inputs must therefore be complete file bytes, not an in-memory record stream.

## Round 10 Format Links
- [[bfd-archive-containing-truncated-msdos-member]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
