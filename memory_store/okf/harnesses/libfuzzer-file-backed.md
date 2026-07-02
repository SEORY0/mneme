---
type: harness-contract
title: "Libfuzzer File Backed Harness"
description: "Round 7 input contract facts for libfuzzer-file-backed."
tags: ["libfuzzer-file-backed", "harness-contract", "round-7"]
okf_support: 11
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

## Round 27 Input Contract
- The libFuzzer harness writes the raw input bytes to a temporary .pa file and calls pixaRead on that file.
- It creates recognizers from the loaded PIXA, runs boot training, removes outliers with debug images requested, and then calls recognition on the removed-outlier display image.
- There is no FuzzedDataProvider split; reachability depends on the raw file being a readable Leptonica PIXA with embedded image labels.

## Round 27 Format Links
- [[leptonica-pixa-pa-with-embedded-png]]

## Round 27 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
