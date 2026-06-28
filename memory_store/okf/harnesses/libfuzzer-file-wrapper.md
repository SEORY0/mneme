---
type: harness-contract
title: "Libfuzzer File Wrapper harness"
description: "Input contract facts for Libfuzzer File Wrapper."
tags: ["libfuzzer-file-wrapper", "round-21"]
okf_support: 1
---
# Libfuzzer File Wrapper Harness

## Round 21 Input Contract (upx-packed-elf)

- The UPX fuzzer writes raw bytes to a temporary file and invokes a UPX operation on that file. The observed target was test/list style execution; there is no byte carving by the harness.

## Round 21 Format Links (upx-packed-elf)
- [[upx-packed-elf]]

## Round 21 Notes (upx-packed-elf)
- These are descriptive harness-carving facts only; they are not causal recovery claims.
