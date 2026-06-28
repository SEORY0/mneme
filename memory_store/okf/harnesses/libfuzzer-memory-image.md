---
type: harness-contract
title: "Libfuzzer Memory Image harness"
description: "Input contract facts for libfuzzer-memory-image."
tags: ["libfuzzer-memory-image", "round-25"]
okf_support: 0
---
# Libfuzzer Memory Image Harness

## Round 25 Input Contract
- The SleuthKit fuzzer opens raw bytes as an in-memory image, opens a filesystem of the configured type at image offset zero, recursively lists from the root inode if opening succeeds, then closes the filesystem and image.

## Round 25 Format Links
- [[ntfs-filesystem-image]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
