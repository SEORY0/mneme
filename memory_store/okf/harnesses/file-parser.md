---
type: harness-contract
title: "File Parser Harness"
description: "Input contract facts for file-parser."
tags: ["file-parser", "round-12"]
okf_support: 0
train_only: true
---
# File Parser Harness

## Round 12 Input Contract
- The binutils-style harness consumes the raw bytes as an ELF file through BFD/ELF parser entry points. There is no fuzzer prefix; the file header determines class, endianness, program headers, and section-header absence.
- The FFmpeg harness writes or feeds the raw input as an IAMF demuxer sample through the local run_poc wrapper. There is no model-side generation or fuzzer prefix; demuxer probing and IAMF OBU parsing decide whether the parser reaches descriptor handling.

## Round 12 Format Links
- [[elf]]
- [[iamf]]

## Round 12 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
