---
type: harness-contract
title: "Libfuzzer Yara Dotnet Scan Mem Harness"
description: "Input contract facts for libfuzzer-yara-dotnet-scan-mem."
tags: ["libfuzzer-yara-dotnet-scan-mem", "round-30"]
okf_support: 0
train_only: true
---
# Libfuzzer Yara Dotnet Scan Mem Harness

## Round 30 Input Contract

### Input Contract
- The harness compiles a fixed YARA rule importing the dotnet module and scans the supplied file bytes directly with yr_rules_scan_mem. There is no mode byte, container prefix, checksum wrapper, or FuzzedDataProvider split; all bytes are interpreted as the scanned PE image.

### Format Links
- [[pe-dotnet]]

### Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
