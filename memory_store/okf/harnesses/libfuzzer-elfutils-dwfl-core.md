---
type: harness-contract
title: "Libfuzzer Elfutils Dwfl Core harness"
description: "Input contract facts for libfuzzer-elfutils-dwfl-core."
tags: ["libfuzzer-elfutils-dwfl-core", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Elfutils Dwfl Core Harness

## Round 17 Input Contract
- The dwfl core fuzzer writes raw libFuzzer bytes to a temporary file, opens it with libelf, reports the core to dwfl, and finalizes reporting.
- The input is a raw ELF-like file, not a FuzzedDataProvider stream.
- Official submit was used because the local Arvo verify mount convention did not match this image.

## Round 17 Format Links
- [[elf-core-note]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[elf-core-note]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
