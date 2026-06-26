---
type: harness-contract
title: "Libfuzzer File Backed Harness"
description: "Round 7 input contract facts for libfuzzer-file-backed."
tags: ["libfuzzer-file-backed", "harness-contract", "round-7"]
okf_support: 2
train_only: true
---
# Libfuzzer File Backed Harness

## Round 7 Input Contract
- The fuzzer writes raw input bytes to a temporary file with a .map suffix, then calls msLoadMap on
that file and frees the result. Inputs outside a fixed size range are skipped; there is no mode
selector or FuzzedDataProvider layout.
- The fuzzer writes raw bytes to a temporary file and invokes UPX list mode on that file, catching
exceptions. The input must be a complete packed file; raw ELF headers or stub fragments are not
enough to reach b_info recovery.

## Round {ROUND} Format Links
- [[mapserver-mapfile]]
- [[upx-packed-elf]]

## Round {ROUND} Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
