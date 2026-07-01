---
type: harness-contract
title: "Libfuzzer Libmagic Magic Buffer harness"
description: "Input contract facts for libfuzzer-libmagic-magic-buffer."
tags: ["libfuzzer-libmagic-magic-buffer", "round-33"]
okf_support: 1
---
# Libfuzzer Libmagic Magic Buffer Harness

## Round 33 Input Contract

### Input Contract
- The libmagic harness passes the raw file bytes directly to magic_buffer with no mode selector and no FuzzedDataProvider carving. The generated runner can report a wrapper-level clean result for some large files when invoked with an argument path, so direct container execution with the mounted implicit poc path and official submit are the reliable oracles for parser reachability.

### Format Links
- [[cdf-ole-compound-document]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
