---
type: harness-contract
title: "Libfuzzer File Wrapper harness"
description: "Input contract facts for Libfuzzer File Wrapper."
tags: ["libfuzzer-file-wrapper", "round-21"]
okf_support: 2
---
# Libfuzzer File Wrapper Harness

## Round 21 Input Contract (upx-packed-elf)

- The UPX fuzzer writes raw bytes to a temporary file and invokes a UPX operation on that file. The observed target was test/list style execution; there is no byte carving by the harness.

## Round 21 Format Links (upx-packed-elf)
- [[upx-packed-elf]]

## Round 21 Notes (upx-packed-elf)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 26 Factual Contract


### Input Contract
- The GPAC fuzz harness writes the raw input bytes to a temporary file and opens it with the ISO media reader in dump/read mode. There is no leading mode selector and no FuzzedDataProvider splitting; the payload must be a file-like MP4/BMFF object that reaches gf_isom_open_file.

### Format Links
- [[isobmff-mp4]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.

## Round 32 Input Contract
- The wrapper reads the submitted file, requires enough bytes for a selector plus instruction stream, chooses a disassembly platform from the first byte, enables detail output, and calls cs_disasm on the remaining bytes.

## Round 32 Format Links
- [[capstone-disasm-selector-plus-bytes]]

## Round 32 Notes
- These facts are descriptive harness-carving observations only; they are not causal recovery claims.
