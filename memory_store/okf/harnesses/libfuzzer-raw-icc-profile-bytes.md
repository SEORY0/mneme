---
type: harness-contract
title: "Libfuzzer Raw ICC Profile Bytes harness"
description: "Input contract facts for Libfuzzer Raw ICC Profile Bytes."
tags: ["libfuzzer-raw-icc-profile-bytes", "round-6"]
okf_support: 1
---
# Libfuzzer Raw ICC Profile Bytes Harness

## Round 6 Input Contract
- The Serenity ICC fuzzer passes the raw bytes directly to the ICC profile loader. No selector bytes are consumed; all reachability depends on the ICC header and tag-table consistency.

## Format Links
- [[icc-profile]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
