---
type: harness-contract
title: "Libfuzzer Libarchive harness"
description: "Input contract facts for libfuzzer-libarchive."
tags: ["libfuzzer-libarchive"]
okf_support: 0
---
# Libfuzzer Libarchive Harness

## Round 10 Input Contract
- The libarchive fuzzer feeds the raw input as an archive byte stream with all read formats enabled. A candidate must be a whole ISO image; the parser performs archive format detection before reaching ISO directory traversal.

## Round 10 Format Links
- [[iso9660]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
