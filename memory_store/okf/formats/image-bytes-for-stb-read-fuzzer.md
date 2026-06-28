---
type: format-family
title: "Image Bytes For Stb Read Fuzzer"
description: "Round 19 factual format contract for image-bytes-for-stb-read-fuzzer."
resource: cybergym://format/image-bytes-for-stb-read-fuzzer
tags: ["image-bytes-for-stb-read-fuzzer", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Image Bytes For Stb Read Fuzzer

## Round 19 Factual Contract

- The described bug concerns relative path strings that include a drive-like component, but the generated target consumes image data through stb image probing/loading. For that selected target, valid image magic and image structure matter more than filesystem path syntax.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
