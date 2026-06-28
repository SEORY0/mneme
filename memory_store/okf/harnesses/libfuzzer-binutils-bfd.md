---
type: harness-contract
title: "Libfuzzer Binutils BFD harness"
description: "Input contract facts for libfuzzer-binutils-bfd."
tags: ["libfuzzer-binutils-bfd", "round-15"]
okf_support: 1
---
# Libfuzzer Binutils BFD Harness

## Round 15 Input Contract
- The binutils task builds several libFuzzer targets over BFD-style object consumers. The relevant
  path writes the raw input as an object file and asks BFD/nm-style code to recognize and inspect it;
  there is no archive wrapper, text envelope, checksum, or FuzzedDataProvider contract.

## Format Links
- [[ecoff-bfd-object]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
