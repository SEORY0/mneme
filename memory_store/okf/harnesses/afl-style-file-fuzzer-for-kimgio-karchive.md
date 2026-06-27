---
type: harness-contract
title: "afl-style file fuzzer for kimgio/karchive harness"
description: "Descriptive harness contract facts for afl-style file fuzzer for kimgio/karchive."
tags: ["afl-style-file-fuzzer-for-kimgio-karchive", "round-18"]
okf_support: 1
train_only: true
---
# Afl Style File Fuzzer For Kimgio Karchive Harness

## Round 18 Input Contract

### Schema / Invariants
- The AFL-style wrapper feeds the raw input file to the kimgio fuzzer, which reaches KArchive archive parsing without a selector byte or FuzzedDataProvider carving. The input is a complete archive file, not a stream of separate fields.

### Format Links
- [[zip-archive]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
