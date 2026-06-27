---
type: harness-contract
title: "Libfuzzer Image Coder Roundtrip harness"
description: "Input contract facts for libfuzzer-image-coder-roundtrip."
tags: ["libfuzzer-image-coder-roundtrip"]
okf_support: 0
---
# Libfuzzer Image Coder Roundtrip Harness

## Round 10 Input Contract
- The fuzzer passes raw file bytes to the GraphicsMagick coder target. The target auto-detects image format and exercises decode/encode behavior; no leading selector byte is consumed by the harness.

## Round 10 Format Links
- [[palm-pdb-image]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
