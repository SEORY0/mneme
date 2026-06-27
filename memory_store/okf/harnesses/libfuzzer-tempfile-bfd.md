---
type: harness-contract
title: "Libfuzzer Tempfile BFD harness"
description: "Input contract facts for libfuzzer-tempfile-bfd."
tags: ["libfuzzer-tempfile-bfd"]
okf_support: 1
---
# Libfuzzer Tempfile BFD Harness

## Round 10 Input Contract
- The fuzzer writes the raw input to a temporary file, opens it with BFD auto-detection, and checks archive format. Inputs must therefore be complete file bytes, not an in-memory record stream.

## Round 10 Format Links
- [[bfd-archive-containing-truncated-msdos-member]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 11 Input Contract
- The harness writes the raw input bytes to a temporary file and opens that file through BFD auto-detection before checking archive format. There is no mode-selector byte and no FuzzedDataProvider field carving; all structure is in the archive bytes.

## Format Links
- [[som-library-archive]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 15 Input Contract
- The libFuzzer input is written to a temporary file, opened by BFD, and checked as an archive.
  Reaching member ELF parsing depends on archive metadata, not just a standalone ELF header. There is
  no selector byte and no FuzzedDataProvider layout.

## Format Links
- [[ar-archive-elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
