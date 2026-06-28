---
type: harness-contract
title: "Honggfuzz Libfuzzer Style Reader Fuzzer harness"
description: "Input contract facts for honggfuzz/libfuzzer-style reader fuzzer."
tags: ["honggfuzz-libfuzzer-style-reader-fuzzer", "round-22"]
okf_support: 1
---
# Honggfuzz Libfuzzer Style Reader Fuzzer Harness

## Round 22 Input Contract
- The harness installs a fake OpenSC reader, connects a card, binds PKCS#15, then consumes additional chunks for cryptographic operation inputs. LibFuzzer bytes are not a file format; they are a simulated smart-card conversation consumed front to back.

## Format Links
- [[opensc-fuzz-reader-chunks]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
