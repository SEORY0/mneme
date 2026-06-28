---
type: harness-contract
title: "Afl Libfuzzer Libarchive Archive Reader harness"
description: "Input contract facts for afl-libfuzzer-libarchive-archive-reader."
tags: ["afl-libfuzzer-libarchive-archive-reader", "round-24"]
okf_support: 1
---
# Afl Libfuzzer Libarchive Archive Reader Harness

## Round 24 Factual Contract

### Input Contract
- The harness feeds the input bytes as an archive stream to libarchive, enables all formats, iterates entries, and drains each entry body. There is no leading mode byte or FuzzedDataProvider split.

### Format Links
- [[rar5]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
