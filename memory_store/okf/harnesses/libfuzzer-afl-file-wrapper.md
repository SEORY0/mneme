---
type: harness-contract
title: "Libfuzzer Afl File Wrapper harness"
description: "Round 8 input contract facts for libfuzzer-afl-file-wrapper."
tags: ["libfuzzer-afl-file-wrapper", "round-8"]
okf_support: 1
---
# Libfuzzer Afl File Wrapper Harness

## Round 8 Input Contract
- The fuzz target writes the raw input bytes to a temporary file and calls gf_isom_open_file in read-dump mode, then closes the movie if opening succeeds. The input is a complete file image; there is no selector byte or FuzzedDataProvider carving.

## Round 8 Format Links
- [[isobmff]]

## Round 8 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

