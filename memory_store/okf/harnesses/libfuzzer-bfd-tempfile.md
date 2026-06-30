---
type: harness-contract
title: "Libfuzzer BFD Tempfile Harness"
description: "Input contract facts for libfuzzer-bfd-tempfile."
tags: ["libfuzzer-bfd-tempfile", "round-27"]
okf_support: 1
---
# Libfuzzer BFD Tempfile Harness

## Round 27 Input Contract
- libFuzzer supplies raw bytes.
- The harness writes them unchanged to a temporary file, opens that file through BFD auto-detection, and asks BFD to check archive format.
- There is no selector byte and no FuzzedDataProvider carving.

## Round 27 Format Links
- [[vms-ia64-library-archive]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
