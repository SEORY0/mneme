---
type: harness-contract
title: "Libfuzzer Binpolicy harness"
description: "Input contract facts for libfuzzer-binpolicy."
tags: ["libfuzzer-binpolicy", "round-15"]
okf_support: 1
---
# Libfuzzer Binpolicy Harness

## Round 15 Input Contract
- The binpolicy fuzzer passes raw input bytes as a memory-backed policy_file to policydb_read. If
  parsing succeeds it loads initial SIDs, may optimize kernel policies, writes the binary policy to a
  sink, and converts the kernel policy to conf and CIL. There is no command-line envelope or
  FuzzedDataProvider layout.

## Format Links
- [[selinux-binary-policy]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
