---
type: harness-contract
title: "Libfuzzer OTS harness"
description: "Input contract facts for libfuzzer-ots."
tags: ["libfuzzer-ots", "round-20"]
okf_support: 1
---
# Libfuzzer OTS Harness

## Round 20 Input Contract
- The OTS fuzzer consumes raw font bytes. A structurally valid sfnt wrapper is important because OTS validates table directories before reaching table-specific sanitizers; mutating a real valid font is much more reliable than hand-building only the STAT table.

## Round 20 Format Links
- [[opentype-font]]

## Round 20 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
