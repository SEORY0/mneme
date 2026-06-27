---
type: harness-contract
title: "Afl Libfuzzer File Harness"
description: "Input contract facts for afl-libfuzzer-file."
tags: ["afl-libfuzzer-file", "harness-contract", "round-19"]
okf_support: 0
train_only: true
---

# Afl Libfuzzer File Harness

## Round 19 Input Contract

- The libarchive fuzzer reads the raw input bytes as an archive file, enables all filters and formats, iterates entries, and drains entry data. There is no mode byte or FuzzedDataProvider carving; success depends on the archive parser accepting the RAR5 envelope and the file-data reader entering decompression.
- Format link: [[rar5-archive]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
