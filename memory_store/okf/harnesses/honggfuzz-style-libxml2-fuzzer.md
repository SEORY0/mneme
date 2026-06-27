---
type: harness-contract
title: "Honggfuzz Style Libxml2 Fuzzer harness"
description: "Input contract facts for honggfuzz-style-libxml2-fuzzer."
tags: ["honggfuzz-style-libxml2-fuzzer", "round-20"]
okf_support: 1
---
# Honggfuzz Style Libxml2 Fuzzer Harness

## Round 20 Input Contract
- The harness reads scalar parser options from the front, installs an in-memory entity loader, then parses the main document through several libxml2 entry points. XInclude processing is gated by parser-option bits; external include text must be supplied as a later entity in the same fuzz stream.

## Round 20 Format Links
- [[libxml2-entity-stream]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
