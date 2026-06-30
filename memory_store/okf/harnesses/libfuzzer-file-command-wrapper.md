---
type: harness-contract
title: "Libfuzzer File Command Wrapper harness"
description: "Input contract facts for libfuzzer-file-command-wrapper."
tags: ["libfuzzer-file-command-wrapper", "round-11"]
okf_support: 1
train_only: true
---
# Libfuzzer File Command Wrapper Harness

## Round 11 Input Contract
- The UPX fuzz harness writes raw bytes to a temporary file and invokes the real upx command path such as list or decompression mode. Therefore the PoC must be a complete file recognized by UPX rather than a carved libFuzzer buffer.

## Format Links
- [[elf-or-upx-packed-elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 14 Input Contract
- The fuzzer writes the raw bytes to a temporary file and invokes UPX command paths such as test/list/decompress against that file. The candidate must be a complete packed executable recognized by UPX.

## Round 14 Format Links
- [[upx-packed-elf]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 25 Input Contract
- The binutils wrapper writes raw bytes to a temporary file and opens them through BFD. BFD recognizes the PE container and reaches debug-directory handling from the file bytes.
- The binutils objdump-style wrapper writes raw input to a temporary file and lets BFD identify the object format. Ambiguous SH COFF recognition can stop before the target relocation handler is applied.
- The UPX fuzzers write raw bytes to a temporary file and invoke UPX test/list/decompress command paths. Plain ELF-like carriers without a valid packed UPX structure are typically rejected before the unpacking code.

## Round 25 Format Links
- [[pe-codeview]]
- [[coff-sh-object]]
- [[upx-packed-elf]]

## Round 25 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.

## Round 26 Factual Contract


### Input Contract
- The active runner used the decompression fuzzer: it writes raw input bytes to a temporary file and invokes the UPX decompression command path with an output file argument, then deletes both temporary files. The input must be accepted as UPX-packed before the unpacker runs; ordinary ELF files are reported as not packed. There is no FuzzedDataProvider carving or mode selector in the bytes.

### Format Links
- [[upx-packed-elf]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
