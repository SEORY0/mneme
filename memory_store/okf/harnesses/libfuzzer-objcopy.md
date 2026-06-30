---
type: harness-contract
title: "Libfuzzer Objcopy harness"
description: "Input contract facts for libfuzzer objcopy."
tags: ["libfuzzer-objcopy", "round-29"]
okf_support: 0
---
# Libfuzzer Objcopy Harness

## Round 29 Input Contract

- The /bin/arvo wrapper runs the objcopy libFuzzer target on a copied PoC file path. The target writes the raw PoC bytes to a temporary file, initializes BFD once, creates objcopy symbol hash tables, and invokes copy_main with only an input path and output path. The PoC does not control argv flags, there is no FuzzedDataProvider carving, and the wrapper/options path disables libFuzzer leak detection.

## Round 29 Format Links
- [[elf-or-ar]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
